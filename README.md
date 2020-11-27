# Python101

This is an example project for Rockstar G5

## Pre-Requisites
- Python = 3
- Docker >= 19.03

## Instructions:

- Clone this repo
- Create **Docker** image as `root`:
  - `docker build -t python101 .`
- Run **Docker** image as root:
  - `docker run -it --rm -p 5000:5000 --name python101-container
      python101`

- Run **Docker** image as root (service mode):
  - `docker run -p 5000:5000 --name python101-container
      python101`

- Run **Docker** image as root (detach mode):
  - `docker run -d -p 5000:5000 --name python101-container
      python101`
