import math

def main():
    # Input
    x = float(input("Masukkan nilai x: "))
    
    # Perhitungan
    y = (3*x**3 - 2*x**2 + 3*x - 1) / (4*x**2 + 2*x + 1)

    # Output
    print("x =", x)
    print("y =", y)

if __name__ == "__main__":
    main()