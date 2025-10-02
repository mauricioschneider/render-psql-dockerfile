# server.py
import http.server
import socketserver

PORT = 10000

# Use SimpleHTTPRequestHandler for serving files from the current directory
Handler = http.server.SimpleHTTPRequestHandler

print(f"Serving at port {PORT}")
# Start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()