from tkinter import *
from tkinter import messagebox
from subprocess import call
import webbrowser

root = Tk()
root.title('Login Gym Management System')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

def signin(t:Tk):
    username=user.get()
    password=code.get()
    
    if username =='admin' and password =='123456':
        messagebox.showinfo("","Logged in as Administrator")
        t.destroy()
        call(["python","main.py"]) # call file tesst
    else:
        messagebox.showinfo("","Invalid username or password")
def on_facebook():
    webbrowser.open_new("https://www.facebook.com/groups/1775647979239578")
def on_youtube():
    webbrowser.open_new("https://www.youtube.com/watch?v=lTswlJjBBi0")
def on_twitter():
    webbrowser.open_new("https://twitter.com/PowerhouseGym")

#open image file
img = PhotoImage(file='./assets/1.png')
Label(root,image=img,bg='white').place(x=50,y=50)

img1 = PhotoImage(file='./assets/user.png')
Label(root,image=img1,bg='white').place(x=466,y=155)

img2 = PhotoImage(file='./assets/password.png')
Label(root,image=img2,bg='white').place(x=466,y=215)

img3 = PhotoImage(file='./assets/Facebook.png')
img4 = PhotoImage(file='./assets/youtube.png')
img5 = PhotoImage(file='./assets/twitter.png')

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=490,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light', 23,'bold'))
heading.place(x=100,y=5)

#----------------------------------------------------------------
textphilo = Label(frame, text='If no one loves you, then love yourself',fg='#081018',bg='white',font=('Microsoft YaHei UI Light', 13,'italic'))
textphilo.place(x=30,y=310)

#create a button to click 
facebook_button = Button(root,image=img3,command=on_facebook,borderwidth=0)
facebook_button.place(x=700,y=420)

youtube_button = Button(root,image=img4,command=on_youtube,borderwidth=0)
youtube_button.place(x=800,y=425)

twitter_button = Button(root,image=img5,command=on_youtube,borderwidth=0)
twitter_button.place(x=750,y=420)

####----------------------------------------------------------------
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=85)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
####----------------------------------------------------------------
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11),show='*')
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
###----------------------------------------------------------------

Button(frame,width=39,pady=7,text='Sign in', bg='#57a1f8',fg='white',border=0,command= lambda: signin(root)).place(x=35,y=204)

root.mainloop()