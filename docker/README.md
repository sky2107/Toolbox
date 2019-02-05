# Docker

> Linux

<h2><b><u>Installation</u></b></h2>

>
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

> Running containers

    sudo docker ps

> List all containers

    sudo docker docker ps -a

> remove container

    sudo docker rm container_id || container_name

> Show images

    sudo docker images

> Remove image if not in use from a container

    sudo docker rmi image_id || imgae_name

> Tags

1. -p => giving the ports to connect from outside
2. -d => will not stop running
3. --name => give container a name before building

> Questions about tags

1. -i
2. -t
3. -m