import time


def is_prime(number: int) -> bool:
    """Return True when number is prime using simple trial division."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor_limit = int(number ** 0.5)
    for divisor in range(3, divisor_limit + 1, 2):
        if number % divisor == 0:
            return False
    return True


def find_primes_naive(limit: int):
    start = time.perf_counter()
    primes = []
    for number in range(limit + 1):
        if is_prime(number):
            primes.append(number)
    elapsed = time.perf_counter() - start
    return primes, elapsed


def find_primes_sieve(limit: int):
    start = time.perf_counter()
    if limit < 2:
        return [], 0.0

    is_prime_flag = [True] * (limit + 1)
    is_prime_flag[0] = False
    is_prime_flag[1] = False

    candidate = 2
    while candidate * candidate <= limit:
        if is_prime_flag[candidate]:
            multiple = candidate * candidate
            while multiple <= limit:
                is_prime_flag[multiple] = False
                multiple += candidate
        candidate += 1

    primes = [index for index, value in enumerate(is_prime_flag) if value]
    elapsed = time.perf_counter() - start
    return primes, elapsed


def _read_limit() -> int:
    user_text = input("Upper limit (default 10000): ").strip()
    if user_text == "":
        return 10000

    return int(user_text)


def main():
    print("Lab 3 - Prime Calculation")
    print("Finding all primes from 0 to 10,000")

    try:
        upper_limit = _read_limit()
    except ValueError:
        print("Invalid input. Using default limit: 10000")
        upper_limit = 10000

    upper_limit_float = float(upper_limit)

    primes_naive, time_naive = find_primes_naive(upper_limit)
    print("\nNaive trial division primes:")
    print(primes_naive)
    print(f"Naive runtime: {round(time_naive, 6)} seconds")

    primes_sieve, time_sieve = find_primes_sieve(upper_limit)
    print("\nSieve of Eratosthenes primes:")
    print(primes_sieve)
    print(f"Sieve runtime: {round(time_sieve, 6)} seconds")

    if time_sieve > 0:
        speed_ratio = round(float(time_naive / time_sieve), 3)
    else:
        speed_ratio = float("inf")

    print(f"\nExecution comparison up to {upper_limit_float:.0f}:")
    print(f"Naive total time: {round(time_naive, 6)} s")
    print(f"Sieve total time: {round(time_sieve, 6)} s")
    print(f"Sieve speed ratio (naive / sieve): {speed_ratio}x")

    if primes_naive != primes_sieve:
        print(
            "\nWarning: the two methods produced different results. "
            "Check implementation."
        )


if __name__ == "__main__":
    main()
