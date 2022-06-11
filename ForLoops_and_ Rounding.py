# x = round (5.782937456,2)
#print(x)



#for x in "Toronto":
    #print(x)



"""
x = ["pen", "pencil", "bottle"]

for y in x:
    print(y)
    if y == "pencil":

        break """



prices = [3.44, 9.99, 2.50, 20.00]
total = 0
for price in prices:
    print("Item costs $", price)
    total = total+price
print("shopping total", round(total, 2))