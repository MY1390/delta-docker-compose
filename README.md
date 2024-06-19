# Delta Lake with Docker-Compose

This repository is a fork of [delta-docker](<https://github.com/delta-io/delta-docker>). I created this repository because I wanted to use docker-compose on Ubuntu(x86-64) and python3 for personal purposes.

## Working with Docker

### Install Docker

Older versions of Docker can sometimes cause issues, so I recommend following the installation method provided in the official documentation (I wasn't aware of this and ended up wasting a lot of time).

<https://docs.docker.com/engine/install/ubuntu/>

### Build the Image and docker-compose

```bash
# build
sudo docker build -t delta_pyspark_quickstart -f Dockerfile_delta_quickstart .
# compose
sudo docker-compose up -d
#login
sudo docker exec -it delta_pyspark /bin/bash
```
