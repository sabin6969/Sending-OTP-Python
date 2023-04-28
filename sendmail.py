import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import smtplib
import random
import validators

root = tk.Tk()
root.title("OTP Verification")
root.geometry('300x300')
root.resizable(False,False)
#----Email Entry Box -----#
email_label=tk.Label(root,text="Enter Your Email",font=("sans serif",13),fg="blue")
email_label.place(x=95,y=10)
email_entry=ttk.Entry(root,font=("sans serif",10))
email_entry.place(x=80,y=50,width=175)
#----send otp call back function---#
def send_otp_fun():
    email_add=email_entry.get()
    #validation
    isValid=validators.email(email_add)
    if isValid==True:
        otp_number=""
        #generating otp number using random module
        for i in range(6):
            otp_number+=str(random.randrange(0,9))
        #connection
        try:
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.ehlo()
            connection.starttls()
            your_email_address="example@gmail.com"
            password_for_your_email="demo"
            connection.login(your_email_address,password_for_your_email)
            connection.sendmail(your_email_address,email_add,f"Subject: Regarding OTP \n\nYour One time Password is {otp_number}\nDo not share it with others\nif you have not requested for otp ignore it.")
            messagebox.showinfo("Sucess","Check Your Mail for OTP")
            connection.quit()
            otp_by_user_label=tk.Label(root,text="Enter Your OTP")
            otp_by_user_label.place(x=120,y=120)
            otp_by_user_entry=ttk.Entry(root)
            otp_by_user_entry.place(x=115,y=150,width=100)
            #verify otp call back function#
            def verify_otp():
                otp1=otp_by_user_entry.get()
                otp2=otp_number
                if otp1=="":
                    messagebox.showerror("Required","That Field is Required")
                elif otp1==otp2:
                    messagebox.showinfo("Sucess","OTP Verified")
                    email_entry.delete(0,tk.END)
                    otp_by_user_entry.delete(0,tk.END)
                else:
                    messagebox.showerror("Failed","Wrong OTP")
                    otp_by_user_entry.delete(0,tk.END)
            otp_verify_button=ttk.Button(root,text="Verify",command=verify_otp)
            otp_verify_button.place(x=115,y=175,width=100)
        except:
            messagebox.showerror("Error","Check Your Email and Password")
    else:
        email_entry.delete(0,tk.END)
        messagebox.showerror("Invalid Address","Please Provide a Valid Email Address")

#----request_otp-----#
send_otp_button=ttk.Button(root,text="Send OTP",command=send_otp_fun)
send_otp_button.place(x=115,y=90,width=100)
root.mainloop()
