# Here is an example of a function to run 
# a script in Rserve. Rserve runs in a docker container
# you pass it a directory on the host machine for it to run a file

import os
import pyRserve

def run_r_script(directory, script_name):
    """
    Connects to the Rserve instance, runs the R script specified, and prints the result.
    
    Parameters:
    - directory: The directory where the R script is located.
    - script_name: The name of the R script to run.
    
    Returns:
    - The result of the R script execution.
    """
    # Connect to the remote Rserve instance
    rsc = pyRserve.connect('localhost', port=6311)

    # Combine the directory and script name to get the full path
    full_script_path = os.path.join(directory, script_name)

    # Run the R script (send the script to be sourced remotely)
    result = rsc.eval(f"source('{full_script_path}')")

    # Extract the actual value from the TaggedList
    result_value = result[0]  # Assuming the result is the first element of the list

    print(f"Result from R script: {result_value}")

    # Close the connection
    rsc.close()

    return result_value

# example usage - you can change my_directory to where ever your file is on the host machine
# aka ec2 instance
#my_directory = '/Users/fausto-personal/Documents/GitHub/remote-r/scripts/'
my_directory = ''
script_path = 'my_script.R'
run_r_script(my_directory, script_path)
