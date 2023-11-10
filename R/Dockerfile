# you probably should use particular tag
FROM rocker/rstudio:latest

LABEL source="https://github.com/Wodajo/Data-science/R/Dockerfile"

MAINTAINER Wodajo <wodajo@pm.me>

#RUN apt-get update && \
#RUN    apt-get upgrade -y && \
#RUN    apt-get install -y \
#        libhdf5-dev \
#        libcurl4-gnutls-dev \
#        libssl-dev \
#        libxml2-dev \
#        libpng-dev \
#        libxt-dev \
#        zlib1g-dev \
#        libbz2-dev \
#        liblzma-dev \
#        libglpk40 \
#        libgit2-dev \
#    && apt-get clean my room madafaka&& \
#    apt-get purge && \
#    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN Rscript -e "install.packages('pak', repos = c(CRAN = 'https://cloud.r-project.org'))"
RUN Rscript -e "pak::pkg_install('renv')"
#RUN Rscript -e "install.packages('pak', repos = c(CRAN = 'https://cloud.r-project.org'))

# copy user settings
#COPY --chown=rstudio:rstudio rstudio/rstudio-prefs.json /home/rstudio/.config/rstudio
# copy .Rprofile info (e.g. .libPaths("/packages/)) 
#COPY --chown=rstudio:rstudio rstudio/.Rprofile /home/rstudio/


WORKDIR /home/rstudio


