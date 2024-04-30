def float_range(start: int, stop: int, step: float):
    while start<=stop:
        yield start
        start += step

for c in float_range(1, 10, 0.5):
    print(c)
