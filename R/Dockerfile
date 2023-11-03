# you probably should use particular tag
FROM rocker/rstudio:latest

LABEL source="https://github.com/Wodajo/Data-science/R/Dockerfile"

MAINTAINER Wodajo <wodajo@pm.me>

RUN apt update && \
    apt upgrade -y && \
    apt install -y \
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
        libgit2-dev \
    && apt clean && \
    apt purge && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN Rscript -e "install.packages('pak', repos = c(CRAN = 'https://cloud.r-project.org'))"
RUN Rscript -e "pak::pkg_install(renv)"
#RUN Rscript -e "install.packages('pak', repos = c(CRAN = 'https://cloud.r-project.org'))

WORKDIR /home/rstudio


