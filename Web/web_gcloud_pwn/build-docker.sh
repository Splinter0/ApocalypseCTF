#!/bin/bash
docker rm -f web_gcloud_pwn
docker build --tag=web_gcloud_pwn .
docker run -p 1337:80 -it --rm --privileged --name=web_gcloud_pwn web_gcloud_pwn
