# Use miniconda as base image
FROM continuumio/miniconda3

# Install jupyternotebook
RUN conda install -y jupyter

# Clone the repo "https://github.com/mijanr/LeetCode.git" into the docker image
# First create a directory projects at the home directory
RUN mkdir /home/projects
WORKDIR /home/projects

# Clone the repo
RUN git clone https://github.com/mijanr/LeetCode.git

# Activate the environment
RUN echo "source activate" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH

# Set the working directory
WORKDIR /home/projects/LeetCode