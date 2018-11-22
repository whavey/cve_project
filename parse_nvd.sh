#!/bin/bash

images=`docker images | awk '{print $1}'`
sysctl -w vm.max_map_count=262144
docker-compose up -d

