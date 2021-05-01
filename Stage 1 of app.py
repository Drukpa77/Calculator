# Stage 1 of unit converter

num1 = input('Enter the value: ')
print("list of units:cm, m, km, mm")
unit1 = input('First Unit Input:  ')
unit2 = input('Second Unit Input: ')

if unit1 == "cm" and unit2 == "m":
    ans = float(num1)/100
    print(ans)
elif unit1 == "mm" and unit2 == "cm":
    ans = float(num1)/10
    print(ans)
elif unit1 == "m" and unit2 == "cm":
    ans = float(num1)*100
    print(ans)
elif unit1 == "cm" and unit2 == "mm":
    ans = float(num1)*10
    print(ans)
elif unit1 == "mm" and unit2 == "m":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "m" and unit2 == "mm":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "km" and unit2 == "m":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "m" and unit2 == "km":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "mm" and unit2 == "km":
    ans = float(num1)/1000000
    print(ans)
