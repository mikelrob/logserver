#! /usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        print("Received POST")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()

        data = json.loads(self.data_string)
        print(f"JSON received: \n\n {data}")

if __name__ == "__main__":

    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    hostName = s.getsockname()[0]
    print(hostName)
    s.close()

    serverPort = 8000

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
