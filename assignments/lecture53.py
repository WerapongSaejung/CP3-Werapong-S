def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result
totalPrice = int(input("Input Your Total Price : ")) #ประกาศ Input ที่บรรทัดนี้ ชื่อ totalPrice เพื่อส่งค่าไป totalPrice บรรทัดที่ 5
print(vatCalculate(totalPrice))