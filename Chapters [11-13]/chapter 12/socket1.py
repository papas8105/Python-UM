'''
 Exploring the HyperText Transport Protocol

You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

    http://www.pythonlearn.com/code/intro-short.txt

'''
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print data

mysock.close()

'''
HTTP/1.1 200 OK
Date: Wed, 29 Jun 2016 11:19:39 GMT
Server: Apache
Last-Modified: Mon, 12 Oct 2015 14:55:29 GMT
ETag: "20f7401b-1d3-521e9853a392b"
Accept-Ranges: bytes
Content-Length: 467
Cache-Control: max-age=604800, public
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: origin, x-requested-with, content-type
Access-Control-Allow-Methods: GET
Connection: close
Content-Type: text/plain
'''
