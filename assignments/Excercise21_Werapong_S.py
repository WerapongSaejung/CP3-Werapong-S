from tkinter import * #นำเข้าฟังก์ชั่นGUI
import math #นำเข้าฟังก์ชั่นคณิตศาตร์

def LefClickButton(event): #ฟังก์ชั่นสำหรับกดปุ่มแล้วนำคำนวนที่นี่
    # print(float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2))
    ResultBMI = (float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2))
    #คำนวนค่า BMI และ ตรวจสอบระดับ ความอ้วน
    if (ResultBMI >= 30):
        labelResult.configure(text = "คุณอ้วนมาก")
    elif (ResultBMI >= 25.0):
        labelResult.configure(text = "คุณอ้วน")
    elif (ResultBMI >= 23.0):
        labelResult.configure(text= "คุณน้ำหนักเกิน")
    elif (ResultBMI >= 18.6):
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    elif (ResultBMI <= 18.5):
        labelResult.configure(text="ผอมเกินไป")

MainWindow = Tk()
labelProgramName = Label(MainWindow,text = "โปรแกรมคำนวนหาค่า BMI เพื่อประเมินความอ้วนหรือผอม")
labelProgramName.grid(row=0)
labelHight = Label(MainWindow,text = "ป้อนค่า ส่วนสูง เป็น (cm.)")
labelHight.grid(row=1,column = 0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=1,column=1)
labelWeight = Label(MainWindow,text = "ป้อนค่า น้ำหนัก เป็น (Kg.)")
labelWeight.grid(row=2,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=2,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>',LefClickButton)
calculateButton.grid(row=3)
labelResult = Label(MainWindow,text = "ผลลัพธ์")
labelResult.grid(row=3,column = 1)
MainWindow.mainloop()