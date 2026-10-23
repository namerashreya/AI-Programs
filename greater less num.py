#take input drom user and match weather
#num is greate or lesss than generated num it continue when the both num is same

#generate num

import random

a=random.randint(1,10)

while True:
    
   
    num=int(input("enter a num:"))

    if num>a:
        print("greater")
    elif num <a:
        print("less")
    else:
        print("correct")
        break


        
