import re
input = open('input.txt')

# Part 1
# How many square inches of fabric are between two or more claims?


data = []
for claim in input:
    claim = re.findall('\d+', claim)
    data.append(claim)

data_test = data[:] # Start small :D

claim_count = {} # Increment claims for each inch.

for claim in data: # Each claim
    id = int(claim[0])
    start_x = int(claim[1])
    start_y = int(claim[2])
    width_x = int(claim[3])
    height_y = int(claim[4])
    for x in range(start_x, start_x + width_x): # Iterate each inch and increment counter for inch
        for y in range(start_y, start_y + height_y):
            if (x, y) in claim_count:
                claim_count[(x, y)] += 1
            else:
                claim_count[(x, y)] = 1

count = 0
for inch in claim_count: # Iterate all the inches and calc sum for 2 or more claims
    if claim_count[inch] >= 2:
        count += 1
print(count) # Answer for part 1

# Part 2
# What is the ID of the one claim that doesn't overlap?

overlaps = {}
id = -1
for claim in data:
    temp_id = int(claim[0])
    overlaps[temp_id] = False
    start_x = int(claim[1])
    start_y = int(claim[2])
    width_x = int(claim[3])
    height_y = int(claim[4])

    for x in range(start_x, start_x + width_x): # Iterate each inch and look at count
        for y in range(start_y, start_y + height_y):
            if claim_count[(x, y)] > 1:
                overlaps[temp_id] = True
                continue
    if overlaps[temp_id] is False:
        id = temp_id
        break
print(id)
