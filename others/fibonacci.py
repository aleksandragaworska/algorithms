
def fibonacci_sequence(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)
