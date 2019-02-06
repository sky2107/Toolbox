# CP docker

> cp cmd

    docker run -d --name testcopy ubuntu:14.04 sleep 360 
    docker exec -ti testcopy /bin/bash 
    root@b81793e9eb3e:/# cd /root 
    root@b81793e9eb3e:~# echo 'I am in the container' > file.txt 
    root@b81793e9eb3e:~# exit 

> Now to get the file that you just created in the container back in the host, docker cp does the work:

    docker cp testcopy:/root/file.txt .
    cat file.txt 
    => I am in the container

> A nice use case is to copy from one container to another container, which is a matter of combining the two methods by temporarily saving the files on the host. For example, if you want to transfer /root/file.txt from two running containers with the names c1 and c2, use the following:
1.20 Copying Data to and from Containers | 35

    docker cp c1:/root/file.txt . 
    docker file.txt c2:/root/file.txt 