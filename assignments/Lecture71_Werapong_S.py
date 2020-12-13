menuList = []
priceList = []
def showBill():
    totalPrice = 0
    textBill = "Your Bill"
    print(textBill.center(60,"-"))
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        totalPrice += int(priceList[number])
    print("Total Price :",totalPrice)

while True :
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Please Enter Your Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

print(showBill())


'''menuList = []
priceList = []
while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
print(menuList)
print(priceList)    '''