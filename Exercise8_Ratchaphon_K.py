Usernameinput = input("Username : ")
Passwordinput = input("Password : ")
if Usernameinput == "prayut" and Passwordinput == "0001":
    computerprice = 15900
    laptopprice = 20000
    iphonexsprice = 30000

    print("-----------Welcome to shop--------------------------------------\n"
        "1.Computer   ราคา :",computerprice,"บาท\n"
        "2.Laptop     ราคา :",laptopprice,"บาท\n"
        "3.Iphone xs  ราคา :",iphonexsprice,"บาท\n"
        "เรามีส่วนลดพิเศษสำหรับ Iphone xs *ถ้าซื้อ Iphone xs :2 เครื่องขึ้นไปรับไปเลยส่วนลด 1000 บาท!!\n"
        "------------------------------------------------------------------")

    selectproducts = input("โปรดเลือกสินค้า : ")
    if selectproducts == "1" or selectproducts == "Computer":
        amount = int(input("จำนวนสินค้าที่ต้องการ : "))
        totalprice = computerprice*amount
        print(  "--------------------------------------\n"
                "Total Price :",totalprice,"\n"
                "----------------Thank you-------------\n"
                "--------------------------------------")
    elif selectproducts == "2" or selectproducts == "Laptop":
        amount = int(input("จำนวนสินค้าที่ต้องการ : "))
        totalprice = laptopprice*amount
        print(  "--------------------------------------\n"
                "Total Price :",totalprice,"\n"
                "----------------Thank you-------------\n"
                "--------------------------------------")
    elif selectproducts == "3" or selectproducts == "Iphone xs":
        amount = int(input("จำนวนสินค้าที่ต้องการ(*ซื้อ2เครื่องขึ้นไปรับส่วนลด 1000 บาท) : "))
        totalprice = iphonexsprice * amount
        if amount == 1:
            print(  "--------------------------------------\n"
                "Total Price :",totalprice,"\n"
                "----------------Thank you-------------\n"
                "--------------------------------------")
        elif amount >= 2:
            totalprice -= 1000
            print("--------------------------------------\n"
                "Total Price :", totalprice, "\n"
                "----------------Thank you-------------\n"
                "--------------------------------------")
    else:
        print("ไม่มีสินค้าที่ท่านเลือก")
else :
    print("Username หรือ Password ผิด!!")




