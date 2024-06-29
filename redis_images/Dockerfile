# Use a base image that supports systemd
FROM ubuntu:latest

# Install systemd
RUN apt-get update && \
    apt-get install -y systemd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt update && \
    apt install sudo && \
    apt install && \
    sudo apt install -y lsb-release curl gpg && \
    curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list && \
    sudo apt-get install -y redis


EXPOSE 6379

# Enable systemd as init system
STOPSIGNAL SIGRTMIN+3
CMD ["/lib/systemd/systemd"]


# Run with : docker run --privileged --tmpfs /run --tmpfs /run/lock --name redis-practice -p 6379:6379 -d redis_image
