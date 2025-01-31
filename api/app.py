from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

@app.route('/run-script', methods=['POST'])
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
