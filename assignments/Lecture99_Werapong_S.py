from tkinter import * #นำเข้าฟังก์ชั่นGUI
import math #นำเข้าฟังก์ชั่นคณิตศาตร์

def LefClickButton(event): #ฟังก์ชั่นสำหรับกดปุ่มแล้วนำคำนวนที่นี่
    #print(float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2))
    labelResult.configure(text = round(float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2),2) )
MainWindow = Tk()
labelHight = Label(MainWindow,text = "ส่วนสูง (cm.)")
labelHight.grid(row=0,column = 0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text = "น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>',LefClickButton)
calculateButton.grid(row=2)
labelResult = Label(MainWindow,text = "ผลลัพธ์")
labelResult.grid(row=2,column = 1)
MainWindow.mainloop()