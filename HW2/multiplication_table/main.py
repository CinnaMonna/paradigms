def print_table(n: int) -> None:
    for a in range (1, int(n) + 1):
        for b in range (1, 10):
            print("{} * {} = {}".format(a, b, a * b))
        print("\n")

def is_correct_input(value) -> None:
    try:
        int(value)
        if int(value) < 1 or int(value) > 9:
            raise ValueError
    except ValueError:
        print("Integer input in range 1 <= n <= 9 is expected")
        raise

def main():
    n = input("Input integer number n in range 1 <= n <= 9:\n")
    is_correct_input(n) 
    print_table(n)

if __name__ == "__main__":
    main()

