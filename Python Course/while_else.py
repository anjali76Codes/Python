p = 123
c = 0 
while c!=3:
   c =c+1
   pin= int(input("Enter your pin:"))
   if pin==p:
    print("Transaction is successful")
    break  
   else:
    print("Invalid pin")
else:
 print("Card is blocked")
   

