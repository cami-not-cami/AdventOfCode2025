# use base Image: Ubuntu 26.04
FROM ubuntu:26.04


# update packages and install Python 3
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \ 
    python3-numpy \
    python3-scipy \ 
    && rm -rf /var/lib/apt/lists/*

# set the working directory inside the container
WORKDIR /app

# copy all project files into the container
COPY . .

# give rights  to the script
RUN chmod +x start.sh
CMD ["./start.sh"]
