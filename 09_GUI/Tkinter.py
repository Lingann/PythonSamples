# python支持多种图像界面的第三方库，包括
# * Tk (python 内置)
# * wxWidgets
# * Qt
# * GTK
from  tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.helloLable = Label(self, text='Hello World')
        self.helloLable.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()


app = Application()
# 设置窗口标题
app.master.title('Hello World')
# 主消息循环
app.mainloop()
