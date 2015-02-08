import logging
from logging.handlers import HTTPHandler
import SimpleHTTPServer
import SocketServer


PORT = 8888
logger_post = logging.getLogger('cs_post-logger')
logger_get = logging.getLogger('cs_get-logger')


class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):         
        print "CONTROL SERVICE got a GET"
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        logger_get.setLevel(logging.DEBUG)
        #logger_get.addHandler(HTTPHandler("localhost:7777", "/"))
        logger_get.warning('log from 8888')  
        print "END DO_GET CS"         
        return
    
    def do_POST(self):
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        print "CONTROL SERVICE got a POST from machine"    
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        print "POST = ", post_body
        print "CONTROL SERVICE is sending POST to client"
        logger_post.setLevel(logging.WARNING)
        logger_post.warning('sending POST to client')
        print "END DO_POST CS"
        return



def control_service_thread():
    logger_get.addHandler(HTTPHandler("localhost:7777", "/"))
    logger_post.addHandler(HTTPHandler("localhost:9999", "/", method='POST'))
    try:
        server = SocketServer.TCPServer(("", PORT), myHandler)
        print '\nStarted CONTROL SERVICE - httpserver on port ' , PORT
        #Wait forever for incoming http requests
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()
        

import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('localhost', 4443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='path/to/localhost.pem', server_side=True)
httpd.serve_forever()







