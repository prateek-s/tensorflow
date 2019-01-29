#!/bin/bash

docker run -it -w /tensorflow -v /home/prateeks/tensorflow:/tensorflow -v $PWD:/mnt -v /data2/pnfs/:/pnfs -e HOST_PERMS="$(id -u):$(id -g)" -e TF_CONFIG="$(cat master.env)" --name "tf-master" --net tfnet --ip 172.18.0.2 --cpus 4 -d  tfr1.11:v1

docker run -it -w /tensorflow -v /home/prateeks/tensorflow:/tensorflow -v $PWD:/mnt -v /data2/pnfs/:/pnfs -e HOST_PERMS="$(id -u):$(id -g)" -e TF_CONFIG="$(cat ps.env)" --name "tf-ps" --net tfnet --ip 172.18.0.3 --cpus 4 -d  tfr1.11:v1

docker run -it -w /tensorflow -v /home/prateeks/tensorflow:/tensorflow -v $PWD:/mnt -v /data2/pnfs/:/pnfs -e HOST_PERMS="$(id -u):$(id -g)" -e TF_CONFIG="$(cat worker-0.env)" --name "tf-worker-0" --net tfnet --ip 172.18.0.4 --cpus 4 -d  tfr1.11:v1

docker run -it -w /tensorflow -v /home/prateeks/tensorflow:/tensorflow -v $PWD:/mnt -v /data2/pnfs/:/pnfs -e HOST_PERMS="$(id -u):$(id -g)" -e TF_CONFIG="$(cat worker-1.env)" --name "tf-worker-1" --net tfnet --ip 172.18.0.5 --cpus 4 -d  tfr1.11:v1


#docker exec tf-master /tensorflow/start-cifar10.sh
