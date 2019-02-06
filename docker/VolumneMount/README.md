# Volumne

> Mount

    sudo docker create --name ubuntu_name -it -v "$PWD":/cookbook ubuntu:14.04 /bin/bash

1. "$PWD" => current position in path of home system
2. :/creatingFolder => in this e.g. cookbook
3. tag_name in tihis case ubuntu:14.04
4. Path to start in container when u enter it

#

> Questiona

1. sudo docker inspect  -f {{.Mounts}} container_id <br> 
   => u can check if the container is connected or mounted
2. docker cp =>
3. docker ?