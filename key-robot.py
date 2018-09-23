## You can find the executable file in dist/key-robot.exe ##

from pynput.keyboard import Key, Controller
from time import sleep
from tkinter import *
from tkinter import ttk
#import PIL.Image
#import PIL.ImageTk

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import codecs

class robo:
    def __init__(self, window):
        # The variables
        self.keyboard = Controller()
        self.keyOne = 1
        self.keyTwo = 0
        
        self.waitTime = 5
        self.cancel_id = None
        self.text="""
        Робо-Съпорт е клавиатурен робот.
        Въведи 'Време' за общото време на работа, 
        'Интервал' за интервал между командите
        и 'Команда' за желаната команда.
        Натисни 'Start', когато си готов
        и отвори желаният прозорец, в който
        ще се изпълняват командите.
        !Увери се, че пишеш в провижънинга!"""
        
        ## Gui: ##
        # The global frame
        self.mainframe = ttk.Frame(window, padding="5 5 5 5")
        self.mainframe.grid(row=0, column=0, sticky=(E, W, N, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(1, weight=1)
        #self.mainframe.rowconfigure(1, weight=1)

        # The image frame
        
        ## The image frame is removed because of problem with the executable file.
        
        #self.frameImage = ttk.LabelFrame(self.mainframe, text="Робо- Съпорт", padding="5 5 5 5")
        #self.frameImage.grid(row=0, column=0, sticky=(E, W, N, S))
        #self.frameImage.columnconfigure(0, weight=1)
        #self.frameImage.rowconfigure(0, weight=1)
        
        # The instructions frame
        self.frameInstructions = ttk.LabelFrame(self.mainframe, text="Инструкции:", padding="5 5 5 5")
        self.frameInstructions.grid(row=0, column=0, sticky=(E, W, N, S))
        #self.frameInstructions.columnconfigure(0, weight=1)
        #self.frameInstructions.rowconfigure(0, weight=1)

        #self.robot = ttk.Label(self.frameImage, text=self.text, image=None)
        #self.robot.grid(row=0, column=0, padx=5, sticky=(E, W, S, N))
        
        self.robot2 = ttk.Label(self.frameInstructions, text=self.text, image=None)
        self.robot2.grid(row=0, column=0, padx=5, sticky=(E, W, S, N))

        # The settings frame
        self.framesettings = ttk.LabelFrame(self.mainframe, text="Настройка:", padding="5 5 5 5")
        self.framesettings.grid(row=0, column=1, sticky=(E, W, N, S))
        self.framesettings.columnconfigure(0, weight=1)
        self.framesettings.rowconfigure(0, weight=1)
        self.framesettings.rowconfigure(1, weight=1)
        self.framesettings.rowconfigure(2, weight=1)
        self.framesettings.rowconfigure(3, weight=1)
        self.framesettings.rowconfigure(4, weight=1)

        self._allTimeFrame = ttk.LabelFrame(self.framesettings, text="Време:(в минути)", padding="5 5 5 5")
        self._allTimeFrame.grid(row=0, column=0, sticky=(E, W))
        self._allTimeFrame.columnconfigure(0, weight=1)
        self._allTimeFrame.rowconfigure(0, weight=1)

        
        self.allTime = StringVar()
        self._allTime = ttk.Entry(self._allTimeFrame, textvariable=
        self.allTime)
        self._allTime.grid(row=0, column=0, sticky=(E, W))

        self._betweenTimeFrame = ttk.LabelFrame(self.framesettings, text="Интервал:(в секунди)", padding="5 5 5 5")
        self._betweenTimeFrame.grid(row=1, column=0, sticky=(E, W))
        self._betweenTimeFrame.columnconfigure(0, weight=1)
        self._betweenTimeFrame.rowconfigure(0, weight=1)

        self.betweenTime = StringVar()
        self._betweenTime = ttk.Entry(self._betweenTimeFrame, textvariable=self.betweenTime)
        self._betweenTime.grid(row=0, column=0, sticky=(E, W))
        
        self._commandFrame = ttk.LabelFrame(self.framesettings, text="Команда:", padding="5 5 5 5")
        self._commandFrame.grid(row=2, column=0, sticky=(E, W))
        self._commandFrame.columnconfigure(0, weight=1)
        self._commandFrame.rowconfigure(0, weight=1)

        
        self.command = StringVar()
        self._command = ttk.Entry(self._commandFrame, textvariable=self.command)
        self._command.grid(row=0, column=0, sticky=(E, W))

        self.startButton = ttk.Button(self.framesettings, text="Start", command=self.start, padding="5 5 5 5")
        self.startButton.grid(row=3, column=0, sticky=(E, W))
        self.stopButton = ttk.Button(self.framesettings, text="Stop", command=self.stop, padding="5 5 5 5")
        self.stopButton.grid(row=4, column=0, sticky=(E, W))
        
        #roboImage = self.create_img_object("robot.jpg")
        #self.set_img(roboImage)

    ## Logic: ##
    
    def start(self):
        if(self.cancel_id==None):
            self.iterator = 0
            self.support()

    def support(self):
        if(self.iterator<int(self.allTime.get())/int(self.betweenTime.get())*60):
            if(self.command.get()!=""):
                self.keyboard.type(self.command.get())
                #print(self.command.get())
            else:
                pass

            if(self.keyOne!=0):
                self.keyboard.press(Key.enter)
                self.keyboard.release(Key.enter)
            else:
                pass

            if(self.keyTwo!=0):
                self.keyboard.press(Key.up)
                self.keyboard.release(Key.up)
            else:
                pass
            sleep(int(self.betweenTime.get()))
            self.iterator += 1
            self.cancel_id = self.stopButton.after(1000, self.support)
            

    def stop(self):
        if self.cancel_id is not None:
            self.stopButton.after_cancel(self.cancel_id)
            self.cancel_id = None


    #def create_img_object(self, arg):
        #self.arg = arg
        #self.photo = PIL.Image.open(self.arg)
        #self.photo = self.photo.resize((150,200), PIL.Image.ANTIALIAS)
        #self.photo = PIL.ImageTk.PhotoImage(self.photo)
        #return self.photo


    #def set_img(self, arg):
        #self.arg = arg
        #self.robot.configure(image=self.arg)
        #self._img_name.set(self.arg)

        
#Graphical interface
# The global window
def main():
    _root = Tk()
    _root.title("Робо-Съпорт, v1.0")
    _root.geometry("720x480")
    _root.columnconfigure(0, weight=1)
    _root.rowconfigure(0, weight=1)
    robo(_root)
    _root.mainloop()


if __name__ == '__main__':
    main() 