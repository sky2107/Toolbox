# OpenCV

> install opencv <br>
> dependencies

    sudo apt-get update
    sudo apt-get upgrade

    # Remove any previous installations of x264</h3>
    sudo apt-get remove x264 libx264-dev
    
    # We will Install dependencies now
    
    sudo apt-get install build-essential checkinstall cmake pkg-config yasm
    sudo apt-get install git gfortran
    sudo apt-get install libjpeg8-dev libjasper-dev libpng12-dev
    
    # If you are using Ubuntu 14.04
    sudo apt-get install libtiff4-dev
    # If you are using Ubuntu 16.04
    sudo apt-get install libtiff5-dev # choosen
    
    sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev
    sudo apt-get install libxine2-dev libv4l-dev
    sudo apt-get install libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
    sudo apt-get install qt5-default libgtk2.0-dev libtbb-dev
    sudo apt-get install libatlas-base-dev ######
    sudo apt-get install libfaac-dev libmp3lame-dev libtheora-dev
    sudo apt-get install libvorbis-dev libxvidcore-dev
    sudo apt-get install libopencore-amrnb-dev libopencore-amrwb-dev
    sudo apt-get install x264 v4l-utils
    
    # Optional dependencies
    sudo apt-get install libprotobuf-dev protobuf-compiler
    sudo apt-get install libgoogle-glog-dev libgflags-dev
    sudo apt-get install libgphoto2-dev libeigen3-dev libhdf5-dev doxygen

> python installation

    sudo apt-get install python-dev python-pip python3-dev python3-pip

    # virtual enviroment
    python3 -m venv .
    pip install opencv-contrib-python

    pip install opencv-python-headless
    pip install opencv-contrib-python-headless
