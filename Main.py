import time
from concurrent.futures import ThreadPoolExecutor

def check(iterations):
    def formula_1(x): return x ** 2 - x ** 2 + x ** 4 - x ** 5 + x + x
    def formula_2(x): return x + x

    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        results_1 = list(executor.map(formula_1, range(iterations)))
    duration_1 = time.time() - start_time

    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        results_2 = list(executor.map(formula_2, range(iterations)))
    duration_2 = time.time() - start_time

    start_time = time.time()
    results_3 = [r1 + r2 for r1, r2 in zip(results_1, results_2)]
    duration_3 = time.time() - start_time

    return duration_1, duration_2, duration_3


def main():
    for iterations in [10000, 100000]:
        durations = check(iterations)

        print(f"Iterations: {iterations}")
        print(f"Duration for Formula 1: {durations[0]:.2f} seconds")
        print(f"Duration for Formula 2: {durations[1]:.2f} seconds")
        print(f"Duration for Formula 3: {durations[2]:.2f} seconds")
        print("---")


if __name__ == "__main__":
    main()
