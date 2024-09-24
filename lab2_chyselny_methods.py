import math

a = 0.1
b = 16.0
e = 0.01
h = 0.1

def calculate_value(x):
    return math.log(x) + x

def find_interval(a, h):
    fa = calculate_value(a)
    b = a + h
    fb = calculate_value(b)

    while fa * fb > 0 and b <= 16.0:
        a = b
        fa = fb
        b = a + h
        fb = calculate_value(b)

    return a, b

def find_root(a, b, e):
    while True:
        x = (a + b) / 2.0
        fa = calculate_value(a)
        fx = calculate_value(x)

        if abs(fx) < e:
            return x

        if fa * fx > 0:
            a = x
        else:
            b = x

def main():
    global a, b
    a, b = find_interval(a, h)

    if calculate_value(a) * calculate_value(b) <= 0:
        result = find_root(a, b, e)
        print("\n\n", result)
    else:
        print("Root not found")

if __name__ == "__main__":
    main()
