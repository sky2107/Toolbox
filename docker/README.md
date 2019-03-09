# Docker

> Linux

<h2><b><u>Installation</u></b></h2>

    sudo apt-get update
    sudo apt-get install -y wget
    sudo wget -qO- https://get.docker.com/ | sh
    sudo docker --version
    => Docker version current

> You can stop, start, and restart  
> the service. For example, to restart it:

    sudo service docker restart

> If you want to use docker from a nonroot user,
> add the user account to the docker group:

     sudo gpasswd -a <user> docker

> Exit the current shell and log in again or start a new 
> shell for the change to take effect.

<h2><b><u>Working with docker</u></b></h2>

> Run from images

    sudo docker run ...

> Just craeting without starting it immediately

    sudo docker create ...

> Run container if existing

    sudo docker start container_id

> Enter into a running container e.g. ubuntu

    sudo docker exec container_id path/target

> Stop container

    sudo docker stop container_id

> Show all running containers

    sudo docker ps

> List all containers

    sudo docker docker ps -a

> all containers but only ids

    docker ps -q -a

> rm all stopped containers

    docker container prune

> remove container

    sudo docker rm container_id || container_name

> Show images

    sudo docker images

> Remove image if not in use from a container

    sudo docker rmi image_id || imgae_name

> If you have <b>a lot of stopped containers</b> that you would like
> to remove, use a subshell to do it in one command. The -q 
> option of docker ps will return only the containers’ IDs: 

    docker rm $(docker ps -a -q)

> Rename image

    docker tag nameOFimage:plusTag newName:optionalNewTagName
#
<h2><b><u>Tags</u></b></h2>

1. -p => giving the ports to connect from outside
2. -d => will not stop running
3. --name => give container a name before building
4. -q => gives only the id`s back
5. -t => gives the tag name

> Questions about tags

1. -i
2. -m
3. --expose

> Question in diffrent topics

1. SIGTERM 
2. SIGKILL
3. sudo docker kill ... vs sudo docker rm ...
4. grace period 
5. sudo docker restart ... why not start
6. PACKER ???
7. ONBUILD function
8. WORKDIR ??

#
# Building images with Dockerfile

> Bad practice multiple RUN commands will add unnecessary layers to the image. Also to use the ADD command to copy a simple file it is better to use COPY. <br>
> ADD => allows more-complex file copy scenarios <br>

# STOPPED page 100

# Todos

1. BitBucket + Github intensive
2. LINKING not really understood !!!!!!!!!!
3. Networking tutorial repeat