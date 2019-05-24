from tkinter import *
import math
import datetime
expression = "" 


class logs(object):
    def __init__(self):
        self.log = []
        self.now = datetime.datetime.now()

    def logFile(self):
        self.fp = open('log','w')
        self.fp.write(str(self.now) + "\n")
        for i in self.log:
            self.fp.write(i + '\n')
            #self.fp.writa(str(i))
        print(self.log)

        self.fp.close()
        
        roop = Tk()
        roop.title("Cal Log")
        roop.geometry('200x100')

        labelframe = LabelFrame(roop, text="Log File")
        labelframe.pack(fill="both", expand="yes")
        
    
        for i in range(len(self.log)):
            left = Label(labelframe, text=self.log[i])
            left.pack()
        
        roop.mainloop()
    


class controller(logs):
    def __init__(self):
        logs.__init__(self)
        
    def press(self,num,flag, op, ex): 
        global expression
        
        if flag == 0:
            expression = expression + str(num) 
            equation.set(expression) 
        if flag == 1:
            expression = str(num)
            x  = op + "("+ ex + ") = " + expression[:7]
            equation.set(x)
            self.log.append(x)

    def equalpress(self):        
        global expression
        
        try:  
            total = str(eval(expression))
            self.log.append(expression + "=" + total) 
            equation.set(total) 
            expression = "" 

        except: 
            equation.set(" error ") 
            expression = "" 

    def clear(self): 
        global expression 
        expression = "" 
        equation.set("") 


class Calculator(controller):
    def __init__(self):
        controller.__init__(self)
        self.fp = open('log','w')
        self.fp.close() 

    def createButton(self,master,h=1,w=2,row=0,col=0,rows=1, cols= 1,name='None', cmd = 'clear'):
        botton =Button(master,height =h,width=w, padx=10, pady=5,text=name,command=cmd)
        botton.grid(row=row,column=col,padx=10,columnspan = cols,rowspan=cols, pady = 5)
        return botton

    
    
if __name__ == "__main__":

    cal = Calculator()
    root = Tk()

    master = Frame(root)
    master.grid()
    root.title("Calculator")

    equation = StringVar() 
    expression_field = Entry(master, justify=RIGHT,width=30,font="Times 16 bold",textvariable=equation)
    expression_field.grid(row = 0, column = 0,columnspan = 8,padx=30, pady = 10) 
    equation.set('') 

    sin = cal.createButton(master,row=1,col=0,name="sin", cmd=lambda: cal.press(math.sin(float(expression)),1,"sin",expression))
    cos = cal.createButton(master,row=2,col=0,name="cos", cmd=lambda: cal.press(math.cos(float(expression)),1,"cos",expression))
    tan = cal.createButton(master,row=3,col=0,name="tan", cmd=lambda: cal.press(math.tan(float(expression)),1,"tan",expression))
    logfile = cal.createButton(master,row=4,col=0,name="LF", cmd= cal.logFile)
    
    pi  = cal.createButton(master,row=1,col=1,name="pi", cmd=lambda: cal.press(math.pi,0,"pi",expression))
    log = cal.createButton(master,row=2,col=1,name="log", cmd=lambda: cal.press(math.log10(float(expression)),1,"log",expression))
    e   = cal.createButton(master,row=3,col=1,name="e", cmd=lambda: cal.press(math.e,0,"e",expression))
    sqr = cal.createButton(master,row=4,col=1,name="sqr", cmd=lambda: cal.press(math.sqrt(float(expression)),1,"sqrt",expression))
    
    sev = cal.createButton(master,row=1,col=2,name="7",cmd=lambda: cal.press(7,0,"7",expression))
    fou = cal.createButton(master,row=2,col=2,name="4",cmd=lambda: cal.press(4,0,"4",expression))
    one = cal.createButton(master,row=3,col=2,name="1",cmd=lambda: cal.press(1,0,"1",expression))
    abs = cal.createButton(master,row=4,col=2,name="abs", cmd=lambda: cal.press(math.fabs(float(expression)),1,"abs",expression))
    
    egt = cal.createButton(master,row=1,col=3,name="8",cmd=lambda: cal.press(8,0,"8",expression))
    fiv = cal.createButton(master,row=2,col=3,name="5",cmd=lambda: cal.press(5,0,"5",expression))
    two = cal.createButton(master,row=3,col=3,name="2",cmd=lambda: cal.press(2,0,"2",expression))
    zer = cal.createButton(master,row=4,col=3,name="0",cmd=lambda: cal.press(0,0,"0",expression))
        
    nin = cal.createButton(master,row=1,col=4,name="9",cmd=lambda: cal.press(9,0,"9",expression))
    six = cal.createButton(master,row=2,col=4,name="6",cmd=lambda: cal.press(6,0,"6",expression))
    tre = cal.createButton(master,row=3,col=4,name="3",cmd=lambda: cal.press(3,0,"3",expression))
    fac = cal.createButton(master,row=4,col=4,name="x!",cmd=lambda: cal.press(math.factorial(float(expression)),1,"fact",expression))
    
    add = cal.createButton(master,row=1,col=5,name="+",cmd=lambda: cal.press('+',0,"+",expression))
    sub = cal.createButton(master,row=2,col=5,name="-",cmd=lambda: cal.press('-',0,"-",expression))
    div = cal.createButton(master,row=3,col=5,name="/",cmd=lambda: cal.press('/',0,"/",expression))
    mul = cal.createButton(master,row=4,col=5,name="*",cmd=lambda: cal.press('*',0,"*",expression))
    
    ac  = cal.createButton(master,row=1,col=6,name="AC",cmd= cal.clear)
    per = cal.createButton(master,row=2,col=6,name="%", cmd=lambda: cal.press('%',0,"%",expression))
    eq  = cal.createButton(master,row=3,col=6,h=4,cols=2,name="=",cmd=lambda: cal.equalpress())
    
    root.mainloop()
