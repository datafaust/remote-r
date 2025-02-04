
FROM rocker/r-ver:4.4.2

# Install necessary packages including netstat
RUN apt-get update && apt-get install -y \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# Install Rserve
RUN R -e "install.packages('Rserve')"

# Copy the Rserv.conf into the container
COPY ./Rserv.conf /etc/Rserv.conf

# Expose Rserve port
EXPOSE 6311

# Set working directory
WORKDIR /srv/scripts

# Start Rserve, using the Rserv.conf file (the default configuration path)
#CMD R -e "Rserve::run.Rserve()"
CMD R -e "Rserve::run.Rserve(config.file = '../../etc/Rserv.conf')"
