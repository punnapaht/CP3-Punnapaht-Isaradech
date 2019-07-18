def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "punnapaht" and passwordInput == "123456":
        return showMenu()
    else:
        print("Wrong !, please try again")
        return login()
def showMenu():
    print("----Shop----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print("Price include vat :",vatCalculate(int(input("Product Price : "))))
    elif userSelected == 2 :
        print("Total Price : ",priceCalculate())
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice*vat/100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

login()
