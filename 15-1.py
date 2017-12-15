SEED_A = 516
SEED_B = 190

FACTOR_A = 16807
FACTOR_B = 48271

DENOMINATOR = 2147483647

result_a = (SEED_A * FACTOR_A) % DENOMINATOR
result_b = (SEED_B * FACTOR_B) % DENOMINATOR

collector = 0
for i in range(40000000):
    if i%500000 == 0:
        print(i)
    if format(result_a, 'b')[-16:] == format(result_b, 'b')[-16:]:
        collector += 1
    result_a = (result_a * FACTOR_A) % DENOMINATOR
    result_b = (result_b * FACTOR_B) % DENOMINATOR 
    
print(collector)