import division
while True:
    try:
        son1 = int(input("1-sonni kiriting: "))
        son2 = int(input("2-sonni kiriting: "))
        bolinma = division.sonlar(son1, son2)
        print(bolinma)
        break
    except ZeroDivisionError:
        print("Sonni 0 ga bo'lib bo'lmaydi!")
        continue
