from tkinter import *
import random

list1=[]
buttons=[]

class wordGame:
    def __init__(self, master):
        self.window = master
        global rows,cols
        i =0
        string =""
        
        rows=3
        cols=3
    
        window.title("Word-Game")
   
        
        list1=[]
        while len(list1)<rows*cols:
            character=chr(random.randint(97,121))
    
            list1.append(character)

        print(list1)
        string=""
        i=0
        self.mainFun(list1)

        

        
    def okCheck(self):
        print("ok")
        
    def Refresh(self,l1):
        print("Refresh")

    def click(self,l,k):
        print("click",l)
    
    def mainFun(self,list1):
        index=0
        for i in range(0,rows):
            for j in range(0,cols):
                b1=Button(window,text=list1[index],width=12,command=lambda k=index: self.click(list1[k],k))
                b1.grid(row=2+i,column=j)
                buttons.append(b1)
                index+=1

        ok=Button(window,text="OK",width=10,command=lambda: self.okCheck())
        ok.grid(row=i+3,column=0,padx=10,pady=20)

        Re=Button(window,text="REFRESH",width=10,command=lambda: self.Refresh(list1))
        Re.grid(row=i+3,column=1,padx=10,pady=20)

        QUIT=Button(window,text="QUIT",width=10,command=window.quit)
        QUIT.grid(row=i+3,column=2,padx=10,pady=20)

        window.mainloop()
        

if __name__ == "__main__":
    window=Tk()
    app=wordGame((window))

