usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "admin" and passwordInput == "1234":
    print("Log in Success")

    print("----- Werapong Shop -----")
    print("กรุณาเลือกรายการสินค้าเพื่อทำการสั่งซื้อ")
    print("1. Apple ราคา 20")
    print("2. ทุเรียน ราคา 150")
    print("3. มังคุด ราคา 80")
    print("4. เงาะ ราคา 40")

    userSelected = int(input("กรุณาป้อนเลขหมายรายการสินค้าที่ต้องการสั่งซื้อ >>"))
    if userSelected == 1:
        print("สินค้าที่คุณเลือกคือ Apple")
        apple = int(input("กรุณาป้อนจำนวนที่ต้องการสั่งซื้อ : "))
        applePRICE = 20
        print("คุณได้สั่ง Apple จำนวน ", apple , "ลูก ราคาทั้งหมด = ", apple*applePRICE)
    elif userSelected == 2:
        print("สินค้าที่คุณเลือกคือ ทุเรียน")
        durian = int(input("กรุณาป้อนจำนวนที่ต้องการสั่งซื้อ : "))
        durianPRICE = 150
        print("คุณได้สั่ง ทุเรียน จำนวน ", durian , "ลูก ราคาทั้งหมด = ", durian*durianPRICE)
    elif userSelected == 3:
        print("สินค้าที่คุณเลือกคือ มังคุด")
        mangoteen = int(input("กรุณาป้อนจำนวนที่ต้องการสั่งซื้อ : "))
        mangoteenPRICE = 80
        print("คุณได้สั่ง มังคุด จำนวน ", mangoteen, "ลูก ราคาทั้งหมด = ", mangoteen * mangoteenPRICE)
    elif userSelected == 4:
        print("สินค้าที่คุณเลือกคือ เงาะ")
        rambutan = int(input("กรุณาป้อนจำนวนที่ต้องการสั่งซื้อ : "))
        rambutanPRICE = 40
        print("คุณได้สั่ง เงาะ จำนวน ", rambutan, "ลูก ราคาทั้งหมด = ", rambutan * rambutanPRICE)
    else :
        print("กรุณากรอกข้อมูล 1 - 4 เท่านั้น")
else:
    print("ข้อมูล User Name & Password ไม่ถูกต้อง")