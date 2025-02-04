from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
import subprocess
import os
import pyRserve 

app = Flask(__name__)
CORS(app)

host = "rserve" # name of docker container
port = 6311  

# Run via python
@app.route('/run-script-native', methods=['POST'])
def run_script():
    script_path = '/srv/scripts/my_script.R' 
    try:
        print("starting execution...")
        # execute the R script using subprocess
        result = subprocess.run(['Rscript', script_path], capture_output=True, text=True, check=True)
        return jsonify({'status': 'success', 'output': result.stdout}), 200
    except subprocess.CalledProcessError as e:
        # handle errors (e.g., script failure)
        return jsonify({'status': 'error', 'message': e.stderr}), 500

# Run rserve commands via api   
@app.route('/run-command-rserve', methods=['POST'])
def run_command_rserve(): 
    try:
        conn = pyRserve.connect(host=host, port=port)
        result = conn.eval('rnorm(10)')
        result_list = result.ravel().tolist()
        # close the connection
        conn.close()        

        return jsonify({'status': 'success', 'output': result_list}), 200
    except subprocess.CalledProcessError as e:
        # handle errors (e.g., script failure)
        return jsonify({'status': 'error', 'message': e.stderr}), 500

# Run via rserve container:
@app.route('/run-script-rserve', methods=['POST'])
def run_script_rserve():
    script_path = '/srv/scripts/my_script.R'
    try:
        print("starting execution via rserve...")

        conn = pyRserve.connect(host=host, port=6311)
        
        result = conn.eval(f"source('{script_path}')")
        
        if isinstance(result, pyRserve.TaggedList):
            result_value = result[0]  # Accessing the first element (assuming it's the output)
        else:
            result_value = result  # If it's not a TaggedList, use it as-is
        
        
        # Close the connection
        conn.close()
        
        # Return the result in the response message
        return jsonify({'status': 'success', 'output': result_value}), 200
    
    except Exception as e:
        # Handle connection errors or script execution errors
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
@app.route('/run-command-rserve', methods=['POST'])
def send_command_rserve(): 
    try:
        # Get the R code from the POST request's JSON payload
        r_code = request.json.get('r_code')
        
        if not r_code:
            return jsonify({'status': 'error', 'message': 'No R code provided'}), 400
        
        # Connect to Rserve
        conn = pyRserve.connect(host=host, port=port)
        
        # Execute the provided R code
        result = conn.eval(r_code)
        
        # Convert the result into a serializable format (if it's a TaggedList)
        result_value = result[0] if isinstance(result, pyRserve.TaggedList) else result
        
        # Close the connection
        conn.close()
        
        # Return the result
        return jsonify({'status': 'success', 'output': result_value}), 200
    
    except Exception as e:
        # Handle any errors that occur during the R code execution
        return jsonify({'status': 'error', 'message': str(e)}), 500

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
