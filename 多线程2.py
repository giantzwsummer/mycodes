import threading
 
class MyThread(threading.Thread):
    def __init__(self,func,name,num):
        super(MyThread,self).__init__()
        self.name=name
        self.num=num
        self.func=func
 
    def run(self):
        self.func(self.num)
def thread_fun(num):
    for n in range(0, int(num)):
        print(" I come from %s, num: %s" %( threading.currentThread().getName(), n))
      
   
if __name__ == "__main__":
    thread_list = list()
    for i in range(0, 3):
        thread_name='thread_%s'%i
        t = MyThread(thread_fun,name=thread_name,num=20)
        thread_list.append(t)
        t.start()
    for thread in thread_list:
        thread.join()
    
    print('have fun')
