#!/usr/bin/env python

import socket
import re
import sys

def check_webserver(address, port, resource):
    #create http request string
    if not resource.strtswith('/'):
        resource = '/' + resource
    request_string = "GET %s HTTP/1.1\r\nHost: %s\r\n\r\n" % (resource, address)

    print 'HTTP request:'
    print '|||%s|||' % request_string

    #create tcp socket
    s = socket.socket
    print "Attemting to connect to %s on port %s" % (address, port)
    try:
        s.connect((address, port))
        print "Connecting to %s on port %s" % (address, port)
        s.send(request_string)
        #need first 100 byte
        rsp = s.recv(100)
        print "Recived 100 bytes on HTTP response"
        print "|||%s|||" % rsp
    except socket.error, e:
                print "Connecting to %s on port %s failed %s" % (address, port, e)
                return False
    finally:
        print "Closing connection"
        s.close()
    lines = rsp.splitlines()
    print "First line on HTTP response %s " % lines[0]
    try:
        version, stats, message = re.split(r'\s+', lines[0], 2)
        print  'Version: %s, Status: %s, Message: %s' % (version, stats,
                                                         message)
    except ValueError:
        print 'Failed to split status line'
        return False
    if stats in ['200', '301']:
        print 'Success - status was %s' % stats
        return True
    else:
        print "Status was %s " % stats
        return False

    if __name__ == '__main__':
        from optparse import OptionParser
        parser = OptionParser()
        parser.add_option(" a", "  address", dest="address", default='localhost',
                          help="ADDRESS to webserver", metavar='ADDRESS')
        parser.add_option(" p", "  port", dest="port", type="int", default=80,
                         help="PORT for webserver", metavar="PORT")
        parser.add_option(" r", "  resource", dest="resource",
                         default='index.html',
                         help="RESOURCE to check", metavar="RESOURCE")
        (options, args) = parser.parse_args()
        print "options %s, args %s " % (options,args)
        check = check_webserver(options.address, options.port, options.resource)
        print "check_webserver returned %s" % check
        sys.exit(not check)
        




