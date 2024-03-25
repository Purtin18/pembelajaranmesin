def main():
    # Input from the user
    a = 8
    b = 12
    a = float(input("Masukkan nilai a dalam float: "))
    b = float(input("Masukkan nilai b dalam float: "))

    # Addition
    addition = a + b

    # Subtraction
    subtraction = a - b

    # Multiplication
    multiplication = a * b

    # Division
    division = a / b if b != 0 else "Tidak dapat dibagi (b bukan nol)"

    # Output
    print("\nHasil penambahan:", addition)
    print("Hasil pengurangan:", subtraction)
    print("Hasil perkalian:", multiplication)
    print("Hasil pembagian:", division)

    print("\nYeahhhh")

if __name__ == "__main__":
    main()