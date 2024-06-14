#simple Arithmetic operations using python
num1=float(input("Enter value 1:"))
num2=float(input("Enter value 2:"))
oper=input("choose operator:")
if(oper=='+'):
      print("Answer:", num1+num2)
elif(oper=='-'):
      print("subtraction:", num1-num2)
elif(oper=='*'):
      print("Multiplication:", num1 *num2)
elif(oper=='/'):
      print("Division:", num1/num2)
else:
       print("Enter valid operator:")