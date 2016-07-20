#get a picture from the web and save it in a file
import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com' , 80))
mysock.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')
count = 0 ; picture = '';
while True:
	data = mysock.recv(5120)
	if len(data) < 1:
		break
	count = count + len(data)
	print len(data) , count
	picture += data
mysock.close()
pos = picture.find("\r\n\r\n");
print 'Header length', pos
print picture[:pos]
picture = picture[pos+4:]
fhand = open("stuff.jpg","w")
fhand.write(picture);
fhand.close();
'''
2828 2828
1414 4242
1414 5656
1414 7070
1414 8484
2828 11312
1414 12726
1414 14140
1414 15554
1414 16968
1414 18382
1414 19796
5120 24916
3364 28280
1414 29694
2828 32522
1414 33936
2828 36764
1414 38178
2828 41006
5120 46126
1950 48076
1414 49490
2828 52318
2828 55146
2828 57974
1414 59388
1414 60802
1414 62216
1414 63630
2828 66458
2828 69286
1017 70303
Header length 242
HTTP/1.1 200 OK
Date: Wed, 06 Jul 2016 11:57:07 GMT
Server: Apache
Last-Modified: Fri, 04 Dec 2015 19:05:04 GMT
ETag: "b294001f-111a9-526172f5b7cc9"
Accept-Ranges: bytes
Content-Length: 70057
Connection: close
Content-Type: image/jpeg

'''
