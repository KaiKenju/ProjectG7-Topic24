import tkinter as tk
from tkinter import *
from subprocess import call
import webbrowser

win = tk.Tk()
win.title("Gym Management System")
win.geometry('1000x600')
#============================================= D A S H B O A R D =====================================
#================= CONTACT HOVER ===========


# === END NEW CODE ====== #

# def labelbt12():
#     x  = Frame(win,text='12\nMonths', width=8,font=('Microsoft YaHei UI Light', 12,'bold'),activebackground='white',activeforeground='#fecc09',borderwidth=0)
#     x.place(x=35,y=430)
def mon12():
    Label(win,text='Duration: 12 Months', font=('Helvetica',14),fg='Black').place(x=400,y=390)
    Label(win,text='Total Cost:    500 USD', font=('Helvetica',14),fg='Black').place(x=400,y=430)
    Label(win,text='Cost/Month:    50 USD', font=('Helvetica',14),fg='Black').place(x=400,y=470)
    Label(win,text='Cost/Day:     1.5 USD', font=('Helvetica',14),fg='Black').place(x=400,y=510)

def mon6():
    Label(win,text='Duration:   6 Months', font=('Helvetica',14),fg='Black').place(x=400,y=390)
    Label(win,text='Total Cost:    350 USD', font=('Helvetica',14),fg='Black').place(x=400,y=430)
    Label(win,text='Cost/Month:    35 USD', font=('Helvetica',14),fg='Black').place(x=400,y=470)
    Label(win,text='Cost/Day:     1.2 USD', font=('Helvetica',14),fg='Black').place(x=400,y=510)

def mon3():
    Label(win,text='Duration:   3 Months', font=('Helvetica',14),fg='Black').place(x=400,y=390)
    Label(win,text='Total Cost:    150 USD', font=('Helvetica',14),fg='Black').place(x=400,y=430)
    Label(win,text='Cost/Month:    15 USD', font=('Helvetica',14),fg='Black').place(x=400,y=470)
    Label(win,text='Cost/Day:      0.9 USD', font=('Helvetica',14),fg='Black').place(x=400,y=510)
def mon1():
    Label(win,text='Duration:   1 Months', font=('Helvetica',14),fg='Black').place(x=400,y=390)
    Label(win,text='Total Cost:      60 USD', font=('Helvetica',14),fg='Black').place(x=400,y=430)
    Label(win,text='Cost/Month:      6 USD', font=('Helvetica',14),fg='Black').place(x=400,y=470)
    Label(win,text='Cost/Day:      0.5 USD', font=('Helvetica',14),fg='Black').place(x=400,y=510)
def mon18():
    Label(win,text='Duration:  18 Months', font=('Helvetica',14),fg='Black').place(x=400,y=390)
    Label(win,text='Total Cost:  1000 USD', font=('Helvetica',14),fg='Black').place(x=400,y=430)
    Label(win,text='Cost/Month:  100 USD', font=('Helvetica',14),fg='Black').place(x=400,y=470)
    Label(win,text='Cost/Day:      2.0 USD', font=('Helvetica',14),fg='Black').place(x=400,y=510)
def mon21():
    Label(win,text='Duration:  21 Months', font=('Helvetica',14),fg='Black').place(x=400,y=390)
    Label(win,text='Total Cost:  1300 USD', font=('Helvetica',14),fg='Black').place(x=400,y=430)
    Label(win,text='Cost/Month:  130 USD', font=('Helvetica',14),fg='Black').place(x=400,y=470)
    Label(win,text='Cost/Day:      2.5 USD', font=('Helvetica',14),fg='Black').place(x=400,y=510)
def year2():
    Label(win,text='Duration:  2 Years', font=('Helvetica',14),fg='Black').place(x=400,y=390)
    Label(win,text='Total Cost:  2000 USD', font=('Helvetica',14),fg='Black').place(x=400,y=430)
    Label(win,text='Cost/Month:  200 USD', font=('Helvetica',14),fg='Black').place(x=400,y=470)
    Label(win,text='Cost/Day:      2.8 USD', font=('Helvetica',14),fg='Black').place(x=400,y=510)
def year3():
    Label(win,text='Duration:  3 Years', font=('Helvetica',14),fg='Black').place(x=400,y=390)
    Label(win,text='Total Cost:  3000 USD', font=('Helvetica',14),fg='Black').place(x=400,y=430)
    Label(win,text='Cost/Month:  300 USD', font=('Helvetica',14),fg='Black').place(x=400,y=470)
    Label(win,text='Cost/Day:      3.4 USD', font=('Helvetica',14),fg='Black').place(x=400,y=510)
# === END NEW CODE ====== #
def on_enter_contact(e):
    contact_btn.config(bg='Black',fg='#fecc09')

def on_leave_contact(e):
    contact_btn.config(bg='black',fg='White')

#=================== KNOWLEDGE HOVER =============
#-----------know frame--------

def on_enter_know(e):
    global know_frame
    know_frame = tk.Frame(win,bg='White')
    know_frame.place(x=650,y=40,width=200,height=150)
    know_btn.config(bg='Black', fg='#fecc09')

    vlog_btn = Button(know_frame, 
        bg='#e1e1d0', 
        fg='White', 
        text='Vlog', 
        font=('Helvetica', 10, 'bold'), width=8,bd=0, 
        activebackground='#e1e1d0', 
        activeforeground='#fecc09', 
        relief=tk.FLAT)
    vlog_btn.grid(row=0, column=0, padx=10, pady=10)

    write_btn = Button(know_frame, 
        bg='#e1e1d0', 
        fg='White', 
        text='Write', 
        font=('Helvetica', 10, 'bold'), width=8,bd=0, 
        activebackground='#e1e1d0', 
        activeforeground='#fecc09', 
        relief=tk.FLAT)
    write_btn.grid(row=1, column=0, padx=10, pady=10)

    library_btn = Button(know_frame, 
        bg='#e1e1d0', 
        fg='White', 
        text='Library', 
        font=('Helvetica', 10, 'bold'), width=8,bd=0, 
        activebackground='#e1e1d0', 
        activeforeground='#fecc09', 
        relief=tk.FLAT)
    library_btn.grid(row=2, column=0, padx=10, pady=10)

def on_leave_know(e):
    if (e.widget == know_btn or e.widget == know_frame):
        know_btn.config(bg='black', fg='white')
        know_frame.bind("<Enter>", on_enter_know)
    know_frame.destroy()

#=================== SERVICE HOVER =============

def on_enter_service(e):
    service_btn.config(bg='Black',fg='#fecc09')

def on_leave_service(e):
    service_btn.config(bg='black',fg='White')

#=================== GYM HOVER =============

def on_enter_gym(e):
    gym_btn.config(bg='Black',fg='#fecc09')

def on_leave_gym(e):
    gym_btn.config(bg='black',fg='White')

#=================== RESULT HOVER =============

def on_enter_result(e):
    result_btn.config(bg='Black',fg='#fecc09')

def on_leave_result(e):
    result_btn.config(bg='black',fg='White')

#========================================================================================
def signupnow(t:Tk):
    t.destroy()
    call(["python", "loginas.py"])

def hiddenContact():
    bottom_frame.place_forget()
    bottom_canvas.place_forget()

def active_both_button():
    gym_btn1.invoke()
    gym_info()

#========================================================================================
#========================================================================================

top = tk.Frame(
    win,
    bg='Black'
)
top.place(width=1000,height=50)
win.resizable(0,0)
#bot = tk.LabelFrame(win,bg='white',width=1000,height=303).place(y=355)

#image on dashboard
img0= PhotoImage(file='./assets/1.png')
img0 = img0.subsample(8)
Label(top,image = img0,bd=0).place(x=0,y=0)

#create a space under dashboard
none_btn = tk.Button(
    top,
    bg='black',
    bd=0,
    activebackground='Black'

)
none_btn.pack(side='right',padx=20)

# ================= CONTACT BUTTON ================= 
def contact_info():
    global img,img_build,img_location,img_fb,img_yt,img_tw
    global bottom_frame,bottom_canvas
    mid = tk.Frame(win,bg='White')
    mid.place(y=50,width=1000,height=303)
    img = PhotoImage(file='./image/contact1.png')
    mid_canvas = Canvas(mid,width=1000,height=303,highlightthickness=0)
    mid_canvas.pack(fill=BOTH,expand=TRUE)

    #SET IMAGE CANVAS FOR MID
    mid_canvas.create_image(0,0,image = img, anchor='nw')

    #CREATE CONTACT TEXT FOR MID FRAME
    mid_canvas.create_text(500,90,text='CONTACT',font=('Montserrat',40,'bold'),fill='#fecc09')
    mid_canvas.create_line(420,130,570,130,width=3,fill='#fecc09')
    mid_canvas.create_text(480,170,text='For a free consultation and visit to the gym',font=('Arial',14),fill='White')
    mid_canvas.create_text(480,200,text='leave your phone number or contact us via hotline 1900.2208',font=('Arial',14),fill='White')

    #CREATE CONTACT TEXT FOR BOTTOM 
    
    bottom_frame = tk.Frame(win,bg='White')
    bottom_frame.place(y=353,width=1000,height=247)
    bottom_canvas = Canvas(bottom_frame,width=1000,height=247,highlightthickness=0)
    bottom_canvas.pack(fill=BOTH,expand=TRUE)
    
    #CONTACT INFORMATION

    bottom_canvas.create_text(105,25,text='HEAD OFFICE',font=('Montserrat',12,'bold'),fill='Black')
    bottom_canvas.create_line(50,7,115,7,width=4,fill='#fecc09')

    bottom_canvas.create_line(722,40,950,40,950,244,722,244,722,40,width=2,fill='Black')
    bottom_canvas.create_text(785,60,text='CONTACT',font=('Montserrat',12,'bold'),fill='Black')
    bottom_canvas.create_text(853,105,text='N01-T1 Khu Ngoại Giao Đoàn,\nBắc Từ Liêm, Hà Nội ',font=('Helvetica',10,'bold'),fill='Black')
    bottom_canvas.create_text(800,135,text='0912 888 111 ',font=('Helvetica',10,'bold'),fill='Black')
    bottom_canvas.create_text(825,155,text='gym@123gmail.com',font=('Helvetica',10,'bold'),fill='Black')


    bottom_canvas.create_line(747,70,830,70,width=3,fill='#fecc09')
    
    #IMAGE FOR BOTTOM
    img_build = PhotoImage(file='./assets/building.png')
    img_build = img_build.subsample(2)
    bottom_canvas.create_image(50,40,image=img_build,anchor='nw' )

    img_location = PhotoImage(file='./assets/location.png')
    img_location = img_location.subsample(2)
    bottom_canvas.create_image(386,40, image = img_location,anchor='nw')

    img_fb = PhotoImage(file='./assets/Facebook.png')
    # bottom_canvas.create_image(750,110,image=img_fb,anchor='nw')
    img_yt = PhotoImage(file='./assets/youtube.png')
    # bottom_canvas.create_image(810,110,image=img_yt,anchor='nw')
    img_tw = PhotoImage(file='./assets/twitter.png')
    # bottom_canvas.create_image(870,110,image=img_tw,anchor='nw')

    def on_facebook():
        webbrowser.open_new("https://www.facebook.com/groups/1775647979239578")
    def on_youtube():
        webbrowser.open_new("https://www.youtube.com/watch?v=lTswlJjBBi0")
    def on_twitter():
        webbrowser.open_new("https://twitter.com/PowerhouseGym")
    facebook_button = Button(bottom_frame,image=img_fb,command=on_facebook,borderwidth=0)
    facebook_button.place(x=760,y=190)

    youtube_button = Button(bottom_frame,image=img_yt,command=on_youtube,borderwidth=0)
    youtube_button.place(x=820,y=195)

    twitter_button = Button(bottom_frame,image=img_tw,command=on_twitter,borderwidth=0)
    twitter_button.place(x=880,y=190)

contact_btn = tk.Button(
    top,
    bg='Black',
    text='CONTACT',
    font=('Helvetica',10,'bold'),width=10, bd=0,
    fg='White',
    activebackground='Black',
    activeforeground='#fecc09',
    relief= tk.FLAT,
    command= contact_info
)

contact_btn.pack(side='right',padx= 15,pady=12)
contact_btn.bind("<Enter>", on_enter_contact)
contact_btn.bind("<Leave>", on_leave_contact)

# ================= KNOWLEDGE BUTTON =================

know_btn = tk.Button(
    top,
    bg='Black',
    fg='White',
    text='KNOWLEDGE',
    font=('Helvetica',10,'bold'),width=10,bd=0,
    activebackground='Black',
    activeforeground='#fecc09',
    relief=tk.FLAT
)
know_btn.pack(side='right',padx= 15,pady=12)
know_btn.bind("<Enter>", on_enter_know)
know_btn.bind("<Leave>", on_leave_know)


# ================= SERVICE BUTTON ================= 
def service_info():
    
    global img1
    mid = tk.Frame(win,bg='White')
    mid.place(y=50,width=1000,height=303)
    img1 = PhotoImage(file='./image/service1.png')
    Label(mid,image=img1,bd=0).place(x=0,y=0)
service_btn = tk.Button(
    top,
    bg='Black',
    fg='White',
    text='SERVICE',
    font=('Helvetica',10,'bold'),width=10,bd=0,
    activebackground='Black',
    activeforeground='#fecc09',
    relief=tk.FLAT,
    command= service_info
)
service_btn.pack(side='right',padx= 15,pady=12)
service_btn.bind("<Enter>", on_enter_service)
service_btn.bind("<Leave>", on_leave_service)


# ================= GYM BUTTON ================= 
# ================= NEW CODEEEEEEEEEEEEEE

def gym_info():
    global img2
    global imgkedoc,imgphanchia,imgHLV
    
    Button(win,text='CLASSIC\n––––––––',font=('Microsoft YaHei UI Light', 12,'bold'),fg='Black',borderwidth=0,command=buttonCl).place(x=40,y=365)
    Button(win,text='ADVANCED\n––––––––',font=('Microsoft YaHei UI Light', 12,'bold'),fg='Black',borderwidth=0,command=buttonAD).place(x=180,y=365)
    mon12()
    
    
    

    mid = tk.Frame(win,bg='White')
    mid.place(y=50,width=1000,height=303)
    # Add this line to create the frame for gym_info's widgets
   
    img2 = PhotoImage(file='./image/Cost.png')
    Label(mid,image=img2,bd=0).place(x=0,y=0)
    
    imgkedoc = PhotoImage(file='./assets/kedoc.png')
    Label(win,image=imgkedoc,fg='white').place(x=350,y=364)

    imgphanchia= PhotoImage(file='./assets/phanchia.png')
    Label(win,image=imgphanchia,fg='white').place(x=55,y=410)

    imgHLV = PhotoImage(file='./image/HLV.png')
    Label(win,image=imgHLV,fg='white').place(x=750,y=354)
    
    # #   add button to click-------------------------------------------------------------------------------------
    # contact admin
    Button(win,text='Sign up now',font=('Microsoft YaHei UI Light', 12,'bold'),bg='#dc5353',fg='white',command=lambda: signupnow(win),width=15).place(x=400,y=550)

def buttonCl():
    test_bt1 =tk.Button(win,text='12\nMonths', width=8,command=mon12,font=('Microsoft YaHei UI Light', 12,'bold'),activebackground='white',activeforeground='#fecc09',borderwidth=0)
    test_bt1.place(x=47,y=430)
    
    test_bt2 =tk.Button(win,text='3\nMonths', width=8,command=mon3,font=('Microsoft YaHei UI Light', 12,'bold'),activebackground='white',activeforeground='#fecc09',borderwidth=0)
    test_bt2.place(x=47,y=500)

    test_bt3 =tk.Button(win,text='6\nMonths', width=8,command=mon6,font=('Microsoft YaHei UI Light', 12,'bold'),activebackground='white',activeforeground='#fecc09',borderwidth=0)
    test_bt3.place(x=145,y=430)

    test_bt4 =tk.Button(win,text='1\nMonth', width=8,command=mon1,font=('Microsoft YaHei UI Light', 12,'bold'),activebackground='white',activeforeground='#fecc09',borderwidth=0)
    test_bt4.place(x=145,y=500)
def buttonAD():
    test_bt5 =tk.Button(win,text='18\nMonths', width=8,command=mon18,font=('Microsoft YaHei UI Light', 12,'bold'),activebackground='white',activeforeground='#fecc09',borderwidth=0)
    test_bt5.place(x=47,y=430)

    test_bt6 =tk.Button(win,text='21\nMonths', width=8,command=mon21,font=('Microsoft YaHei UI Light', 12,'bold'),activebackground='white',activeforeground='#fecc09',borderwidth=0)
    test_bt6.place(x=47,y=500)

    test_bt7 =tk.Button(win,text='2\nYears', width=8,command=year2,font=('Microsoft YaHei UI Light', 12,'bold'),activebackground='white',activeforeground='#fecc09',borderwidth=0)
    test_bt7.place(x=145,y=430)

    test_bt8 =tk.Button(win,text='3\nYears', width=8,command=year3,font=('Microsoft YaHei UI Light', 12,'bold'),activebackground='white',activeforeground='#fecc09',borderwidth=0)
    test_bt8.place(x=145,y=500)

gym_btn = tk.Button(
    top,
    bg='black',
    fg='White',
    text='COST',
    font=('Helvetica',10,'bold'),width=10,bd=0,
    activebackground='Black',
    activeforeground='#fecc09',
    relief=tk.FLAT,
    command= active_both_button
)
gym_btn1 = tk.Button(
    top,
    bg='black',
    fg='White',
    text='COST',
    font=('Helvetica',10,'bold'),width=10,bd=0,
    activebackground='Black',
    activeforeground='#fecc09',
    relief=tk.FLAT,
    command= hiddenContact
)

gym_btn.pack(side='right',padx= 0,pady=12)
gym_btn.bind("<Enter>", on_enter_gym)
gym_btn.bind("<Leave>", on_leave_gym)

# ================= NEW CODEEEEEEEEEEEEEE

# =====================Button in button gym =====================# NEW CODEEEEEEEEEEEEEE

 # === END NEW CODE ====== #

# ================= RESULT BUTTON ================= 

def result_info():
    global img3
    mid = tk.Frame(win,bg='White')
    mid.place(y=50,width=1000,height=303)
    img3 = PhotoImage(file='./image/result.png')
    Label(mid,image=img3,bd=0).place(x=0,y=0)
result_btn = tk.Button(
    top,
    bg='Black',
    fg='White',
    text='RESULT',
    font=('Helvetica',10,'bold'),width=10,bd=0,
    activebackground='Black',
    activeforeground='#fecc09',
    relief=tk.FLAT,
    command= result_info
)
result_btn.pack(side='right',padx= 0,pady=12)
result_btn.bind("<Enter>", on_enter_result)
result_btn.bind("<Leave>", on_leave_result)


win.mainloop()