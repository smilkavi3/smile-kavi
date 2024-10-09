# notes counting program:
amount=int(input("Enter amount"))
rs2000=0
rs500=0
rs200=0
rs100=0
rs50=0
rs10=0
rs5=0
rs2=0
rs1=0


if amount >= 2000:
    rs2000=amount//2000
    amount%=2000
    print("Two thousand",rs2000)
if amount>=500:
    rs500=amount//500
    amount%=500
    print("Five hundred",rs500)
if amount>=100:
    rs100=amount//100
    amount%=100
    print("Hundred",rs100)
if amount>=50:
    rs50=amount//50
    amount%=50
    print("Fifty ",rs50)
if amount>=10:
    rs10=amount//10
    amount%=10
    print("Ten",rs10)
if amount>=5:
    rs5=amount//5
    amount%=5
    print("Five",rs5)
if amount>=2:
    rs2=amount//2
    amount%=2
    print("Two",rs2)
if amount>=1:
   rs1=amount//1
   amount%=1
   print("One",rs1)
                            

                    
# calculate electricity bill:
u=int(input("Enter units"))
if(u<=50):
    amount=50*0.50
    total=amount*.20
    print("frist 50 units Rs",amount)
elif(u<=100):
    amount=100*0.75+ 50*0.50
    total=amount*.20
    print("Next 100 unts Rs",amount)
elif(u<=150):
    amount=100*1.20+100*0.75+50*0.50
    total=amount*.20
    print("Next 150 unit Rs",amount)
elif(u<=250):
    amount=250*1.50+100*1.20+100*0.75+50*0.50
    total=amount*.20
    print("Next 250 units Rs",total)






