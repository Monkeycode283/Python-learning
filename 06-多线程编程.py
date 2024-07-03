# threading模块  创建一个线程然后启动就可以
import time
import threading
def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)



if __name__=='__main__':
    # 创建一个唱歌的线程
    sing_thread=threading.Thread(target=sing)
    # 创建一个跳舞的线程
    dance_thread=threading.Thread(target=dance)
    sing_thread.start()
    dance_thread.start()










