def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
print("select operation\n1.add\n2.sub\n3.mul")
se=input('select operation')
a=int(input('enter the number:'))
b=int(input('ente the number:'))
if se== '1': 
    print(a ,"+", b, "=", 
                    add(a,b)) 
  
elif se == '2': 
    print(a, "-", b, "=", sub(a, b))
 
elif se == '3': 
    print(a, "*", b, "=", mul(a, b))
else:
    print('invalid')
  
    
"""class name:
    def a(self):
        name=input('enter name:')
        age=input('enter age:')
        print("your name is:"+name,"and yourage is:"+age)
ob=name()
ob.a()"""
