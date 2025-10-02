# server.py
import http.server
import socketserver

PORT = 10000
HOST = "0.0.0.0"

# Use SimpleHTTPRequestHandler for serving files from the current directory
Handler = http.server.SimpleHTTPRequestHandler

print(f"Serving at {HOST}:{PORT}")
# Start the server with the host specified
with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    httpd.serve_forever()