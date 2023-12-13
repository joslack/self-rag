#!/bin/bash

set -xe

docker run -v ./index.html:/frontend/index.html -it -p 8000:80 frontend-image:latest

