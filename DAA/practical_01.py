"""DAA Practical 1: Fibonacci numbers (recursive and non-recursive) with step count."""
import sys

steps = 0  # global step counter used by the recursive version


def fib_recursive(n):
    """Recursive Fibonacci. Every call counts as one step. Time O(2^n), space O(n)."""
    global steps
    steps += 1
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    """Non-recursive Fibonacci. Returns (value, step_count). Time O(n), space O(1)."""
    count = 1  # the initial check
    if n <= 1:
        return n, count
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
        count += 1  # one step per loop pass
    return b, count


def read_n():
    text = input("Enter n (non-negative integer, press Enter for 10): ").strip()
    if text == "":
        return 10
    try:
        n = int(text)
    except ValueError:
        print("Invalid input: please enter a whole number.")
        sys.exit(1)
    if n < 0:
        print("Invalid input: n must be >= 0.")
        sys.exit(1)
    if n > 35:
        print("n > 35 makes the recursive version very slow. Use n <= 35.")
        sys.exit(1)
    return n


def main():
    global steps
    n = read_n()
    print(f"\nFibonacci series up to n = {n}: ", end="")
    print([fib_iterative(i)[0] for i in range(n + 1)])

    steps = 0
    r = fib_recursive(n)
    rec_steps = steps
    i, it_steps = fib_iterative(n)

    print(f"\n{'Method':<14}{'F(n)':<12}{'Step count':<12}{'Time':<10}{'Space'}")
    print(f"{'Recursive':<14}{r:<12}{rec_steps:<12}{'O(2^n)':<10}O(n) (call stack)")
    print(f"{'Non-recursive':<14}{i:<12}{it_steps:<12}{'O(n)':<10}O(1)")

    print("\nStep count growth (recursive vs non-recursive):")
    print(f"{'n':<5}{'recursive':<12}{'non-recursive'}")
    for k in range(5, min(n, 30) + 1, 5):
        steps = 0
        fib_recursive(k)
        print(f"{k:<5}{steps:<12}{fib_iterative(k)[1]}")


if __name__ == "__main__":
    main()
