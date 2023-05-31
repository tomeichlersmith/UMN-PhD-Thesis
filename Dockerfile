FROM ubuntu:22.04
LABEL ubuntu.version="22.04"
MAINTAINER Tom Eichlersmith <eichl008@umn.edu>

ENV DEBIAN_FRONTEND=noninteractive

# instead of spending time trying to figure out which specific texlive
# packages we want, we just install 'texlive-full' which has everything
# including latexmk, the full listing can be viewed online:
#   https://packages.ubuntu.com/jammy/texlive-full
RUN apt-get update &&\
    apt-get install -y \
      texlive-full \
    && rm -rf /var/lib/apt/lists/* &&\
    apt-get autoremove --purge &&\
    apt-get clean all

