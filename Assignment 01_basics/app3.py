def main():
    # 10 se 1 tak countdown using a for loop
    for i in range(10, 0, -1):  # Start at 10, stop before 0, step -1
        print(i, end=" ")

    # After countdown, print Liftoff!
    print("Liftoff!")

# Required to run main function
if __name__ == '__main__':
    main()
