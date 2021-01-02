class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to ", self.name,self.lastName,"'s Cart")

customer1 = Customer()
customer1.name = "Werapong"
customer1.lastName = "Saejung"
customer1.age = "35"
customer1.addCart()

customer2 = Customer()
customer2.name = "Imdalazio"
customer2.lastName = "Mae"
customer2.age = "33"
customer2.addCart()

customer3 = Customer()
customer3.name = "Yui"
customer3.lastName = "YuiYui"
customer3.age = "30"
customer3.addCart()

customer4 = Customer()
customer4.name = "Pupe"
customer4.lastName = "Supa"
customer4.age = "50"
customer4.addCart()


