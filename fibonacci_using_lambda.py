def fibonacci_of_number(count):
    value = [0, 1]
    any(map(lambda _: value.append(sum(value[-2:])), range(2, count)))
    return value[:count]
print(fibonacci_of_number(15))
