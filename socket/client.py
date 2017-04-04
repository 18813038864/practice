
import socket
import time
import threading
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('localhost', 5050))
sock.send(b'1')
print(sock.recv(1024).decode())
nickName = ''
nickName = raw_input('input your nickname: ')
sock.send(nickName.encode())


def sendThreadFunc():
    while True:
        try:
            myword = raw_input ()
            sock.send(myword.encode())
            # print(sock.recv(1024).decode())
        except socket.error, arg:
            (errno, err_msg) = arg
            print "Connect server failed: %s, errno=%d" % (err_msg, errno)


def recvThreadFunc():
    while True:
        try:
            otherword = sock.recv(1024)
            if otherword:
                print(otherword.decode())
            else:
                pass
        except socket.error, arg:
            (errno, err_msg) = arg
            print "Connect server failed: %s, errno=%d" % (err_msg, errno)


th1 = threading.Thread(target=sendThreadFunc)
th2 = threading.Thread(target=recvThreadFunc)
threads = [th1, th2]

for t in threads:
    t.setDaemon(True)
    t.start()
t.join()