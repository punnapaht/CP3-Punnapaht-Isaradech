menuList = []
priceList = []

def showBill():
    price = 0
    print("----- My Food -----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number],'Baht')
    for count in priceList:
        price += int(count)
    print("Total price :",price)

while True:
   menuName = input("Please Enter Menu:")
   if (menuName.lower() == "exit"):
       break
   else:
       menuPrice = input("Price :")
       menuList.append(menuName)
       priceList.append(menuPrice)
showBill()
