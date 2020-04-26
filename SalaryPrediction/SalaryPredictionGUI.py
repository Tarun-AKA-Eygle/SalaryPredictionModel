import tkinter as tk
from PIL import ImageTk,Image
from SalaryPredictionModel import *

insert = 0

class g(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.title("SalaryPrediction")
        self.iconbitmap('D:\Programswin\Ostl project\Proycontec-Robots-Robot-documents.ico')
        
        container = tk.Frame(self)
        container.pack(side = 'top',fill='both',expand=True)
        

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames ={}

        for f in (Startpage,Pageone,Pagetwo):
            frame = f(container,self)
            self.frames[f] = frame

            frame.grid(row=0,column=0,sticky='nsew')
        self.show_frame(Startpage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
        

class Startpage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        introduction='You work in the H.R. department of your company.\n While interviewing a person, you came to know that this salary of previous job was 16k.\nYou decided to fact check his clames.\nYou called his ex-company but due to some complicatiothey could only give you their dataset of one year.\nYour goal is to predict what his salary of previous job was....(Press Im in to proceed)'
        label = tk.Label(self,text='Welcome! Mr.Homes')
        labelquestion = tk.Label(self,text=introduction)
        
        iminbutton = tk.Button(self,text="I'm in",command=lambda: controller.show_frame(Pageone))
       
        label.grid(row=0,column=1)
        labelquestion.grid(row=1,column=1)
        iminbutton.grid(row=2,column=1)
        
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(1,weight=1)

class Pageone(tk.Frame):
    
      
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        label = tk.Label(self,text='what is the level?')
        goback = tk.Button(self,text='go back',command=lambda: controller.show_frame(Startpage))
        view = tk.Button(self,text='view dataset',command=self.showdata)
        insert = tk.Entry(self,width=15)
        submit = tk.Button(self,text='Submit',command=lambda: self.check(insert.get(),controller))
        insert.insert(0,"Enter the level")
        
        
        label.grid(row=0,column=1)
        view.grid(row=1,column=1)
        insert.grid(row=2,column=1)
        goback.grid(row=3,column=1)
        submit.grid(row=4,column=1)

        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(1,weight=1)

        
      
    def check(self,entry,controller):
        global insert
        try:
            insert = float(entry)
            controller.show_frame(Pagetwo)
             
        except:
            tk.messagebox.showinfo("Error","INPUT MUST BE interger or float")
                

    def showdata(self):
        root = tk.Tk()
        root.title("SalaryPrediction")
        root.iconbitmap('D:\Programswin\Ostl project\Proycontec-Robots-Robot-documents.ico')
        
        label = tk.Label(root,text=showdataset())
        label.pack()
        root.mainloop()
        

class Pagetwo(tk.Frame):
    def __init__(self,parent,controller):

       
        
        tk.Frame.__init__(self,parent)
        backbutton = tk.Button(self,text='go back',command=lambda: controller.show_frame(Pageone))
        Polybutton = tk.Button(self,text='Polynomial Linear Regression',command=self.showpolyreg)
        Prediction = tk.Button(self,text='Prediction',command=self.prediction)
        Linearbutton = tk.Button(self,text='Linear Regression',command=self.showlinearreg)
        


        backbutton.grid(row=0,column=1)
        Polybutton.grid(row=1,column=1)
        Linearbutton.grid(row=2,column=1)
        Prediction.grid(row=3,column=1)

        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(1,weight=1)



    def showlinearreg(self):
        Showliner()
    
    def showpolyreg(self):
        Showpoly()

    def prediction(self):
        global insert
        
        tk.messagebox.showinfo("Prediction","The Predicted Salary is "+str(PredictionModel([[insert]])))
        tk.messagebox.showinfo("Checkout","Checkout my github page for the source code https://github.com/Tarun-AKA-Eygle/SalaryPredictionModel")
        
        
        


if __name__ == '__main__':    

    value=g()
    value.mainloop()
    

    
