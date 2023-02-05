from tkinter import *
def set_value(formula):
    if formula == '':
        label['text'] = '0'
    else:
        label['text'] = str(eval(formula))
def logic(operator):
    if operator == 'C':
        set_value('')
    elif operator == 'DEL':
        set_value(label['text'][0:-1])
    elif operator == 'X^2':
        set_value(str((eval(label['text']))**2))
    elif operator == '=':
        set_value(label['text'])
    else:
        if label['text'] == '0':
            label['text'] = ''
        label['text'] = label['text']+operator
list = ['C','DEL','*','=','1','2','3','/','4','5','6','+','7','8','9','-','(','0',')','X^2']
root = Tk()
root['bg'] = 'black'
root.title('Сложный калькулятор')
root.geometry('485x550')
root.resizable(False,False)
label = Label(text='0', font=('Consolas',21,'bold'), bg='black', foreground = 'white')
label.place(x=10,y=50)
x=10
y=140
for lis in list:
    com = lambda x=lis: logic(x)
    Button(text=lis, bg = 'white', font=('Consolas',15), command = com).place(x=x,y=y,width=115,height=79)
    x+=117
    if x>400:
        x=10
        y+=81
root.mainloop()