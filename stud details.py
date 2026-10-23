'''take input such as name, perc in 12grage if less then one range give msg please reappear for the exam, stream sci,commer,arts.
area of studemt's  intrest. suggest courses.(with if else)'''

'''name = input("Enter student's name: ")
stream = input("Enter stream (science/commerce/arts): ").lower()
perc = float(input("Enter 12th percentage: "))

print("\nStudent Name:", name)
print("Percentage:", perc)
print("Stream:", stream)

if perc < 40:
    print("Please reappear for the exam.")

elif stream == "science":
    if perc >= 80:
        print("You can do: MBBS, B.Tech, B.Sc, BCA")
    elif perc >= 60:
        print("You can do: B.Tech, B.Sc, BCA")
    else:
        print("You can do: B.Sc, BCA")

elif stream == "commerce":
    if perc >= 80:
        print("You can do: CA, B.Com, BBA")
    elif perc >= 60:
        print("You can do: B.Com, BBA")
    else:
        print("You can do: B.Com")

elif stream == "arts":
    if perc >= 80:
        print("You can do: BA, LLB, BJMC")
    elif perc >= 60:
        print("You can do: BA, BSW, BJMC")
    else:
        print("You can do: BA, BSW")

else:
    print("Invalid stream.")'''

name = input("Enter student's name: ")
stream = input("Enter stream (science/commerce/arts): ").lower()
perc = float(input("Enter 12th percentage: "))
interest = input("Enter your interest (computer/medical/accounting/business/law/design): ").lower()

print("\nStudent Name:", name)
print("Stream:", stream)
print("Percentage:", perc)
print("Interest:", interest)

if perc < 40:
    print("Please reappear for the exam.")

elif stream == "science":

    if interest == "computer":
        print("Your interest matches your stream.")
        print("Suggested courses: BCA, B.Tech Computer Science")

    elif interest == "medical":
        print("Your interest matches your stream.")
        print("Suggested courses: MBBS, B.Pharm, Nursing")

    elif interest == "maths":
        print("Your interest matches your stream.")
        print("Suggested courses: B.Sc Mathematics, B.Tech")

    else:
        print("You did Science, but your interest does not match the Science courses.")
        print("Please choose a course related to your stream.")

elif stream == "commerce":

    if interest == "accounting":
        print("Your interest matches your stream.")
        print("Suggested courses: B.Com, CA, CMA")

    elif interest == "business":
        print("Your interest matches your stream.")
        print("Suggested courses: BBA, B.Com")

    elif interest == "finance":
        print("Your interest matches your stream.")
        print("Suggested courses: B.Com, BBA Finance")

    else:
        print("You did Commerce, but your interest does not match the Commerce courses.")
        print("Please choose a course related to your stream.")

elif stream == "arts":

    if interest == "law":
        print("Your interest matches your stream.")
        print("Suggested courses: LLB, BA LLB")

    elif interest == "design":
        print("Your interest matches your stream.")
        print("Suggested courses: B.Des, Fine Arts")

    elif interest == "teaching":
        print("Your interest matches your stream.")
        print("Suggested courses: BA, B.Ed")

    else:
        print("You did Arts, but your interest does not match the Arts courses.")
        print("Please choose a course related to your stream.")

else:
    print("Invalid stream.")
