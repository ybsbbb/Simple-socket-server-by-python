import socket
import threading

class client(threading.Thread):
    def __init__(self,conn,addr,cnt):
        threading.Thread.__init__(self)
        self.conn=conn
        self.addr=addr
        self.cnt=cnt
        self.thread_stop=False
    def run(self):
        print('Client',self.cnt,':',self.addr,'has connected...')
        while True:
            self.data = self.conn.recv(1024).decode()
            if self.data=='bye':
                break
            else:
                print('Client',self.cnt,' send:',self.data)
                self.conn.sendall(self.data_reverse())
        conn.close()
        self.stop()
    def stop(self):
        print('Client',self.cnt,'exits...')
        self.thread_stop= True
    def data_reverse(self):
        return self.data[::-1].encode()
if __name__=='__main__':
    HOST=''
    PORT=8080
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen()
    cnt=0
    while True:
        conn,addr=s.accept()
        cnt+=1
        c=client(conn,addr,cnt)
        c.start()
    s.close()
