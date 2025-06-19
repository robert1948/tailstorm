#!/bin/bash

# Shut down any previous containers/volumes
docker compose down -v

# Rebuild without cache
docker compose build --no-cache

# Start Docker Compose in the background
docker compose up &

# Wait a few seconds for the server to start
sleep 5

# Open the browser (Linux + Chrome)
xdg-open http://localhost:8000

# Optional: tail logs (remove if you want clean terminal)
docker compose logs -f
