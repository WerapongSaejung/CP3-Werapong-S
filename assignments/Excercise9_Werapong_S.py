usernameInput = input("Username :")
passwordInput = input("Password :")
while usernameInput != "admin" or passwordInput != "1234":
    print("Log in Faile กรุณากรอกข้อมูลอีกครั้ง")
    usernameInput = input("Username :")
    passwordInput = input("Password :")
print("Log in Success เข้าระบบสำเร็จ")
