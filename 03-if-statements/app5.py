import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100


def main():
    """
    Generates and prints N_NUMBERS random integers between
    MIN_VALUE and MAX_VALUE (inclusive).
    """
    for _ in range(N_NUMBERS):
        value = random.randint(MIN_VALUE, MAX_VALUE)
        print(value, end=" ")
    print()  # to move to the next line after printing all numbers


if __name__ == '__main__':
    main()
