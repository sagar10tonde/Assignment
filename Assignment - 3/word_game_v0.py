from tkinter import *
import random

list1=[]
buttons=[]

def okCheck():
    print("ok")

def Refresh(l1):
    print("Refresh")

def click(l,k):
    print("click",l)
    
def mainFun(list1):
    index=0
    for i in range(0,rows):
        for j in range(0,cols):
            b1=Button(window,text=list1[index],width=12,command=lambda k=index: click(list1[k],k))
            b1.grid(row=2+i,column=j)
            buttons.append(b1)
            index+=1

    ok=Button(window,text="OK",width=10,command=lambda: okCheck())
    ok.grid(row=i+3,column=0,padx=10,pady=20)

    Re=Button(window,text="REFRESH",width=10,command=lambda: Refresh(list1))
    Re.grid(row=i+3,column=1,padx=10,pady=20)

    QUIT=Button(window,text="QUIT",width=10,command=window.quit)
    QUIT.grid(row=i+3,column=2,padx=10,pady=20)

    window.mainloop()


if __name__ == "__main__":
    global window
    global rows,cols
    i =0
    string =""
    
    rows=3
    cols=3
    
    window=Tk()
    window.title("Word-Game")
   
    
    list1=[]
    while len(list1)<rows*cols:
        character=chr(random.randint(97,121))
        #if character not in list1:
        list1.append(character)

    print(list1)
    string=""
    i=0
    mainFun(list1)

   




