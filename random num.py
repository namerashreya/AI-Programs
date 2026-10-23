#generate num

import random
while True:
    
    a=random.randint(1,10)
    print(a)
    num=int(input("enter a num:"))

    if num==a:
        print("match")
    else:
        print("not match")

    choice = input("Do you want to continue? (yes/no): ").strip().lower()
    if choice != "yes":
        print("Thanks for playing!")
        break


        
