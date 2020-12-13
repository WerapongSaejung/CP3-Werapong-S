menuList = []
def showBill():
    totalBill = 0
    textBill = "Your Bill"
    print(textBill.center(60,"-"))
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        totalBill += int(menuList[number][1])
    print("Total Price :",totalBill)

while True :
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Please Enter Your Price :")
        menuList.append([menuName,menuPrice])
print(menuList)
print(showBill())