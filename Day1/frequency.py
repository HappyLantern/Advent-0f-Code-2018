frequencies = open('input.txt')
output = open("output.txt", 'w')

# freq_sum = 0
#
# for line in frequencies:
#
#     freq = line[1:]
#     if line[0] == '+':
#         freq_sum += int(freq)
#     else:
#         freq_sum -= int(freq)
#
# output.write(str(freq_sum))
# print(freq_sum)

# Comprehension

freq_list = [int(line[1:]) if line[0] == '+' else -1*int(line[1:]) for line in frequencies]
print(sum(freq_list))
output.write(str(sum(freq_list)))
