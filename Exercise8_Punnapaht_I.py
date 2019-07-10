usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "punnapaht" and passwordInput == "123456" :
    print("-----Welcome to Cosmetics Shop-----")
    print("Order    Product                Price")
    print("1.       Lipstick               1290 THB")
    print("2.       Blush on               690  THB")
    print("3.       Mascara                499  THB")
    print("4.       Eye Shadow             2590 THB")
    print("5.       Foundation             2190 THB")
    print("6.       Concealer              399  THB")
    product = int(input("Select product No.1-6 : "))
    quant = int(input("Quantity(1-5) :"))
    if quant <1 or quant >5 :
      print("Error! , please try again")
    else:
     price = int(input("Enter Price :"))
     total = quant*price
     print("Total Price :",total)
else:
    print("Incorrect username or password ")
