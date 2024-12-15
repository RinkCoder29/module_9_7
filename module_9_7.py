def is_prime(func):
    def wrapper(*args, **kwargs):
        num = func(*args, **kwargs)
        if num <= 1:
            print("составное")
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    print("составное")
                    break
            else:
                print("Простое число")
        return num
    return wrapper

@is_prime
def sum_three(num_1, num_2, num_3):
    return num_1 + num_2 + num_3

result = sum_three(2, 3, 6)
print(result)