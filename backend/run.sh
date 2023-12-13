#!/bin/bash

set -xe

docker run -v ./app.py:/backend/app.py -it -p 5001:5001 backend-image:latest
