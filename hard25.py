def find_special_numbers(d1_start, d1_end, d2_start, d2_end):

    divisor_counts = {}

    for num in range(d1_start, d1_end + 1):
        for divisor in range(d2_start, d2_end + 1):
            if num % divisor == 0:
                if divisor not in divisor_counts:
                    divisor_counts[divisor] = 0
                divisor_counts[divisor] += 1

    sorted_divisors = sorted(divisor_counts.items(), key=lambda x: (x[1], x[0]))

    top_special_numbers = sorted_divisors[-3:]

    return [(num, count) for num, count in top_special_numbers]


d1_start, d1_end = 150689, 170899
d2_start, d2_end = 550, 6289

result = find_special_numbers(d1_start, d1_end, d2_start, d2_end)
for number, count in result:
    print(number, count)
