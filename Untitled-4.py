def calculate_sum_and_average(numbers):
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average

def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(float, user_input.split()))
    
    total, average = calculate_sum_and_average(numbers)
    
    print(f"Sum: {total}")
    print(f"Average: {average}")

if __name__ == "__main__":
    main()
