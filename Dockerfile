FROM nvidia/cuda:11.0-devel-ubuntu20.04

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113

WORKDIR /work