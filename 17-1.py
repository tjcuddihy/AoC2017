STEPS = 370

curr_list = [0]
curr_pos = 0
for i in range(1,2018):
    curr_pos = (curr_pos + STEPS + 1)%i
    curr_list.insert(curr_pos, i)


index2017 = curr_list.index(2017)
print(curr_list[index2017-1:index2017+3])