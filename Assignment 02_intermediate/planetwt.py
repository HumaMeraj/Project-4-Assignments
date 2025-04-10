# Gravitational constants
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14


def main():
    # Step 1: Get Earth weight from user
    earth_weight = float(input("Enter a weight on Earth: "))

    # Step 2: Get planet name
    planet = input("Enter a planet: ")

    # Step 3: Select correct gravity constant
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        # If it's not any of the above, default to Neptune
        gravity_constant = NEPTUNE_GRAVITY

    # Step 4: Calculate and print result
    planetary_weight = earth_weight * gravity_constant
    rounded_planetary_weight = round(planetary_weight, 2)
    print("The equivalent weight on " + planet + ": " + str
          (rounded_planetary_weight))

# Standard entry point


if __name__ == "__main__":
    main()
