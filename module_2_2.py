fist=int(input("первое число "))
second=int(input("второе число "))
third=int(input("третье число "))
if fist==second==third:
    print(3)
elif fist==second or fist==third or second==third:
    print(2)
else:
    print(0)

