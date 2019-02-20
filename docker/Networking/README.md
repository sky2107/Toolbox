# Docker Networking

> finding IP address of a container

    docker run -d -- name nginx nginx
    docker inspect --format ' {{ .NetworkSettings.IPAddress }}' nginx

> automatically setting a port free with -P <br>
> manually with -p 1111:2222 e.g.

> Linking  Containers