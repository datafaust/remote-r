FROM rocker/r-ver:4.4.2

# Install necessary packages
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Install Rserve
RUN R -e "install.packages('Rserve')"

# Expose Rserve port
EXPOSE 6311

# Start Rserve directly when the container starts
CMD R -e "Rserve::run.Rserve()"
