###########################
# Author:  Don C. Weber (@cutaway)
# Purpose: Simple python-based web server to provide local access to a local repo of PwnWiki.io
# Usage:   python pypwnwiki.py [-h] [-s x.x.x.x] [-p int]'
# Note:    Go forth and do good things. - cutaway
#
# Inspired from: 
#          PwnWiki.io recommendation to use "python -m SimpleHTTPServer" for offline use
#          http://stackoverflow.com/questions/12268835/is-it-possible-to-run-python-simplehttpserver-on-localhost-only
#
# TODO:    Write Ruby-On-Rails version for those who just HAVE to use Ruby.   <- Yeah, right.
###########################
import sys
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer

SERVER = '127.0.0.1'
PORT   = 1337

def usage():
    print sys.argv[0] + ' [-h] [-s x.x.x.x] [-p int]'
    print "    -h: This is it."
    print "    -s <x.x.x.x>: Server address in dot notation. Local host is default."
    print "    -p <int>: Port number in decimal. Port 1337 is default."
    sys.exit()

def pwnwiki(server,port):

    # Test server and port are still set
    if not server or not port:
        usage()

    # Configure SimpleHTTPServer
    protocol = "HTTP/1.0"
    server_address = (server, port)
    HandlerClass=SimpleHTTPRequestHandler
    ServerClass=BaseHTTPServer.HTTPServer
    HandlerClass.protocol_version = protocol

    # Run server
    httpd = ServerClass(server_address, HandlerClass)
    sa = httpd.socket.getsockname()
    print "Serving local PwnWiki.io on", sa[0], "port", sa[1], "..."
    print "Happy Hunting...."
    httpd.serve_forever()

if __name__ == "__main__":

    # Hangle options from command line by processing one at a time
    ops = ['-h','-s','-p']
    while len(sys.argv) > 1:
        op = sys.argv.pop(1)
        if op == '-h':
            usage()
        if op == '-s':
            SERVER = sys.argv.pop(1)
        if op == '-p':
            PORT   = sys.argv.pop(1)
        if op not in ops:
            usage()

    # Test server and port are still set
    if not SERVER or not PORT:
        usage()
    
    # Run pwnwiki server
    pwnwiki(server=SERVER,port=PORT)
