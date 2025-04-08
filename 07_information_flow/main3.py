def in_range(n, low, high):
    """ Returns True if n is between low and high, inclusive. """
    return low <= n <= high


def main():
    n = int(input("Enter the number to check: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    result = in_range(n, low, high)
    print(result)  # This will print True or False

    # Optional: More explanation if you want
    if result:
        print(f"{n} is in the range [{low}, {high}].")
    else:
        print(f"{n} is NOT in the range [{low}, {high}].")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
