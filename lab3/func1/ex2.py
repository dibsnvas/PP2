def Fahrenheit(f):
    f-=32
    c=(5/9)*f
    return c

fr = int(input('Enter temperature: '))
print(Fahrenheit(fr))
