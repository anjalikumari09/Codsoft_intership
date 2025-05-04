print("******CALCULATOR******")

num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
choice=input("Choose the operator(+,-,*,/,%,//):")
if(choice=="+"):
    sum=num1+num2
    print("The sum of",num1,"and",num2,"is equal to",sum)
elif(choice=="-"):
    sub=num1-num2
    print("The difference of",num1,"and",num2,"is equal to",sub)
elif(choice=="*"):
    prod=num1*num2
    print("The product of",num1,"and",num2,"is equal to",prod)
elif(choice=="/"):
    div=num1/num2
    print("The division of",num1,"and",num2,"is equal to",div)
elif(choice=="%"):
    mod=num1%num2
    print("The remainder of",num1,"and",num2,"is equal to",mod)
elif(choice=="//"):
    fd=num1//num2
    print("The floor division value of",num1,"and",num2,"is equal to",fd)
else:
    print("Invalid operator!")
    