# you probably should use particular tag
FROM rocker/rstudio:4.2.2

LABEL source="https://github.com/Wodajo/Data-science/R/Dockerfile"

MAINTAINER Wodajo <wodajo@pm.me>

RUN sudo su
#-e ROOT=TRUE
RUN apt-get update && \
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
        libgit2-dev \
    && apt-get clean my room madafaka && \
    apt-get purge
#    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN Rscript -e "install.packages('pak', repos = c(CRAN = 'https://cloud.r-project.org'))"
RUN R -e "install.packages('renv', repos = c(CRAN = 'https://cloud.r-project.org'))"
#RUN Rscript -e "pak::pak('renv')"
#RUN Rscript -e "install.packages('pak', repos = c(CRAN = 'https://cloud.r-project.org'))

# copy user settings
#COPY --chown=rstudio:rstudio rstudio/rstudio-prefs.json /home/rstudio/.config/rstudio
# copy .Rprofile info (e.g. .libPaths("/packages/)) 
#COPY --chown=rstudio:rstudio rstudio/.Rprofile /home/rstudio/


#WORKDIR /home/rstudio


