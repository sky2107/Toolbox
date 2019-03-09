# Creation and sharing of images

1. Change into the container something
   => docker run -it ubuntu:14.04 /bin/bash <br>
   root@container_id:/# apt-get update <br>
   For not lose everthing commit changes <br>
   => docker commit container_id new_name:tag_name <br>
   for the image
2. Saving img and containers as TAR files for sharing <br>
   =>TARBALL ???; Docker CLI import and export commands <br>
   docker export container_id > upti.tar <br>
   creating a file with all information of the container <br>
   And to import the tar file <br>
   docker import - name_of_image < name_of_tar_file.tar <br>

3. Next point

# 
# Changes in order documented

> Inspect the changes that have been made inside the container with the docker diff command <br>
> VERY USEFUL !!!

    docker diff container_id