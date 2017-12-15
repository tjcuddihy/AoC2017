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

# while n_pairs <= 5000000:
#     if n_pairs % 100000 == 0:
#         print('I:', i)
#         print('n_pairs:', n_pairs)
#         print('percent:', (n_pairs / 5000000) * 100)
#     if result_a % MULTIPLE_A == 0:
#         a_list.append(result_a)
#     if result_b % MULTIPLE_B == 0:
#         b_list.append(result_b)
#     if len(a_list) > 0 and len(b_list) > 0:
#         # print('I:', i)
#         n_pairs += 1
#         A, *a_list = a_list
#         B, *b_list = b_list
#         if judge(A, B):
#             collector += 1
#     result_a = (result_a * FACTOR_A) % DENOMINATOR
#     result_b = (result_b * FACTOR_B) % DENOMINATOR
#     i += 1

with open('15-2-A.txt', 'r') as f:
    a_list = f.read().strip('[').strip(']').split(',')
print('a_list:', len(a_list))
print(a_list[0])

with open('15-2-B.txt', 'r') as f:
    b_list = f.read().strip('[').strip(']').split(',')
print('b_list:', len(b_list))

for i in range(len(a_list)):
    if judge(int(a_list[i]), int(b_list[i])):
        collector += 1

print(collector)
