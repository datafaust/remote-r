FROM rocker/rstudio:4.0.5
 
#install R and Python dependencies 
RUN apt-get clean all && \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y \
    libhdf5-dev \
    libcurl4-gnutls-dev \
    libssl-dev \
    libxml2-dev \
    libpng-dev \
    libxt-dev \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libglpk40 \
    libgit2-28 \
    python3.6 \ 
    python3-pip \ 
    python3-setuptools \ 
    python3-dev \
  && apt-get clean all && \
  apt-get purge && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
 
#RUN Rscript -e "install.packages(c('rmarkdown', 'tidyverse', 'workflowr', 'BiocManager', 'magrittr', 'jsonlite', 'lubridate', 'rlang', 'assertthat', 'foreach', 'devtools'));"
#RUN Rscript -e "BiocManager::install(version = '3.12')"



#COPY .Rprofile /home/rstudio/

#RUN Python package installations
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
