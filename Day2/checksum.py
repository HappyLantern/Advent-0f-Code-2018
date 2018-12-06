import re

def char_frequency(str):
    dict = {}
    for s in str:
        if s in dict.keys():
            dict[s] += 1
        else:
            dict[s] = 1
    dict.pop('\n') # Not needed
    return dict

def word_diff(one, two):
    temp = "".join(one)
    difference = 0
    for i in range(len(one)):
        if one[i] != two[i]:
            difference = difference + 1
            temp = re.sub(one[i], '', temp) # Remove the char.
    if difference is 1: # If only one char removed, answer found.
        return temp
    else:
        return ""

box_list = open('input.txt')

# Part 1

two_count = 0
three_count = 0
word_list = []

for box_id in box_list:
    word_freq = char_frequency(box_id)
    word_list.append(list(box_id.strip())) #For part 2
    if 2 in word_freq.values():
        two_count = two_count + 1
    if 3 in word_freq.values():
        three_count = three_count + 1

checksum = two_count * three_count
print(checksum)
box_list.seek(0)

# Part 2

common_letters = ""
for word_one in word_list:
    for word_two in word_list:
        if word_one == word_two:
            continue
        common_letters = word_diff(word_one, word_two)
        if common_letters is not "":
            break
    if common_letters is not "":
        print("Common letters: " + common_letters)
        print("ID one: " + "".join(word_one))
        print("ID two: " + "".join(word_two))
        break

output = open('output.txt', 'w')
output.write("Part one: " + str(checksum))
output.write("\nPart two: " + common_letters)
output.close()
