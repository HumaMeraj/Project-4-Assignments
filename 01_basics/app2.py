def main():
    # User se number input lena
    curr_value = int(input("Enter a number: "))

    # Jab tak number 100 se chhota hai, tab tak usse double karte raho
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")  # Saath-saath print karein same line mein

# Yeh line zaroori hai taake main() function run ho jab program start ho
if __name__ == '__main__':
    main()
