import math

def correlation_coeff(x_list: list, y_list: list) -> float:
    x_avg = (sum(x_list)) / len(x_list)
    y_avg = (sum(y_list)) / len(y_list)

    r_xy = sum(map(lambda x, y: (x - x_avg) * (y - y_avg), x_list, y_list)) \
        / math.sqrt(sum(map(lambda x: (x - x_avg) ** 2, x_list)) * sum(map(lambda y: (y - y_avg) ** 2, y_list)))

    return r_xy

x = [1, 4, 5, 0]
y = [3, 6, 9, 7]

print(correlation_coeff(x, y))