num = int(input("Enter a no: "))
try:
    for i in range(1, num + 1):
        if i % 3 == 0 and num % 5 == 0:
            print("ByteRush")
        elif i % 3 == 0:
            print("Byte")
        elif i % 5 == 0:
            print("rush")
        else:
            print(i)
except ValueError:
    print("Enter a valid whole number")
