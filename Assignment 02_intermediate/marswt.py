# Constant for Mars gravity
MARS_MULTIPLE = 0.378


def main():
    # Step 1: Take weight input from user
    earth_weight_str = input("Enter a weight on Earth: ")

    # Step 2: Convert string input to float
    earth_weight = float(earth_weight_str)

    # Step 3: Calculate Mars weight
    mars_weight = earth_weight * MARS_MULTIPLE
    rounded_mars_weight = round(mars_weight, 2)

    # Step 4: Show the result
    print("The equivalent weight on Mars: " + str(rounded_mars_weight))

# Standard Python entry point


if __name__ == "__main__":
    main()
