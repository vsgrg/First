string=str(input("Please enter a word:"))
result=string[::-1]
print(result)
if string == result:
    print("palindrome")
else:
    print("not palindrome")