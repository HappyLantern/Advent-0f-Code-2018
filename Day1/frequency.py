frequencies = open('input.txt')
output = open("output.txt", 'w')


# PART 1


freq_sum = sum([int(freq) for freq in frequencies])
print(freq_sum)
output.write(str(freq_sum))
frequencies.seek(0)

#PART 2

#Testdata
test_input_1 = ['+1', '-1']
test_input_2 = ['+3', '+3', '+4', '-2', '-4']
test_input_3 = ['-6', '+3', '+8', '+5', '-6']
test_input_4 = ['+7', '+7', '-2', '-7', '-4']

freq_current = 0
freq_list = [0]
not_finished = 1
while not_finished :
    for freq in frequencies:
        freq_current += int(freq)
        freq_list.append(freq_current)
        #print(set(freq_list).symmetric_difference(freq_list))
        if len(freq_list) != len(set(freq_list)):
            not_finished = 0
            break
    frequencies.seek(0)

print(freq_list[-1])
