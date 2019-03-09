# Linux

> Change password

    sudo passwd

> Change folder name

    mv olf_folder new_folder

> copy file to this location

    cp SOURCE DEST
    cp SOURCE DIRECTORY
    cp SOURCE1 SOURCE2 SOURCE3 SOURCEn DIRECTORY
    cp [OPTION] SOURCE DEST
    cp [OPTION] SOURCE DIRECTORY

> Repeat lass command maybe forgot sudo

    sudo !!

> open nano directly for multiple commands

    ctrl + x + e
    type all cmds

> creating ram temporary

    mkdir ram
    cd ram
    dd if=/dev/zero of=test.iso bs=1M count=8000

    rm test.iso
    cd ..
    # without mount

    mount -t tmpfs tmpfs /mnt/ram -o size=8192M
    cd ram
    dd if=/dev/zero of=test.iso bs=1M count=8000
    # much faster

> not in history SPACE between cmds

    _sudo something

> longer cmd forgot a flag

    fc

> sub folders

    mkdir -p folder/{sub1,sub2}/{sub1,sub2,sub3}

> intersect stout and log to file

    cat file | tee -a log | cat > /dev/null

> leave terminal but leave all processes running

    disown -a && exit

> ps aux | grep sleep

# Quellen

> [Utube_link](https://www.youtube.com/watch?v=Zuwa8zlfXSY&t=302s)
