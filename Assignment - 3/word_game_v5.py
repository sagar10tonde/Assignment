from tkinter import *
from dictionary import *
import random

list1=[]
buttons=[]

def click(ele,k):
    global i
    global string
    global select
    
    print ("Click",ele,k)
    string+=ele
    e1.insert(i,ele)
    i+=1
    buttons[k].config(state="disabled")

  

def Refresh(list1):
    global i
    global string
    list1=[]

    """
    while len(list1)<rows*cols:
        character=chr(random.randint(97,121))
        list1.append(character)
    """
    list1=['b','a','g','a','i','o','d','d','o']
    
    string=""
    e1.delete(0, END)
    i=0
    e2.delete(0, END)
    print (list1)
    main(list1)

def getResult():
    global res
    res+=10
    
    string=""
    e1.delete(0, END)
    i=0
    e2.delete(0, END)
  
    e3=Label(window,width=10,text= res)
    e3.config(font=('times', 14, 'bold'))
    e3.grid(row=1,column=2)
   
    
def okCheck(list1):
    global string
    listofWords=dict[string[0]]
    print(string)
    
    if string in listofWords:
        getResult()
        e2.insert(0,"Valid")
    else:
        e2.delete(0, END)
        e2.insert(0,"InValid")
    string = ""
    main(list1)



def main(list1):
    index=0
    for i in range(0,rows):
        for j in range(0,cols):
            b1=Button(window,text=list1[index],width=12,command=lambda k=index: click(list1[k],k))
            b1.grid(row=2+i,column=j)
            buttons.append(b1)
            index+=1
        
    ok=Button(window,text="OK",width=10,command=lambda: okCheck(list1))
    ok.grid(row=i+3,column=0,padx=10,pady=20)

    Re=Button(window,text="REFRESH",width=10,command=lambda: Refresh(list1))
    Re.grid(row=i+3,column=1,padx=10,pady=20)

    QUIT=Button(window,text="QUIT",width=10,command=window.quit)
    QUIT.grid(row=i+3,column=2,padx=10,pady=20)

    window.mainloop()


if __name__ == "__main__":

    rows=3
    cols=3
    res=0
    i=0
    string=""
    
    window=Tk()
    window.title("Word-Game")
     
    l1=Label(window,text="Enter String")
    l1.grid(row=0,column=0)
    
    l2=Label(window,text="Reuslt")
    l2.grid(row=1,column=0)
    
    l3=Label(window,text="Score")
    l3.config(font=('times', 14, 'bold underline'))
    l3.grid(row=0,column=2)
    
    e1=Entry(window)
    e1.grid(row=0,column=1)
    
    e2=Entry(window)
    e2.grid(row=1,column=1,padx=10,pady=10)

    e3=Label(window,width=10,text= res)
    e3.config(font=('times', 14, 'bold'))
    e3.grid(row=1,column=2)
   

    
    Refresh(list1)
