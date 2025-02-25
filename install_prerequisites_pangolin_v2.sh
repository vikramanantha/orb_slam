#!/bin/bash

# Update package list
echo "Updating package list..."
sudo apt update

# Install required packages
echo "Installing required packages..."
sudo apt install -y \
    libgl1-mesa-dev \
    libwayland-dev \
    libxkbcommon-dev \
    wayland-protocols \
    libegl1-mesa-dev \
    libc++-dev \
    libepoxy-dev \
    libglew-dev \
    libeigen3-dev \
    cmake \
    g++ \
    libjpeg-dev \
    libpng-dev \
    libavcodec-dev \
    libavutil-dev \
    libavformat-dev \
    libswscale-dev \
    libavdevice-dev

sudo apt-get install -y ninja-build

echo "Installation complete."

