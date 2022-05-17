from http.server import HTTPServer, BaseHTTPRequestHandler
from multiprocessing import Event
import webbrowser
import threading, os, json
import config

from config import HTTP_SECRET

class Handler(BaseHTTPRequestHandler):
    def on_event(self, js):
        print("Incoming log event:", js)

    def do_POST(self):
        if config.HTTP_SECRET in [None, ""]:
            self.send_response(404)
            self.end_headers()
            return

        secret = self.headers.get("x-application-secret")
        if secret != config.HTTP_SECRET:
            self.send_response(404)
            self.end_headers()
            return


        content_len = self.headers.get('Content-Length')
        if content_len in [None, ""]: 
            self.send_response(300)
            self.end_headers()
            return
        
        post_body = self.rfile.read(int(content_len))

        js = json.loads(post_body)
        self.on_event(js)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("{}", "utf-8"))

def start_server(handler, port=8000):
    '''Start a simple webserver serving path on port'''
    httpd = HTTPServer(('', port), handler)
    httpd.serve_forever()

def run_logging_server(handler = Handler, port = 8000):
    # Start the server in a new thread
    daemon = threading.Thread(name='daemon_server', target=start_server, args=(handler, port))
    daemon.setDaemon(True) # Set as a daemon so it will be killed once the main thread is dead.
    daemon.start()
    return daemon

if __name__ == "__main__":
    run_logging_server().join()