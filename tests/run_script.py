import pyRserve

# Connect to the remote Rserve instance
rsc = pyRserve.connect('localhost', port=6311)

# Specify the full path to the script
script_path = '/srv/scripts/my_script.R'
rsc.eval(f'source("{script_path}")')

rsc.close()
