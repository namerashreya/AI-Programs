s1=int(input("enter mark of sub1:"))
s2=int(input("enter mark of sub2:"))
s3=int(input("enter mark of sub3:"))
s4=int(input("enter mark of sub4:"))
s5=int(input("enter mark of sub5:"))

total=(s1+s2+s3+s4+s5)
print(total)

per=(total*100)/500
print(per)


if(s1>100 or s2>100 or s3>100 or s4>100 or s5>100 or s1<0 or s2<0 or s3<0 or s4<0 or s5<0):
    print("invalid marks")

elif(s1<23 or s2<23 or s3<23 or s4<23 or s5<23):
    print("fail")
else:
    if(per>90):
        print("A Grade")
    elif(per>70 and per <90):
        print("B Grade")
    elif(per >40 and per<70):
        print("C Grade")
    else :
        print("f garde")
    
