# This dockerfile is useful for running the CI pipeline locally.
# Build and tag an image:
#
#    cat .github/workflows/Dockerfile | docker build - -t ubuntu-builder
#
# then use https://github.com/nektos/act to run locally, using this image
#
#    act -P ubuntu-latest=ubuntu-builder

FROM ubuntu:20.04

RUN apt-get update \
    && apt-get upgrade -y \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    curl \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*
