# TASK2-CALCULATOR
a=int(input("ENTER NUMBER 1:"))
b=int(input("ENTER NUMBER 2:"))
print("CHOOSE THE OPERATION:")
print("ADD-+")
print("SUB- -")
print("MUL- *")
print("DIV- /")
print("MOD DIV-%")
print("INTEGER DIV-//")
op=input("ENTER THE OPERATION")
if(op=='+'):
    print("RESULT:",a+b)
if(op=='-'):
    print("RESULT:",a-b)
if(op=='*'):
    print("RESULT:",a*b)
if(op=='/'):
    print("RESULT:",a/b)
if(op=='%'):
    print("RESULT:",a%b)
if(op=='//'):
    print("RESULT:",a//b)
