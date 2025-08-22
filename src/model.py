def load_weights(filename="src/thetas.txt"):
    with open(filename, "r") as f:
        return list(map(float, f.read().strip().split(",")))


theta0, theta1 = load_weights()

if __name__ == "__main__":
    mileage = int(input("enter car mileage in KM to predict it's price: "))

    price = theta0 + theta1 * mileage
    print(f"the price of the car is ~ {price}")
