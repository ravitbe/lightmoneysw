import logging
from logging.handlers import HTTPHandler
import SimpleHTTPServer
import SocketServer

PORT = 7777

logger_get = logging.getLogger('machine-logger')

class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        print "MACHINE got a GET from CONTROL SERVICE"
        logger_get.setLevel(logging.DEBUG)
        print "MACHINE is sending a POST to CONTROL SERVICE"
        logger_get.critical('POST from machine')
        print "END DO_GET MACHINE"
        return


def machine_thread():
    logger_get.addHandler(HTTPHandler("localhost:8888", "/" ,method='POST' ))
    try:
        server = SocketServer.TCPServer(("", PORT), myHandler)
        print '\nStarted MACHINE - httpserver on port ' , PORT
        #Wait forever for incoming http requests
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()




