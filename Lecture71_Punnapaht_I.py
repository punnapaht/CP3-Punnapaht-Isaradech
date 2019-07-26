menuList = []
priceList = []

def showBill():
    print("----- My Food -----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number],'Baht')
    for x in range(len(priceList)):
        price = 0
        price += int(priceList[number])
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
