from tkinter import *
from email.message import EmailMessage
import smtplib

screen = Tk()

screen.resizable( width = False, height = False)
screen.geometry('400x300')
screen.title('IT-NOX')
   
Tname = Label(text = 'ФИО:', font = 'Consolas')
name = Entry(screen, font = 'Consolas')

Tphone = Label(text = 'Телефон:', font = 'Consolas')
phone = Entry(screen, font = 'Consolas')

Torg = Label(text = 'Организация:', font = 'Consolas')
org = Entry(screen, font = 'Consolas')

Tmail = Label(text = 'Почта:', font = 'Consolas')
mail = Entry(screen, font = 'Consolas')

Ttrouble = Label(text = 'Опишите проблему:', font = 'Consolas')
trouble = Entry(screen, font = 'Consolas')
trouble = Text(width = 23, height = 7)

Tname.grid(row = 0, column = 0, sticky = W)
name.grid(row = 0, column = 1)

Tphone.grid(row = 1, column = 0, sticky = W)
phone.grid(row = 1, column = 1)

Torg.grid(row = 2, column = 0, sticky = W)
org.grid(row = 2, column = 1)

Tmail.grid(row = 3, column = 0, sticky = W)
mail.grid(row = 3, column = 1)

Ttrouble.grid(row = 4, column = 0, sticky = W)
trouble.grid(row = 4, column = 1)

result = Label(text = '', font = 'Consolas')
result.grid(row = 5, column = 0, sticky = W)

def send_mail(event):
    N = name.get()
    P = phone.get()
    O = org.get()
    M = mail.get()
    T = trouble.get("1.0",'end-1c')
     
    msg = f"{N}, \n{P}, \n{O}, \n{M}, \n{T}"
    
    server = smtplib.SMTP('smtp.mail.ru')
    server.starttls()
    server.login('aaa@aaa.aaa', 'password')
    server.sendmail('from', 'to', msg.encode('cp-1251'))
    result['text'] = 'Заявка успешно \n отправлена.'
    server.quit()
        
enter = Button(text = 'Отправить', font = 'Consolas')
enter.grid(row = 5, column = 1)
result.grid(row = 6, column = 1, sticky = W)
enter.bind('<Button-1>', send_mail)

screen.mainloop()

