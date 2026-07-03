x = "hello"
y = type(x)
print(y)

i = 2 + float(2)
j = type(i)
print(f"{i:.2f}, {j}")

m = 54 + int('123')
n = type(m)
print(f"{m:.1f}, {n}")

#Formatted floating point number
l = float('12.6') + 20
print(f"{l:.2f}, {type(l)}")

#Formatted string
nam = input("What is your name? ")
print(f"Hello, {nam}!")

nam = input("What is your name? ")
print('Hello,', nam , '!')
#Output multiple items in sequence, auto separated by space

Eur = input("What is the floor number in Europe? ")
print(type(Eur))   
Us = int(Eur) + 1
print(f"The floor number in the US is: {Us}!")

print('123'+'abc')
print('123','abc')