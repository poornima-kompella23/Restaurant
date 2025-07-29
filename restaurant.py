print("🍜---WELCOME---🍜\nMENU:\nIDLY-100rs\nDOSA-150rs\nBAJJI-120rs\nUPMA-50rs\nPOORI-130rs\nCHAPATHI-180rs\n")
order=list(map(str,input("place your order:").split(" ")))
sum1=sum2=sum3=sum4=sum5=sum6=sum=bill=0
for i in range (len(order)):
    if order[i]=="IDLY":
        id=int(input("Enter how many plates of IDLY  you want:"))
        sum1=id*(sum1+100)
    if order[i]=="BAJJI":
        id=int(input("Enter how many plates of BAJJI  you want:"))
        sum2=id*(sum2+120)
    if order[i]=="DOSA":
        id=int(input("Enter how many plates of DOSA  you want:"))
        sum3=id*(sum3+150)
    if order[i]=="UPMA":
        id=int(input("Enter how many plates of UPMA  you want:"))
        sum4=id*(sum4+50)
    if order[i]=="POORI":
        id=int(input("Enter how many plates of POORI  you want:"))
        sum5=id*(sum5+130)
    if order[i]=="CHAPATHI":
        id=int(input("Enter how many plates of CHAPATHI  you want:"))
        sum6=id*(sum6+180)
sum=sum1+sum2+sum3+sum4+sum5+sum6
if sum>=500 and sum<750:
    r1=10/100
    bill=sum*r1
    o_bill=sum-bill
    print("TOTAL BILL:",sum)
    print("You have got 10% discout \nSo now your bill is:",o_bill)
elif sum>=750 and sum<1000:
    r2=20/100
    bill=sum*r2
    o_bill=sum-bill
    print("TOTAL BILL:",sum)
    print("You have got 20% discout \nSo now your bill is:",o_bill)
elif sum>=1000:
    r5=50/100
    bill=sum*r5
    o_bill=sum-bill
    print("TOTAL BILL:",sum)
    print("You have got 50% discout So now your bill is:",o_bill)
else:
    print("your bill is:",sum)
print("🙏THANKYOU🙏\n---VISIT AGAIN---")
