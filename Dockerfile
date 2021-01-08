FROM ubuntu:20.04

# Update and add package repo
RUN apt-get update
RUN echo '12' | echo '1' | apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa


# Install pip, python and other libraries
RUN apt install -y python3-pip python3.7-dev libomp-dev git vim wget unzip libsm6 libxrender1

# Update pip and install dependencies
RUN python3.7 -m pip install -U pip
RUN python3.7 -m pip install git+https://github.com/Jittor/jittor.git
RUN python3.7 -m pip install jittor==1.1.7.0 pyqt5==5.9.2 Pillow scipy dominate opencv-python==4.1.0.25

# Clone the original repo
RUN git clone https://github.com/IGLICT/DeepFaceDrawing-Jittor
RUN mv /DeepFaceDrawing-Jittor/heat/bg.jpg /DeepFaceDrawing-Jittor/heat/.jpg

# Testing Jittor and download some more dependencies
RUN python3.7 -m jittor.test.test_example