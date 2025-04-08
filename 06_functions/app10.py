def print_ones_digit(num):
    ones_digit = abs(num) % 10  # abs() to handle negative numbers
    print("The ones digit is", ones_digit)


def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
