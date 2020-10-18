disTance = float(input("Input distance in kilometer: ")) # รับค่าระยะทาง
time = float(input("Input time in hour: ")) # รับค่าเวลา
v = int(disTance / time)  # คำนวนหาความเร็ว
print("Result : ",v,"km/h")