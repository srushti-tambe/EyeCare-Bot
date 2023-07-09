import customtkinter
import tkinter

# root = customtkinter.CTk()
# root.geometry('300x400')
# f1 = customtkinter.CTkScrollableFrame(master=root, width=200,height=200)
# f1.pack()
# root.mainloop()

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add widgets onto the frame...
        self.l3 = tkinter.Label(master=self)
        self.l2 = customtkinter.CTkLabel(self, text='Hello,what filed are you interested in?', font=('Modern', 20))
        self.l2.grid(row=0, column=0,padx=5)
        # self.place(x=5,y=5)
        self.e1 = customtkinter.CTkEntry(master, font=('Modern', 20), height=40, width=520)
        self.e1.grid(row=10, column=0, pady=10)
        self.e1.focus()
        def sel():
            self.l3 = customtkinter.CTkLabel(self,text='Tell us your symptoms.',font=('Modern',20)).grid(row=17,column=0,sticky=customtkinter.W,padx=5)
            # global l3
            # if (var1.get() == 1):
            #     self.l3.destroy()
            #     self.l3 = customtkinter.CTkLabel(self,text="Which part of your body needs orthopaedic?", font=('Modern',20)).grid(row=7,column=0,padx=5,sticky=customtkinter.W)
            #
            # elif (var1.get() == 2):
            #     self.l3.destroy()
            #     self.l3 = customtkinter.CTkLabel(self,text="What kind of symptons you have been experiencing?", font=('Modern',20))
            #     self.l3.grid(row=7,column=0,padx=10,sticky=customtkinter.W)
            #
            # elif (var1.get() == 3):
            #    self.destroy()
            #    self.l3 = customtkinter.CTkLabel(self,text="What symptons are you experiencing?", font=('Modern',20), justify=LEFT)
            #    self.l3.place(x=2, y=300)
            #
            # elif (var1.get() == 4):
            #   self.l3.destroy()
            #   self.l3 = customtkinter.CTkLabel(self,text="Tell your symptoms", font=('Modern',20), justify=LEFT)
            #   self.l3.place(x=2, y=300)

        var1 = tkinter.IntVar(self,0)
        self.values1 = ["Orthopedics",
                  "Cardiologist",
                  "Psychology",
                  "Neurology",
                  "Ophthalmology",
                  "Pathology",
                  "Oncology",
                  "Gastroenterology",
                  "Audiology",
                  "Immunology",
                  "Otorhinolaryngology",
                  "Homeopathy",
                  "Obstetrics and Gynaecology",
                  "Urology",
                  "Dentistry",
                  "Endocrinology"
                 ]

        # v = tkinter.StringVar(self, "0")
        # for (text, value) in self.values.items():
        #     customtkinter.CTkRadioButton(self, text=text, variable=v,
        #                    value=value).grid(column=0, row=value, sticky=customtkinter.W)

        for i in range(len(self.values1)):
            customtkinter.CTkRadioButton(self,text=self.values1[i],font=('Modern',16),variable=var1,
                                         value=i+1,command=sel).grid(column=0, row=i+1, sticky=customtkinter.W,pady=5)



        l4 = customtkinter.CTkLabel(self,text=self.e1.get(),font=('Modern',20)).grid(row=18,column=0,sticky=customtkinter.W,padx=5)
            # ints = predict_class(message)
            # res = get_response(ints, intents)
            # print(res)
class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("blue")

        self.l1 = customtkinter.CTkLabel(master=self,text='ChatBot',font=('Modern',40))
        self.l1.grid(row=0,column=0)
        self.f1 = MyFrame(master=self, width=500, height=500)
        self.f1.grid(row=1, column=0, padx=20, pady=20)

root = Root()
root.title("ChatBot-your complete health assistant")
root.mainloop()