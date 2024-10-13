#!/bin/bash
echo "y" | docker system prune -a
docker-compose up --build -d
