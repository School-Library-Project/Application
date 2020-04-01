from tkinter import *
from PIL import ImageTk
class MainWindow:
    def __init__(self):
        self.width = 1440
        self.height = 900
        self.sost = 0
        self.fonti = "Italic 20"
        self.stat = 0
        self.stat_stud = 1
        self.back_img =ImageTk.PhotoImage(file="img/background_img.png")#
        self.logo_img = ImageTk.PhotoImage(file="img/logo.png")#
        self.image_stud = ImageTk.PhotoImage(file="img/students_button.png")#
        self.image_book = ImageTk.PhotoImage(file="img/books_button.png")#
        self.image_options = ImageTk.PhotoImage(file="img/options_button.png")#
        self.line_img = ImageTk.PhotoImage(file = "img/line.png")#
        self.title1_image = ImageTk.PhotoImage(file="img/title.png")#
        self.image_add = ImageTk.PhotoImage(file="img/add_book_button.png")#
        self.image_give = ImageTk.PhotoImage(file="img/give_button.png")#
        
        
        self.title_add_book = ImageTk.PhotoImage(file="img/title_add_book.png")#
        self.panel_add_book = ImageTk.PhotoImage(file="img/add_book_panel.png")#
        
        self.delet_button = ImageTk.PhotoImage(file="img/delete_button.png")#
        self.ok_img = ImageTk.PhotoImage(file="img/OK_button.png")#
        self.title_delet_book = ImageTk.PhotoImage(file="img/delet_title.png")#
        self.scan_img = ImageTk.PhotoImage(file="img/scan_qr.png")#
        self.title_give_book = ImageTk.PhotoImage(file="img/give_book_title.png")#
        
        self.title_put_book = ImageTk.PhotoImage(file="img/put_book_title.png")#
        self.panel_give_put_book = ImageTk.PhotoImage(file="img/give_book_panel.png")#
        self.image_put = ImageTk.PhotoImage(file="img/put_button.png")#
        
        self.error = ImageTk.PhotoImage(file="img/error.png")#
        self.norma = ImageTk.PhotoImage(file="img/succes.png")#


        self.stud_img_title = ImageTk.PhotoImage(file="img/options_stud_title.png")#
        
        self.stud_add_button = ImageTk.PhotoImage(file="img/add_stud_button.png")#
        self.stud_add_title_img = ImageTk.PhotoImage(file="img/title_add_stud.png")#
        self.stud_add_panel_img = ImageTk.PhotoImage(file="img/add_stud_panel.png")#
        
        self.stud_spis_button = ImageTk.PhotoImage(file="img/spis_stud_button.png")#
        self.stud_spis_title_img = ImageTk.PhotoImage(file="img/title_spis_stud.png")#
        
        self.stud_delet_button = ImageTk.PhotoImage(file="img/delete_stud_button.png")#
        self.stud_delet_title_img = ImageTk.PhotoImage(file="img/title_delet_stud.png")#
        self.stud_delet_panel_img = ImageTk.PhotoImage(file="img/delet_stud_panel.png")#
        
        self.book_img_title = ImageTk.PhotoImage(file="img/books_title.png")#
        self.book_img_panel = ImageTk.PhotoImage(file="img/background_books.png")#
        #---------------------------------Left-------------------------------------------------
        self.background = Label(root,image = self.back_img)
        self.line = Label(root,image = self.line_img)
        self.options_b = Button(root, image=self.image_options,border="0", command=lambda: self.options_page())
        self.book_b = Button(root, image=self.image_book,border="0", command=lambda: self.books_func_open())
        self.stud_b = Button(root, image=self.image_stud,border="0", command=lambda: self.students_func_open())
        self.logo = Label(root,image = self.logo_img)
        #---------------------------------Left-------------------------------------------------
        
        self.title1 = Label(root,image = self.title1_image,border="0")
        self.add_book = Button(root,image = self.image_add,border="0",command = lambda: self.add_book_page())
        self.give_book = Button(root,image = self.image_give,border="0",command = lambda:self.give_book_page())
        self.put_book = Button(root,image = self.image_put,border="0",command = lambda:self.put_book_page())
        self.delet_book = Button(root,image=self.delet_button,border="0",command = lambda:self.delet_book_page())

        #------------------------------add book------------------------------------------------
        self.title_add = Label(root,image = self.title_add_book)
        self.panel_add = Label(root,image = self.panel_add_book)
        self.button_ok = Button(root,image = self.ok_img,command = lambda:self.add_book_func())
        self.enter_name = Entry(root,border="1",font=self.fonti)
        self.enter_type = Entry(root,border="1",font=self.fonti)
        self.enter_class = Entry(root,border="1",font=self.fonti)
        self.enter_name_p = Entry(root,border="1",font=self.fonti)
        self.enter_year = Entry(root,border="1",font=self.fonti)
        self.enter_count = Entry(root,border="1",font=self.fonti)
        #------------------------------add book------------------------------------------------

        #------------------------------give book-----------------------------------------------
        self.give_title = Label(root,image=self.title_give_book)
        self.give_panel = Label(root,image=self.panel_give_put_book)
        self.give_ok = Button(root,border="0",image=self.ok_img,command = lambda:self.give_put_book_func(self.give_enter.get(),1))
        self.give_scan = Button(root,border="0",image=self.scan_img)
        self.give_enter = Entry(root,border="1",font=self.fonti)
        self.give_error = Label(root,border="0",image=self.error)
        #------------------------------give book-----------------------------------------------

        #------------------------------put book------------------------------------------------
        self.put_title = Label(root,image=self.title_put_book)
        self.put_panel = Label(root,image=self.panel_give_put_book)
        self.put_ok = Button(root,border="0",image=self.ok_img,command = lambda:self.give_put_book_func(self.put_enter.get(),0))
        self.put_scan = Button(root,border="0",image=self.scan_img)
        self.put_enter = Entry(root,border="1",font=self.fonti)
        self.put_error = Label(root,border="0",image=self.error)
        #------------------------------put book------------------------------------------------

        #------------------------------delet book----------------------------------------------
        self.delet_title = Label(root,image=self.title_delet_book)
        self.delet_panel = Label(root,image=self.panel_give_put_book)
        self.delet_ok = Button(root,border="0",image=self.ok_img,command = lambda: self.delete_func(self.delet_enter.get(),"book"))
        self.delet_scan = Button(root,border="0",image=self.scan_img)
        self.delet_enter = Entry(root,border="1",font=self.fonti)
        self.delet_error = Label(root,border="0",image=self.error)
        #------------------------------delet book----------------------------------------------


        #------------------------------students page-------------------------------------------
        self.stud_title = Label(root,image = self.stud_img_title)
        
        self.stud_add_title = Label(root,image=self.stud_add_title_img)
        self.stud_add = Button(root,border="0",image = self.stud_add_button,command = lambda: self.stud_add_open())
        self.stud_add_panel = Label(root,image=self.stud_add_panel_img)
        self.stud_add_ok = Button(root,image=self.ok_img,border="0",command = lambda: self.stud_add_func(self.stud_add_name1.get(),self.stud_add_name2.get(),self.stud_add_name3.get(),self.stud_add_class.get()))
        self.stud_add_class = Entry(root,border="1",font=self.fonti)
        self.stud_error_class = Label(root,image=self.error)
        
        self.stud_add_name1 = Entry(root,border="1",font=self.fonti)
        self.stud_error_name1 = Label(root,image=self.error)
        
        self.stud_add_name2 = Entry(root,border="1",font=self.fonti)
        self.stud_error_name2 = Label(root,image=self.error)
        
        self.stud_add_name3 = Entry(root,border="1",font=self.fonti)
        self.stud_error_name3 = Label(root,image=self.error)

        self.stud_spis_title = Label(root,image=self.stud_spis_title_img)
        self.stud_spis = Button(root,border="0",image = self.stud_spis_button,command = lambda: self.stud_spis_func())

        self.stud_delet_title = Label(root,image=self.stud_delet_title_img)
        self.stud_delet = Button(root,border="0",image = self.stud_delet_button,command = lambda: self.stud_delet_open())
        self.stud_delet_panel = Label(root,image = self.stud_delet_panel_img)
        self.stud_delet_ok = Button(root,image=self.ok_img,command = lambda: self.delete_func(self.stud_delet_enter.get(),"students"))
        self.stud_delet_enter = Entry(root,border="1",font=self.fonti)
        self.stud_delet_error = Label(root,image=self.error)
        #------------------------------students page-------------------------------------------

        
        #------------------------------books page----------------------------------------------
        self.book_title = Label(root,image = self.book_img_title)
        self.book_panel = Label(root,image = self.book_img_panel)
        #------------------------------books page----------------------------------------------
    def initalize_window(self):
        self.background.place(x=0,y=0,width = 1440,height = 900)
        
        self.title1.place(x=417,y=0,width=1023,height=200)
        self.add_book.place(x=450,y=334,width=471,height=178)
        self.give_book.place(x=450,y=615,width=471,height=178)
        self.put_book.place(x=935,y=614,width=471,height=178)
        self.delet_book.place(x=937,y=337,width=471,height=178)
        
        self.line.place(x=420,y=0,width=1,height = 900)
        self.options_b.place(x=26,y=687,width=378,height=147)
        self.book_b.place(x=23,y=461,width=378,height=147)
        self.stud_b.place(x=27,y=236,width=378,height=147)
        self.logo.place(x=0,y=0,width=434,height=201)
    def options_page(self):
        self.on_off(self.sost)
        self.title1.place(x=417,y=0,width=1023,height=200)
        self.add_book.place(x=450,y=334,width=471,height=178)
        self.give_book.place(x=450,y=615,width=471,height=178)
        self.put_book.place(x=935,y=614,width=471,height=178)
        self.delet_book.place(x=937,y=337,width=471,height=178)
        self.sost = 0
    def add_book_page(self):
        self.on_off(self.sost)
        self.title_add.place(x=418,y=0,width=1022,height=195)
        self.panel_add.place(x=466,y=260,width=942,height=549)
        self.button_ok.place(x=1303,y=726,width=69,height=50)# x=1303,y=726|1150 726
        
        self.enter_name.place(x=830,y=300,width = 300,height=35)
        self.enter_type.place(x=720,y=380,width = 300,height=35)
        self.enter_class.place(x=670,y=465,width = 300,height=35)
        self.enter_name_p.place(x=960,y=545,width = 300,height=35)
        self.enter_year.place(x=770,y=630,width = 300,height=35)
        self.enter_count.place(x=860,y=715,width = 300,height=35)
        self.sost = 1
    def give_book_page(self):
        self.on_off(self.sost)
        self.give_title.place(x=414,y=0,width=1026,height=199)
        self.give_panel.place(x=466,y=249,width=924,height=406)
        self.give_ok.place(x=1270,y=563,width=69,height=50)
        self.give_scan.place(x=499,y=289,width=443,height=66)
        self.give_enter.place(x=730,y=415,width=300,height=35)
        self.sost = 2
    def put_book_page(self):
        self.on_off(self.sost)
        self.put_title.place(x=417,y=0,width=1023,height=202)
        self.put_panel.place(x=466,y=249,width=924,height=406)
        self.put_ok.place(x=1270,y=563,width=69,height=50)
        self.put_scan.place(x=499,y=289,width=443,height=66)
        self.put_enter.place(x=730,y=415,width=300,height=35)
        self.sost = 3
    def delet_book_page(self):
        self.on_off(self.sost)
        self.delet_title.place(x=411,y=0,width=1029,height=197)
        self.delet_panel.place(x=466,y=249,width=924,height=406)
        self.delet_ok.place(x=1270,y=563,width=69,height=50)
        self.delet_scan.place(x=499,y=289,width=443,height=66)
        self.delet_enter.place(x=730,y=415,width=300,height=35)
        self.sost = 4
    def add_enter_clear(self):
        self.errors([self.enter_name,self.enter_type,self.enter_class,self.enter_name_p,self.enter_year,self.enter_count],"enter")
    def books_func_open(self):
        self.on_off(self.sost)
        self.book_title.place(x=418,y=0,width=1022,height=173)
        self.book_panel.place(x=460,y=197,width=958,height=692)
        self.sost = 5
    def students_func_open(self):
        self.on_off(self.sost)
        self.stud_title.place(x=418,y=0,width=1022,height=173)

        self.stud_add.place(x=489,y=326,width=424,height=194)
        self.stud_spis.place(x=489,y=595,width=881,height=179)
        self.stud_delet.place(x=948,y=330,width=424,height=194)
        self.sost = 6
    def stud_add_open(self):
        self.on_off(self.sost)
        self.stud_add_title.place(x=413,y=0,width=1027,height=179)
        self.stud_add_panel.place(x=477,y=245,width=906,height=392)
        self.stud_add_ok.place(x=1292,y=564,width=69,height=50)#x=1292|1100
        self.stud_add_class.place(x=660,y=290,width=300,height=35)
        self.stud_add_name1.place(x=630,y=365,width=300,height=35)
        self.stud_add_name2.place(x=730,y=440,width=300,height=35)
        self.stud_add_name3.place(x=730,y=525,width=300,height=35)
        self.sost = 7
    def stud_spis_func(self):
        self.on_off(self.sost)
        self.stud_spis_title.place(x=418,y=0,width=1022,height=173)
        self.sost = 8
    def stud_delet_open(self):
        self.on_off(self.sost)
        self.stud_delet_title.place(x=413,y=0,width=1027,height=179)
        self.stud_delet_panel.place(x=460,y=235,width=939,height=246)
        self.stud_delet_ok.place(x=1286,y=400,width=69,height=50)#x=1286|1100
        self.stud_delet_enter.place(x=780,y=295,width=300,height=35)
        self.sost = 9
    def stud_add_func(self,name1,name2,name3,clas):
        self.errors([self.stud_error_class,self.stud_error_name1,self.stud_error_name2,self.stud_error_name3],"error")
        error = 0
        if clas=="":
            self.stud_error_class.place(x=995,y=290,width=35,height=35)
            error+=1
        if name1=="":
            self.stud_error_name1.place(x=965,y=365,width=35,height=35)
            error+=1
        if name2=="":
            self.stud_error_name2.place(x=1065,y=440,width=35,height=35)
            error+=1
        if name3=="":
            self.stud_error_name3.place(x=1065,y=525,width=35,height=35)
            error+=1
        if error>0:
            return 0
        id = -1
        for i in open("students.txt", "r"):
            id = int(i.split("|")[0])
        if (id//10**self.stat_stud):
            num = id
            while(num>0):
                self.stat_stud+=1
                num//=10
        if id==-1:
            id+=1
        else:
            id+=1
        f = open("students.txt","a")
        string = name1+"|"+name2+"|"+name3+"|"+clas
        f.write(("0"*(5-self.stat_stud))+str(id)+"|"+string+"\n")
        f.close()
#############################################################################################################################################################
    def on_off(self,type_of):
        if (type_of==0):
            self.errors([self.title1,self.add_book,self.give_book,self.put_book,self.delet_book],"error")
        if (type_of==1):
            self.errors([self.title_add,self.panel_add,self.button_ok,self.enter_name,self.enter_type,self.enter_class,self.enter_name_p,self.enter_year,self.enter_count],"error")
            self.add_enter_clear()
        if (type_of==2):
            self.errors([self.give_title,self.give_panel,self.give_ok,self.give_scan,self.give_enter,self.give_error],"error")
            self.give_enter.delete(0,'end')
        if (type_of==3):
            self.errors([self.put_title,self.put_panel,self.put_ok,self.put_scan,self.put_enter,self.put_error],"error")
            self.put_enter.delete(0,'end')
        if (type_of==4):
            self.errors([self.delet_title,self.delet_panel,self.delet_ok,self.delet_scan,self.delet_enter,self.delet_error],"error")
            self.delet_enter.delete(0,'end')
            self.delet_error["image"] = self.error
        if (type_of==5):
            self.errors([self.book_title,self.book_panel],"error")
        if (type_of==6):
            self.errors([self.stud_title,self.stud_add,self.stud_spis,self.stud_delet],"error")
        if (type_of==7):
            self.errors([self.stud_add_title,self.stud_add_panel,self.stud_add_ok,self.stud_add_name1,self.stud_add_name2,self.stud_add_name3,self.stud_add_class,self.stud_error_class,self.stud_error_name1,self.stud_error_name2,self.stud_error_name3],"error")
        if (type_of==8):
            self.stud_spis_title.place_forget()
        if (type_of==9):
            self.errors([self.stud_delet_title,self.stud_delet_panel,self.stud_delet_ok,self.stud_delet_enter,stud_delet_error],"error")
#############################################################################################################################################################
    def errors(self,arr_of_errors,type_of):
        for i in arr_of_errors:
            if type_of=="error":
                i.place_forget()
            if type_of=="enter":
                i.delete(0,'end')
    def add_book_func(self):
        string = self.enter_name.get()+"|"+self.enter_type.get()+"|"+self.enter_class.get()+"|"+self.enter_name_p.get()+"|"+self.enter_year.get()
        id = 0
        num = 0
        for i in open("books.txt", "r"):
            id = int(i.split("|")[0])
        num = id
        while(num>0):
            self.stat+=1
            num//=10
        if id==0:
            self.stat = 1
        else:
            id+=1
        f = open("books.txt","a")
        l = open("status.txt","a")
        for i in range(int(self.enter_count.get())):
            if (id//(10**self.stat))>0:
                self.stat+=1
            f.write(("0"*(5-self.stat))+str(id)+"|"+string+"\n")
            l.write(("0"*(5-self.stat))+str(id)+"|0\n")
            id+=1
        f.close()
        self.add_enter_clear()
        self.stat = 0
    def join_all(self,arr):
        for i in range(len(arr)):
            arr[i] = "|".join(arr[i])
        return arr
    def delete_func(self,id,type_of):
        if type_of=="book":
            self.delet_error.place_forget()
            value = [i.split("|") for i in open("books.txt","r",encoding="ISO-8859-1")]
            status = [i for i in open("status.txt","r",encoding="ISO-8859-1")]
        if type_of=="students":
            self.stud_delet_error.place_forget()
            value = [i.split("|") for i in open("students.txt","r",encoding="ISO-8859-1")]
        if (id.isdigit() and int(id)<int(value[len(value)-1][0])):
            for i in range(len(value)):
                if int(value[i][0])==int(id):
                    del value[i]
                    if type_of=="book":
                        del status[i]
                    value = self.join_all(value)
                    if type_of=="book":
                        b = open("books.txt","w",encoding="ISO-8859-1")
                        s = open("status.txt","w",encoding="ISO-8859-1")
                    if type_of=="students":
                        b = open("students.txt","w",encoding="ISO-8859-1")
                    for i in range(len(value)):
                        b.write(value[i])
                        if type_of=="book":
                            s.write(status[i])
                    b.close()
                    if type_of=="book":
                        s.close()
                        self.delet_error["image"] = self.norma
                        self.delet_error.place(x=1035,y=415,width=35,height=35)
                        self.delet_enter.delete(0,'end')
                    if type_of=="students":
                        self.stud_delet_error["image"] = self.norma
                        self.stud_delet_error.place(x=1080,y=295,width=35,height=35)
                        self.stud_delet_enter.delete(0,'end')
                    break
            return 0
        if (len(id.split("-"))==2):
            id = id.split("-")
            if ((id[0].isdigit() and (int(id[0])>0)) and (id[1].isdigit() and int(id[1])<=int(value[len(value)-1][0])) and (int(id[0])<int(id[1]))):
                ch = 0
                for i in range(len(value)):
                    if (int(value[i][0])==int(id[0])):
                        ch = i
                        break
                for i in range(int(id[0]),int(id[1])+1):
                    if (i==int(value[ch][0])):
                        del value[ch]
                        if type_of=="book":
                            del status[ch]
                value = self.join_all(value)
                if type_of=="book":
                    b = open("books.txt","w",encoding="ISO-8859-1")
                    s = open("status.txt","w",encoding="ISO-8859-1")
                if type_of=="students":
                     b = open("students.txt","w",encoding="ISO-8859-1")
                for i in range(len(value)):
                    b.write(value[i])
                    if type_of=="book":
                        s.write(status[i])
                b.close()
                if type_of=="book":
                    s.close()
                    self.delet_error["image"] = self.norma
                    self.delet_error.place(x=1035,y=415,width=35,height=35)
                    self.delet_enter.delete(0,'end')
                if type_of=="students":
                    self.stud_delet_error["image"] = self.norma
                    self.stud_delet_error.place(x=1080,y=295,width=35,height=35)
                    self.stud_delet_enter.delete(0,'end')
            return 0
        try:
            id = int(id)
            if (id >int(value[len(value)-1][0])):
                if type_of=="book":
                    self.delet_error["image"] = self.error
                    self.delet_error.place(x=1035,y=415,width=35,height=35)
                if type_of=="students":
                    self.stud_delet_error["image"] = self.error
                    self.stud_delet_error.place(x=1080,y=295,width=35,height=35)
                return 0
        except:
            if type_of=="book":
                self.delet_error["image"] = self.error
                self.delet_error.place(x=1035,y=415,width=35,height=35)
            if type_of=="students":
                self.stud_delet_error["image"] = self.error
                self.stud_delet_error.place(x=1080,y=295,width=35,height=35)
            return 0
    def give_put_book_func(self,id,type):
        status = [i.split("|") for i in open("status.txt","r",encoding="ISO-8859-1")]
        if (id.isdigit() and int(id)<int(status[len(status)-1][0])):
            for i in range(len(status)):
                if (int(status[i][0])==int(id)):
                    status[i][1] = str(type)+"\n"
                    status = self.join_all(status)
                    s = open("status.txt","w",encoding="ISO-8859-1")
                    for i in range(len(status)):
                        s.write(status[i])
                    s.close()
                    if type==1:
                        self.give_error["image"] = self.norma
                        self.give_error.place(x=1035,y=415,width=35,height=35)
                        self.give_enter.delete(0,'end')
                    if type==0:
                        self.put_error["image"] = self.norma
                        self.put_error.place(x=1035,y=415,width=35,height=35)
                        self.put_enter.delete(0,'end')
            return 0
        if (len(id.split("-"))==2):
            id = id.split("-")
            if ((id[0].isdigit() and (int(id[0])>=0)) and (id[1].isdigit() and int(id[1])<=int(status[len(status)-1][0])) and (int(id[0])<int(id[1]))):
                for i in range(int(id[0]),int(id[1])+1):
                    if (int(id[0])<=int(status[i][0]) and int(status[i][0])<=int(id[1])):
                        status[i][1] = str(type)+"\n"
                status = self.join_all(status)
                s = open("status.txt","w",encoding="ISO-8859-1")
                for i in range(len(status)):
                    s.write(status[i])
                s.close()
                if type==1:
                    self.give_error["image"] = self.norma
                    self.give_error.place(x=1035,y=415,width=35,height=35)
                    self.give_enter.delete(0,'end')
                if type==0:
                    self.put_error["image"] = self.norma
                    self.put_error.place(x=1035,y=415,width=35,height=35)
                    self.put_enter.delete(0,'end')
                return 0
        try:
            id = int(id)
            if (id >int(status[len(status)-1][0])):
                if type==1:
                    self.give_error["image"] = self.error
                    self.give_error.place(x=1035,y=415,width=35,height=35)
                if type==0:
                    self.put_error["image"] = self.error
                    self.put_error.place(x=1035,y=415,width=35,height=35)
                return 0
        except:
            if type==1:
                self.give_error["image"] = self.error
                self.give_error.place(x=1035,y=415,width=35,height=35)
            if type==0:
                self.put_error["image"] = self.error
                self.put_error.place(x=1035,y=415,width=35,height=35)
            return 0
        
root = Tk()
root.title("library")
root.geometry("1440x900")

window = MainWindow()
window.initalize_window()

root.mainloop()
