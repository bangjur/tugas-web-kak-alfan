#!/bin/bash

# File ini digunakan untuk mengupdate web flask ketika terjadi perubahan pada kode website.
# File ini diletakkan pada /etc/systemd/system/update_docker.service dimana setiap kali 
# instance di-reboot, maka docker otomatis mem-build image baru (webiste otomatis ter-update pula) 
# dan menghapus image lawas. 

# Update and run the Docker containers in detached mode
docker-compose up --build -d

# Clean up unused Docker images, containers, and networks
echo "y" | docker system prune -f
