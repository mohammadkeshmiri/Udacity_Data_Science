FROM ubuntu:22.04

# Setup environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV NVIDIA_VISIBLE_DEVICES ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES:-all}

RUN apt update \
    && apt upgrade -y \
    && apt install -y \
    python3-pip

RUN apt-get update \
    && apt-get install -y git

RUN pip install --upgrade pip

RUN pip3 install \
    notebook \
    matplotlib \
    pandas \
    -U scikit-learn \


RUN apt-get install -y python3-pyqt5

RUN echo "set +e" | tee -a ~/.bashrc

CMD ["bash"]
