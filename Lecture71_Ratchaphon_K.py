def showBill():
    print("Your bill".center(31, "-"))
    for i in range(len(menulist)):
        print(menulist[i], ":", pricelist[i])
    print("total price :", sum(pricelist))
    print("-".center(31, "-"))

menulist = []
pricelist = []

while True:
    menu = input("menu:")
    if menu.lower() == "exit":
        break
    else:
        price = int(input("price:"))
        menulist.append(menu)
        pricelist.append(price)
showBill()
