import tkinter
import threading
import time
class MyGUI:
    def __init__(self,root):
        self.root=root
        self.root.geometry('200x200')
        self.b1=tkinter.Button(text="Start",command=self.mythread)
        self.b1.pack()
        self.b2 = tkinter.Button(text="Stop",command=self.stopnumber)
        self.b2.pack()
    def mythread(self):
        t1=threading.Thread(target=self.shownos)
        t1.start()
    def shownos(self):
        self.flag=True
        for i in range(1,16):
            if self.flag==False:
                break
            print(i)
            time.sleep(1)
    def stopnumber(self):
        self.flag=False




root=tkinter.Tk()
obj=MyGUI(root)
root.mainloop()