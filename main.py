import sys

from calculator import calculator


def main():
    print(f"Hello from Python {sys.version}")
    print("Project initialized successfully!")


if __name__ == "__main__":
    main()

    my_list = [1, 2, 3, 4, 5]

    print(calculator(10, 2, "+"))
    print(calculator(10, 2, "-"))
    print(calculator(10, 2, "*"))
    print(calculator(10, 2, "/"))
    print(calculator(10, 2, "%"))
    print(calculator(10, 2, "sqrt"))
