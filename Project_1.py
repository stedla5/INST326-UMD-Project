from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import json
 
root = Tk()
root.geometry("1200x800")
root.title(" Python Practice Quiz")
with open('quiz.json') as f:
    obj = json.load(f)
q = (obj['question'])
options = (obj['choices'])
a = (obj['answer'])
 
class Quiz:
    def __init__(self):
        self.q_num = 0
        self.ques = self.question(self.q_num)
        self.opt_selected = IntVar()
        self.opts = self.radiobutns()
        self.display_options(self.q_num)
        self.buttons()
        self.correct = 0

    def question(self, q_num):
        t = Label(root, text="INST 326 Quiz OOP Programming", width=70, bg="purple", fg="white", font=("times", 22, "bold"))
        t.place(x=0, y=2)
        q_num = Label(root, text=q[q_num], width=70, font=("arial", 16, "bold"), anchor="w")
        q_num.place(x=70, y=120)
        return q_num
 
    def radiobutns(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            butn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
            b.append(butn)
            butn.place(x=100, y=yp)
            val += 1
            yp += 60
        return b
 
    def display_options(self, q_num):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[q_num]
        for op in options[q_num]:
              self.opts[val]['text'] = op
              val += 1
 
    def buttons(self):
        nbutton = Button(root, text="Next",command=self.nextbutn, width=10,bg="Black",fg="white",font=("times",16,"bold"))
        nbutton.place(x=300,y=380)
        quitbutton = Button(root, text="Exit", command=root.destroy,width=10,bg="red",fg="white", font=("times",16,"bold"))
        quitbutton.place(x=500,y=380)
 
    def check_ans(self, q_num):
        if self.opt_selected.get() == a[q_num]:
             return True
        
    def nextbutn(self):
        if self.check_ans(self.q_num):
            self.correct += 1
        self.q_num += 1
        if self.q_num == len(q):
            self.display_result()
        else:
            self.display_options(self.q_num)       
        
 
    def display_result(self):
        score = int(self.correct / len(q) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(q) - self.correct
        correct = "correct answers: " + str(self.correct)
        wrong = "wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))

quiz=Quiz()
root.mainloop()
 
 
