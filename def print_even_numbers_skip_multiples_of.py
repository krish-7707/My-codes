def print_even_numbers_skip_multiples_of_8():
    for number in range(1, 51):
        if number % 2 == 0:
            if number % 8 == 0:
                continue
            print(number)

if __name__ == "__main__":
    print_even_numbers_skip_multiples_of_8()
