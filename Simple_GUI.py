from tkinter import*
import os
import csv
from tkinter import filedialog
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders



count,c=0,0
creds='/tempfile.temp'

def CheckLogin():
    global  ro
    with open(creds) as f:
        data=csv.reader(f)
        for line in data:
            try:
                uname=line[0]
                pword=line[1]
                if nameEL.get()==uname and pwordEL.get()==pword:
                    rootA.destroy()
                    r=Tk()
                    r.title(':D')
                    #r.iconbitmap(r'20170115_144259.ico')
                    r.geometry('150x50')
                    rlbl=Label(r,text='\n[+] Logged In')
                    rlbl.pack()
                    r.mainloop()
                    send()
            except IndexError:
                pass
        else:
            r=Tk()
            r.title(':D')
            #r.iconbitmap(r'20170115_144259.ico')
            r.geometry('150x50')
            rlbl = Label(r, text='\n[!] Invalid Login')
            rlbl.pack()
            r.mainloop()
            login()

def send():
    global ro
    ro=Tk()
    ro.title('Send Message')
    #ro.iconbitmap(r'20170115_144259.ico')
    ro.geometry('200x100')
    new=Button(ro,text='New Message', relief=GROOVE,command=mail)
    new.grid(row=1,column=0,sticky=N)
    new=Button(ro, text='Log Out', relief=GROOVE, command=logout)
    new.grid(row=1,column=2,sticky=N)
    ro.mainloop()


def mail():
    def attach():
        global count
        root.filename =filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        file=Label(root,text=root.filename)
        file.grid(row=7,column=0,sticky=W)

    def Pass():
        pass
    def Sendmail():
        global count
        global c
        msg=MIMEMultipart()
        msg['From']='abc1234@gmail.com'
        msg['to']=Toe.get()
        msg['Subject']=Subjecte.get()
        body=texte.get("1.0","end-1c")
        msg.attach(MIMEText(body,'plain'))
        if count>0:
            filename=root.filename
            attachment=open(filename,'rb')
            part=MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition","attachment; filename="+filename)
            msg.attach(part)
        else:
            pass
        text=msg.as_string()
        mail=smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login("abc1234@gmail.com","ABC@123")
        try:
            mail.sendmail("abc1234@gmail.com",msg['To'],text)
            c+=1
            print("email sent")
        except:
            print('Error sending mail')
        mail.quit()
        root.destroy()
        if c>=1:
            r=Tk()
            r.title(':D')
            #r.iconbitmap(r'20170115_144259.ico')
            r.geometry('150x50')
            rlbl = Label(r, text='\n[+] Email sent')
            rlbl.pack()
            r.mainloop()
        else:
            r=Tk()
            r.title(':D')
            #r.iconbitmap(r'20170115_144259.ico')
            r.geometry('150x50')
            rlbl = Label(r, text='\n[!] Error Sending Email')
            rlbl.pack()
            r.mainloop()


    root = Tk()
    root.title('New Message')
    #root.iconbitmap(r'20170115_144259.ico')
    To = Label(root, text="To:")
    Subject = Label(root, text="Subject:")
    text = Label(root, text="Message:")
    To.grid(row=1, column=0, sticky=W)
    Subject.grid(row=2, column=0, sticky=W)
    text.grid(row=3, column=0, sticky=NW)

    Toe = Entry(root, width=67)
    Subjecte = Entry(root, width=67)
    texte = Text(root, width=50, height=5)
    Toe.grid(row=1, column=1, sticky=W)
    Subjecte.grid(row=2, column=1, sticky=W)
    texte.grid(row=3, column=1, sticky=W)
    attach=Button(root,text="Attach",relief=GROOVE,command=attach)
    attach.grid(row=6,column=1,sticky=W)
    send=Button(root,text="Send",relief=GROOVE,command=Sendmail)
    send.grid(row=6,column=0,sticky=W)
    file=Label(root,text='')
    file.grid(row=7,column=0,sticky=W)
    root.geometry('500x170')
    root.mainloop()


def logout():
        ro.destroy()
        r = Tk()
        r.title(':D')
        #r.iconbitmap(r'20170115_144259.ico')
        r.geometry('150x100')
        rlbl = Label(r, text='\n[+] Logged Out Successfully.')
        rlbl.pack()
        r.mainloop()
        login()


def Signup():
    global pwordE
    global nameE
    global roots
    #rootA.destroy()
    roots=Tk()
    roots.title("Signup")
    #roots.iconbitmap(r'20170115_144259.ico')
    intruction = Label(roots, text='Please Enter new Credidentials\n')
    intruction.grid(row=0, column=0, sticky=E)
    nameL = Label(roots, text='New Username: ')
    pwordL = Label(roots, text='New Password: ')
    nameL.grid(row=1, column=0, sticky=W)
    pwordL.grid(row=2, column=0, sticky=W)
    nameE = Entry(roots)
    pwordE = Entry(roots, show='*')
    nameE.grid(row=1, column=1)
    pwordE.grid(row=2, column=1)
    signupButton = Button(roots, text='Signup', relief=GROOVE, command=FSSignup)
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop()
def FSSignup():
    with open(creds, 'a') as f:
        f.write(nameE.get())
        f.write(',')
        f.write(pwordE.get())
        f.write('\n')
        f.close()
    roots.destroy()
    login()

def DelUser():
    os.remove(creds)
    rootA.destroy()
    Signup()


def login():
    global nameEL
    global pwordEL
    global rootA

    rootA=Tk()
    rootA.title('Login')
    #rootA.iconbitmap(r'20170115_144259.ico')
    instruction=Label(rootA,text="Please Login\n")
    instruction.grid(sticky=E)

    nameL=Label(rootA,text="Username: ")
    pwordL=Label(rootA,text='Passwprd: ')
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)

    nameEL=Entry(rootA)
    pwordEL=Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)

    loginB=Button(rootA, text='Login',relief=GROOVE,command=CheckLogin)
    loginB.grid(columnspan=2, sticky=W)
    loginB=Button(rootA,text='Signup',relief=GROOVE,command=Signup)
    loginB.grid(columnspan=2,sticky=W)
    rmuser=Button(rootA,text='Delete User',fg='red',relief=GROOVE,command=DelUser)
    rmuser.grid(column=2,sticky=W)
    rootA.mainloop()


if os.path.isfile(creds):
    login()
else:
    Signup()
