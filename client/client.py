import SimpleHTTPServer
import SocketServer



PORT = 9999

class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    #Handler for the GET requests
    def do_GET(self):
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        print "got result back from 8888"
        print "\nEND DO_GET CLIENT" 
        return
    def do_POST(self):
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        print "CLIENT got a POST from CONTROL SERVICE"    
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        print "POST = ", post_body
        print "\nEND DO_POST CLIENT" 
        return


if __name__ == "__main__":
    try:
        server = SocketServer.TCPServer(("", PORT), myHandler)
        print 'Started CLIENT httpserver on port ' , PORT
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()



