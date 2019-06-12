fo=open(r"c:\python\student.txt","a")
while True:
    str1=input("enter text:")
    fo.write((str1+'\n'))
    choice=input("To exit type x:")
    if choice=='x' or choice=='X':
        break
    else:
        continue
fo.close()
print("work done")

    
