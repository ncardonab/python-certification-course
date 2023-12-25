def powers_of_2(n):
    power = 1
    for _ in range(n):
        yield power
        power *= 2

powers_of_2_iter = powers_of_2(8)

# for power_of_2 in powers_of_2_iter:
#     print(power_of_2)

# print([power_of_2 for power_of_2 in powers_of_2_iter])
print(dir( powers_of_2_iter ))
print(powers_of_2_iter.__iter__())
print(powers_of_2_iter)