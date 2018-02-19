money=input("How much money you have?")
number_of_iphone=money/50000
print("You can buy",number_of_iphone,"iphone")

if money <50000:
    print("You will need",50000-money,"to afford an iphone")
if money >50000:
    print("You will need",50000-(money%50000),"to afford an additional iphone")
