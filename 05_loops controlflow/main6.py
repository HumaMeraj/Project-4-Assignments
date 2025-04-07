def main():
    number = int(input("Enter a number: "))
    
    while number < 100:
        number *= 2
        print(number, end=" ")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
