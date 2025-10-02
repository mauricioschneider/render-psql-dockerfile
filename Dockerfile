# Stage 1: Use a minimal base image
FROM alpine:3.18

# Install Python 3 and PostgreSQL client tools
# 'postgresql-client' provides utilities like psql, pg_dump, etc.
RUN apk update && \
    apk add --no-cache python3 py3-pip postgresql-client && \
    rm -rf /var/cache/apk/*

# Set the working directory in the container
WORKDIR /app

# Copy the server script into the container
# We'll create a simple server.py for this example
COPY server.py /app/

# Expose the port the server will listen on
EXPOSE 10000

# Command to run the Python server
# This script uses Python's built-in http.server module to serve content
CMD ["python3", "server.py"]