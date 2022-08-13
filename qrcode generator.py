from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class Qr_generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1050x600+200+50")
        self.root.title("QR Generator|Developed By Pooja Bhardwaj")
        self.root.resizable(False,False)

        title=Label(self.root,text=" QR Code Generator",font=("times new roman",42),bg="#053246",fg='white',anchor='w').place (x=0,y=0,relwidth=1)

        #####Student details window #########
        ########## variables #####
        self.var_stud_admission_no = StringVar()
        self.var_stud_name = StringVar()
        self.var_stud_F_name = StringVar()
        self.var_stud_M_name = StringVar()
        self.var_stud_Bgroup = StringVar()
        self.var_stud_DOB = StringVar()
        self.var_stud_gender = StringVar()
        self.var_stud_contact = StringVar()
        self.var_stud_adhaar_no = StringVar()
        self.var_stud_address = StringVar()
        self.var_stud_course = StringVar()
        self.var_stud_department = StringVar() 
        self.var_stud_URN = StringVar()
        self.var_stud_CRN = StringVar()
        self.var_stud_year = StringVar()
        self.var_stud_section = StringVar()
        self.var_stud_Email = StringVar()

        stud_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        stud_Frame.place(x=40,y=100,width=580,height=480)
        title=Label(stud_Frame,text="Student's Details",font=("goudy old style",20),bg="#053246",fg='white').place (x=0,y=0,relwidth=1)
        
        lb1_admission_no=Label(stud_Frame,text="Admission No",font=("times new roman",15,'bold'),bg="white").place (x=10,y=60)
        lb1_name = Label(stud_Frame, text="Student Name", font=("times new roman", 15,'bold'), bg="white").place(x=10, y=100)
        lb1_F_name=Label(stud_Frame,text="Father Name",font=("times new roman",15,'bold'),bg="white").place (x=10,y=140)
        lb1_M_name=Label(stud_Frame,text="Mother Name",font=("times new roman",15,'bold'),bg="white").place (x=10,y=180)
        lb1_E_gender=Label(stud_Frame,text="Gender",font=("times new roman",15,'bold'),bg="white").place (x=10,y=220)
        lb1_DOB=Label(stud_Frame,text="DOB",font=("times new roman",15,'bold'),bg="white").place (x=310,y=100)
        lb1_Bgroup=Label(stud_Frame,text="Blood Group",font=("times new roman",15,'bold'),bg="white").place (x=310,y=140)
        lb1_contact=Label(stud_Frame,text="Contact No",font=("times new roman",15,'bold'),bg="white").place (x=310,y=180)
        lb1_adhaar_no=Label(stud_Frame,text="Adhaar No",font=("times new roman",15,'bold'),bg="white").place (x=310,y=220)
        lb1_Email=Label(stud_Frame,text="Email",font=("times new roman",15,'bold'),bg="white").place (x=10,y=260)
        lb1_address=Label(stud_Frame,text="Address",font=("times new roman",15,'bold'),bg="white").place (x=10,y=300)


        
        txt_admission_no=Entry(stud_Frame,font=("times new roman",15),textvariable=self.var_stud_admission_no ,bg="light yellow").place (x=140,y=60)
        txt_name = Entry(stud_Frame, font=("times new roman", 15),textvariable=self.var_stud_name ,bg="light yellow").place(x=140, y=100,width=150)
        txt_F_name = Entry(stud_Frame, font=("times new roman", 15),textvariable=self.var_stud_F_name , bg="light yellow").place(x=140, y=140,width=150)
        txt_M_name = Entry(stud_Frame, font=("times new roman", 15),textvariable=self.var_stud_M_name ,bg="light yellow").place(x=140, y=180,width=150)
        txt_gender = Entry(stud_Frame, font=("times new roman", 15),textvariable=self.var_stud_gender ,bg="light yellow").place(x=140, y=220,width=150)
        txt_DOB = Entry(stud_Frame, font=("times new roman", 15),textvariable=self.var_stud_DOB ,bg="light yellow").place(x=433, y=100,width=130)
        txt_Bgroup = Entry(stud_Frame, font=("times new roman", 15),textvariable=self.var_stud_Bgroup ,bg="light yellow").place(x=433, y=140,width=130)
        txt_contact = Entry(stud_Frame, font=("times new roman", 15),textvariable=self.var_stud_contact ,bg="light yellow").place(x=433, y=180,width=130)
        txt_adhaar_no = Entry(stud_Frame, font=("times new roman", 15),textvariable=self.var_stud_adhaar_no ,bg="light yellow").place(x=433, y=220,width=130)
        txt_Email= Entry(stud_Frame, font=("times new roman", 15),textvariable=self.var_stud_Email,bg="light yellow").place(x=140, y=260,width=400)
        txt_address= Entry(stud_Frame, font=("times new roman", 15),textvariable=self.var_stud_address,bg="light yellow").place(x=140, y=300,width=400,height=57)


        btn_generator = Button(stud_Frame, text="QR Generate",command=self.generate,font=("times new roman", 15,'bold'), bg="#2196f3", fg='white').place(x=90, y=380,width=180,height=30)
        btn_clear = Button(stud_Frame, text="Clear",command=self.clear,font=("times new roman", 15,'bold'), bg="gray", fg='white').place(x=300, y=380,width=120,height=30)

        self.msg=''
        self.lb1_msg=Label(stud_Frame,text=self.msg,font=("times new roman",20),bg="white",fg='green')
        self.lb1_msg.place(x=-20,y=420,relwidth=1)

        qua_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qua_Frame.place(x=630, y=101, width=400, height=190)
        title=Label(qua_Frame,text="Qualification",font=("goudy old style",20),bg="#053246",fg='white').place (x=0,y=0,relwidth=1)
        #============ qualification ======================
        lb1_course=Label(qua_Frame,text="Course",font=("times new roman",15,'bold'),bg="white").place (x=10,y=45)
        lb1_department=Label(qua_Frame,text="Department",font=("times new roman",15,'bold'),bg="white").place (x=10,y=80)
        lb1_URN=Label(qua_Frame,text="URN",font=("times new roman",15,'bold'),bg="white").place (x=10,y=115)
        lb1_CRN=Label(qua_Frame,text="CRN",font=("times new roman",15,'bold'),bg="white").place (x=10,y=150)
        lb1_year=Label(qua_Frame,text="Year",font=("times new roman",15,'bold'),bg="white").place (x=200,y=115)
        lb1_section=Label(qua_Frame,text="Section",font=("times new roman",15,'bold'),bg="white").place (x=200,y=150)


        txt_course = Entry(qua_Frame, font=("times new roman", 15),textvariable=self.var_stud_course , bg="light yellow").place(x=150, y=45)
        txt_department = Entry(qua_Frame, font=("times new roman", 15),textvariable=self.var_stud_department ,bg="light yellow").place(x=150, y=80)
        txt_URN = Entry(qua_Frame, font=("times new roman", 15),textvariable=self.var_stud_URN ,bg="light yellow").place(x=90, y=115,width=90)
        txt_CRN = Entry(qua_Frame, font=("times new roman", 15),textvariable=self.var_stud_CRN ,bg="light yellow").place(x=90, y=150,width=90)
        txt_year = Entry(qua_Frame, font=("times new roman", 15),textvariable=self.var_stud_year ,bg="light yellow").place(x=290, y=115,width=90)
        txt_section = Entry(qua_Frame, font=("times new roman", 15),textvariable=self.var_stud_section ,bg="light yellow").place(x=290, y=150,width=90)
        


        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_Frame.place(x=630,y=300,width=400,height=280)
        title=Label(qr_Frame,text="Student QR Code",font=("goudy old style",20),bg="#053246",fg='white').place (x=0,y=0,relwidth=1)
        
        self.qr_code=Label(qr_Frame,text='No QR \nAvaliable',font=("times new roman",20),bg="light blue",fg='dark blue',bd=1,relief=RIDGE)
        self.qr_code.place(x=100, y=80, width=180, height=170)


    
    def clear(self):
        self.var_stud_admission_no.set('')
        self.var_stud_name.set('')
        self.var_stud_F_name.set('')
        self.var_stud_M_name.set('')
        self.var_stud_gender.set('')
        self.var_stud_DOB.set('')
        self.var_stud_adhaar_no.set('')
        self.var_stud_Bgroup.set('')
        self.var_stud_contact.set('')
        self.var_stud_address.set('')
        self.var_stud_Email.set('')
        self.msg = ''
        self.lb1_msg.config(text=self.msg)
        self.qr_code.config(image='')
        self.var_stud_URN.set('')
        self.var_stud_CRN.set('')
        self.var_stud_year.set('')
        self.var_stud_section.set('')



    def generate(self):
        if self.var_stud_admission_no.get() == '' or self.var_stud_name.get() == '' or self.var_stud_F_name.get() == '' or self.var_stud_M_name.get() == '' or self.var_stud_gender.get() == '' or self.var_stud_DOB.get() == '' or self.var_stud_Bgroup.get() == '' or self.var_stud_contact.get() == '' or self.var_stud_address.get() == '' or self.var_stud_Email.get() == '' or self.var_stud_adhaar_no.get() == '' or self.var_stud_course.get() == '' or self.var_stud_department.get() == '' or self.var_stud_URN.get() == '' or self.var_stud_CRN.get() == '' or self.var_stud_year.get() == '' or self.var_stud_section.get() == '':
            self.msg='All Field are Required!!!'
            self.lb1_msg.config(text=self.msg,fg='red')
        else:
            qr_data = (f"Admission No:{self.var_stud_admission_no.get()}\n\nStudent Name:{self.var_stud_name.get()}\n\nFather Name:{self.var_stud_F_name.get()}\n\nMother Name:{self.var_stud_M_name.get()}\n\nGender:{self.var_stud_gender.get()}\n\nDOB:{self.var_stud_DOB.get()}\n\nBlood Group:{self.var_stud_Bgroup.get()}\n\nContact No:{self.var_stud_contact.get()}\n\nAdhaar No:{self.var_stud_adhaar_no.get()}\n\nEmail:{self.var_stud_Email.get()}\n\nAddress:{self.var_stud_address.get()}\n\nCourse:{self.var_stud_course.get()}\n\nDepartment:{self.var_stud_department.get()}\n\nURN:{self.var_stud_URN.get()}\n\nCRN:{self.var_stud_CRN.get()}\n\nYear:{self.var_stud_year.get()}\n\nSection:{self.var_stud_section.get()}")
            qr_code=qrcode.make(qr_data)
            # print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("student_QR/Stud_"+str(self.var_stud_admission_no.get())+'.png')
            # #========QR code image updating===========
            self.im=ImageTk.PhotoImage(file="student_QR/Stud_"+str(self.var_stud_admission_no.get())+'.png')
            self.qr_code.config(image=self.im)
            # #======== updating Notification ==========
            self.msg = 'QR Generated Successfully!!'
            self.lb1_msg.config(text=self.msg,fg='green')

root=Tk()
obj=Qr_generator(root)
root.mainloop()

