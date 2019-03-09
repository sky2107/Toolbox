# <u> Redis</u> 

[Redis official site click for Information](https://redislabs.com)

> Anaconda python 3.7 redis-py libary

    # into docker container 
    docker run --name=my_redis -d -p 6379:6379 image_name # redis in this case
    docker exec <container_id> -it /bin/bash 
    # jump into the container of redis image
    container_id# redis-cli
    container_id# ping # check conection
    PONG # if it is working
    container_id# SET part_a 1 # SET key value
    container_id# GET part_a
    "1"
    container_id# INCR part_a
    (integer) 2
    container_id#
