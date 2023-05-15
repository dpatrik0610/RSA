import math

def quick_pow(base: int, exp: int, mod: int) -> int:
    #print(f"{base}^{exp} mod {mod}:")
    exp_of_two = exponents_of_two(exp)
    #print(f"{exp} = " + " + ".join(["2^" + str(n) for n in exp_of_two]))

    step = base % mod
    partial_results = [step]
    for i in range(max(exp_of_two)):
        step = (step ** 2) % mod
        partial_results.append(step)

    productum = 1
    for i in exp_of_two:
        productum *= partial_results[i]
    final_result = productum % mod
    return final_result

def exponents_of_two(number: int):
    return [i for i in range(number.bit_length()) if number & (1 << i)]

def extended_euclidean(x: int, y: int):
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    step = 0
    while y:
        step += 1
        quotient, remainder = divmod(x, y)
        x, y = y, remainder

        x_next = x1 * quotient + x0
        y_next = y1 * quotient + y0

        x0, x1 = x1, x_next
        y0, y1 = y1, y_next

    if step % 2 == 0:
        return x0, -y0
    else:
        return -x0, y0
