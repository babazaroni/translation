FROM babazaroni/docker-opencv

RUN 	apt-get update && \
	apt-get upgrade -y

#RUN	apt-get install nano

RUN	cd root && \
	git clone https://github.com/babazaroni/CCTag.git && \
	cd CCTag && \
	git checkout specialCases && \
	mkdir build && \
	cd build && \
	cmake .. -DOpenCV_DIR=/usr/local/share/OpenCV/ && \
	make -j `nproc`


CMD /bin/bash

