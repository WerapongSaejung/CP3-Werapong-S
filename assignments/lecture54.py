def login():
    print("กรุณากรอกข้อมูล Username & Password")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return print(showMenu())
    else:
        print("คุณกรอกรหัส Username & Password ไม่ถูกต้อง กรุณากรอกข้อมูลใหม่อีกครั้ง")
        return print(login())

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("พิมพ์ 1 หรือ 2 เพื่อเลือกหัวข้อการทำงาน")
    return print(menuSelect())

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return print(vatCalculator())
    elif userSelected == 2:
        return print(priceCalculator())
    else:
        print("รายการที่คุณเลือกไม่อยู่ใน Menu กรุณากรอกใหม่อีกครั้ง")
        return print(menuSelect())

def vatCalculator():
    print("[--------------------Program Vat Calculator-------------------]")
    print("กรุณาป้อนราคา เพื่อคำนวน VAT")
    price = int(input("price : "))
    vat = 7
    result = price + (price * vat / 100)
    print("ราคารวม VAT =",result)
    return print(showMenu())

def priceCalculator():
    print("[--------------------Program Price Calculator-------------------]")
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    vat = 7
    result = price1+price2
    total_result = (result + (result * vat / 100))
    print("ราคาสินค้าทั้งหมด :",result)
    print("ราคาสินค้าทั้งหมดรวม Vat :",total_result)
    return print(showMenu())

print(login())
