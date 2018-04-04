#FROM 	ubuntu:16.04
FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04

RUN 	apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y --no-install-recommends python python-dev python-pip build-essential cmake git pkg-config libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libatlas-base-dev gfortran libavresample-dev libgphoto2-dev libgstreamer-plugins-base1.0-dev libdc1394-22-dev && \
	apt-get install -y --no-install-recommends dialog apt-utils git gdb && \
	apt-get install -y --no-install-recommends g++ libpng12-dev libjpeg-dev libeigen3-dev && \
	apt-get install -y libboost-atomic-dev libboost-chrono-dev libboost-date-time-dev libboost-dev libboost-program-options-dev libboost-exception-dev libboost-filesystem-dev libboost-serialization-dev libboost-system-dev libboost-thread-dev libboost-timer-dev libtbb-dev libdevil-dev libboost-test-dev && \
	pip install numpy && \
	pip install pillow && \
	cd /opt && \
	git clone https://github.com/opencv/opencv_contrib.git && \
	cd opencv_contrib && \
	git checkout 3.4.1 && \	
	cd /opt && \
	git clone https://github.com/opencv/opencv.git && \
	cd opencv && \
	git checkout 3.4.1 && \
	mkdir build && \
	cd build && \
	cmake 	-D CMAKE_BUILD_TYPE=RELEASE \
		-D BUILD_NEW_PYTHON_SUPPORT=ON \
		-D CMAKE_INSTALL_PREFIX=/usr/local \
		-D INSTALL_C_EXAMPLES=OFF \
		-D INSTALL_PYTHON_EXAMPLES=OFF \
		-D OPENCV_EXTRA_MODULES_PATH=/opt/opencv_contrib/modules \
		-D PYTHON_EXECUTABLE=/usr/bin/python2.7 \
		-D BUILD_EXAMPLES=OFF /opt/opencv && \
	make -j $(nproc) && \
	make install && \
	ldconfig && \
	apt-get clean && rm -rf /var/lib/apt/lists/* && \
	rm -rf /opt/opencv*

CMD /bin/bash

