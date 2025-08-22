import statistics as sts


def parse_csv(filename="src/data/data.csv") -> list[int]:
    with open(filename, "r") as f:
        data = f.read()
        data = list(
            map(
                int,
                data.replace("km,price\n", "", 1).strip().replace("\n", ",").split(","),
            )
        )
        return [
            [data[idx] for idx in range(0, len(data), 2)],
            [data[idx + 1] for idx in range(0, len(data), 2)],
        ]


x, y = parse_csv()

theta0, theta1 = 0.0, 0.0

x_mean, x_std = sts.mean(x), sts.stdev(x)
y_mean, y_std = sts.mean(y), sts.stdev(y)

x_scaled = [(xi - x_mean) / x_std for xi in x]
y_scaled = [(yi - y_mean) / y_std for yi in y]

alpha = 0.01
epochs = 500

m = len(x)

for _ in range(epochs):
    y_pred = [theta0 + theta1 * xi for xi in x_scaled]
    errors = [yp - yi for yp, yi in zip(y_pred, y_scaled)]

    dtheta0 = (2 / m) * sum(errors)
    dtheta1 = (2 / m) * sum(e * xi for e, xi in zip(errors, x_scaled))

    theta0 -= alpha * dtheta0
    theta1 -= alpha * dtheta1

b = theta1 * (y_std / x_std)
a = y_mean + (theta0 * y_std) - b * x_mean


def save_thetas(filename="src/thetas.txt"):
    with open(filename, "w+") as f:
        f.write(f"{a},{b}")
        print(f"results are saved in {filename}")


print(f"θ0 (intercept) = {a:.4f}")
print(f"θ1 (slope)     = {b:.4f}")

save_thetas()
