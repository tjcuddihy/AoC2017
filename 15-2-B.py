SEED_A = 516
SEED_B = 190
# SEED_A = 65
# SEED_B = 8921
FACTOR_A = 16807
FACTOR_B = 48271
MULTIPLE_A = 4
MULTIPLE_B = 8
DENOMINATOR = 2147483647

result_a = (SEED_A * FACTOR_A) % DENOMINATOR
result_b = (SEED_B * FACTOR_B) % DENOMINATOR

a_list = []
b_list = []

def judge(res_a, res_b):
 return format(res_a, 'b')[-16:] == format(res_b, 'b')[-16:]

collector = 0
n_pairs = 0
i = 0

while n_pairs <= 5000000:
    if n_pairs % 100000 == 0:
        print('I:', i)
        print('n_pairs:', n_pairs)
        print('percent:', (n_pairs / 5000000) * 100)
    if result_b % MULTIPLE_B == 0:
        n_pairs += 1
        b_list.append(result_b)
    result_b = (result_b * FACTOR_B) % DENOMINATOR 
    i += 1
    
with open('15-2-B.txt', 'wt') as f:
    f.write(str(b_list))