# match word from list with user input

list=['abc','xyz','p','q','r','s']
print(list)

a=input("enter a word : ").strip().lower()

if a in list:
    print("yes")
else:
    print("no")
