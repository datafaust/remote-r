# # Set the IP and port for JupyterHub
# c.JupyterHub.bind_url = 'http://0.0.0.0:8000'

# # Ensure you're using DummyAuthenticator
# c.JupyterHub.authenticator_class = 'dummy'

# # Configure DummyAuthenticator
# c.DummyAuthenticator.password = 'password'  # Set the password for dummy authentication
# c.DummyAuthenticator.username_map = {"dummy": "dummy"}  # Map 'dummy' to itself
# c.Authenticator.allow_all = True  # Allow all users to authenticate

# # Configure Spawner to use SimpleLocalProcessSpawner (runs Jupyter as a local process)
# c.JupyterHub.spawner_class = 'simple'

# # Set the default page to JupyterLab
# c.Spawner.default_url = '/lab'
# c.Spawner.http_timeout = 60
# c.Spawner.start_timeout = 60

from jupyterhub.auth import PAMAuthenticator

c = get_config()

# Disable PAM password handling for simplicity (not recommended for production)
c.JupyterHub.authenticator_class = PAMAuthenticator

# Automatically create system users for JupyterHub users
c.LocalAuthenticator.create_system_users = True

# Set the allowed users (no need for password handling here if using PAM)
c.Authenticator.allowed_users = {'dummy'}

# Set default Spawner (this can be customized based on your needs)
c.Spawner.cmd = ['jupyter-labhub']

# Set default URL for users (optional)
c.Spawner.default_url = '/tree'

# JupyterHub port
c.JupyterHub.port = 8000

