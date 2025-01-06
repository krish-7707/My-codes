def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

def main():
    temp = float(input("Enter the temperature: "))
    choice = input("Convert to (F)ahrenheit or (C)elsius? ").upper()

    if choice == 'F':
        converted = celsius_to_fahrenheit(temp)
        print(f"{temp} degrees Celsius is {converted} degrees Fahrenheit.")
    elif choice == 'C':
        converted = fahrenheit_to_celsius(temp)
        print(f"{temp} degrees Fahrenheit is {converted} degrees Celsius.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
