# Use the official JupyterHub image as a base
FROM jupyterhub/jupyterhub:latest

# Install necessary packages (if any)
RUN apt-get update && apt-get install -y \
    adduser \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Create the 'dummy' user
RUN adduser --disabled-password --gecos "" --home /home/dummy dummy \
    && mkdir -p /home/dummy \
    && chown dummy:dummy /home/dummy

# Ensure proper ownership and permissions for JupyterHub's directories
RUN chown -R dummy:dummy /srv/jupyterhub && \
    chmod -R 755 /srv/jupyterhub

# Expose port for JupyterHub
EXPOSE 8000

# Start JupyterHub when the container runs
CMD ["jupyterhub"]
