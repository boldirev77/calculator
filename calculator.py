"""
    File name: calculator.py
    Python Version: 3.3
"""

from tkinter import *


def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="gray")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')

        display = StringVar()
        Entry(self, relief=SUNKEN, textvariable=display, justify='right',\
              bd=5, bg="light green").pack(side=TOP, expand=YES, fill=BOTH)

        for clearBut in (["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar, lambda storeObj=display, q=ichar: storeObj.set(''))

        for numBut in ("789/", "456*", "123-", "0.+"):
            functionNum = iCalc(self, TOP)
            for iEquals in numBut:
                button(functionNum, LEFT, iEquals, \
                       lambda storeObj=display, q=iEquals: storeObj.set(storeObj.get() + q))

        equalsButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(equalsButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', \
                                lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquals = button(equalsButton, LEFT,iEquals,\
                                    lambda storeObj=display, s=' %s '%iEquals: storeObj.set(storeObj.get()+s))
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERR")


if __name__ == '__main__':
    app().mainloop()