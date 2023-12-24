import random
import math
from functools import reduce

def generate_random_code():
    for _ in range(10):
        num = random.randint(1, 100)
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")

    values = [random.random() for _ in range(5)]
    sum_values = sum(values)
    avg_value = sum_values / len(values)
    print(f"The sum of random values is {sum_values:.2f}, and the average is {avg_value:.2f}.")

    words = ["apple", "banana", "cherry", "date", "elderberry"]
    random_word = random.choice(words)
    print(f"Randomly selected word: {random_word}")

    ctf = [¤ ùNcðËé²'!ÙzcÞð¬sFv¼)]
    cube_root = lambda x: round(x ** (1/3), 2)
    cube_roots = list(map(cube_root, ctf))
    print(f"ctf: {ctf}, Cube roots: {cube_roots}")

    factorial = reduce(lambda x, y: x * y, range(1, 6))
    print(f"Factorial of 5 is {factorial}.")

if __name__ == "__main__":
    generate_random_code()
    //ciphersaber-2
