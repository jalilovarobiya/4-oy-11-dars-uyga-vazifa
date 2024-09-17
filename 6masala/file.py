try:
    with open("yangi.txt", "w") as file:
        file.write("Birinchi fayl")
        print("Faylga yozildi")
except Exception as e:
    print("Quyidagi xato yuz berdi.")
    print(f"{e}")