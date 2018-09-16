from tkinter import *

class Example:
    def __init__(self, master):
        self.cancel_id = None
        
        self.startButton = Button(master,text='Start', command=self.start)
        self.startButton.grid(row=0, column=0)

        self.stopButton = Button(master, text='Stop', command=self.stop)
        self.stopButton.grid(row=0, column=1)

        self.textBox = Text(master, bd=2)
        self.textBox.grid(row=1, columnspan=2)

    def start(self):
        if(self.cancel_id==None):
            self.count = 0
            #self.cancel_id = None
            self.counter()

    def counter(self):
        self.textBox.delete("1.0", END)
        if (self.count < 10):
            self.count += 1
            self.textBox.insert(END, str(self.count)+'\n\n')
            self.cancel_id = self.textBox.after(1000, self.counter)

    def stop(self):
        if self.cancel_id is not None:
            self.textBox.after_cancel(self.cancel_id)
            self.cancel_id = None

root=Tk()
Example(root)
root.mainloop()