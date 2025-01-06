def max_of_three(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    set1 = (3, 1, 2)
    set2 = (10, 30, 20)
    set3 = (-5, -10, 0)

    print(f"The maximum of {set1} is {max_of_three(*set1)}")
    print(f"The maximum of {set2} is {max_of_three(*set2)}")
    print(f"The maximum of {set3} is {max_of_three(*set3)}")

if __name__ == "__main__":
    main()
