# Part 1
# How many units remain after fully reacting the polymer you scanned?
# a starts at 97 in ascii
# A starts at 65 in ascii
# Difference is 32

input = open('input.txt')
polymer_ref = input.read()

def react(str):
    entered_if = False
    for i in range(len(str) - 1):
        if ord(str[i]) == ord(str[i+1]) + 32 or ord(str[i]) + 32 == ord(str[i+1]):
             str = str[:i] + str[i+2:]
             entered_if = True
             return str, entered_if
    return str, entered_if

polymer = polymer_ref
polymer, reacted = react(polymer)
while reacted:
polymer, reacted = react(polymer)
polymer = polymer.rstrip() # Remove newline
print(len(polymer))        # Answer for part 1

# Part 2
# What is the length of the shortest polymer you can produce by removing all
# units of exactly one type and fully reacting the result?
polymer = polymer_ref
reacted_best = dict()
for i in range(26): # This solution takes redicilous amounts of time.
    lower   = chr(ord('a') + i) # a-z
    capital = chr(ord('A') + i) # A-Z
    polymer = polymer.replace(lower, '')
    polymer = polymer.replace(capital, '')
    polymer, reacted = react(polymer) # Do part 1 for each modification
    while reacted:
        polymer, reacted = react(polymer)
    reacted_best[lower + capital] = len(polymer).strip()
    polymer = polymer_ref

min_result = reacted_best[0] # Just an initial value
for key in reacted_best:
    if min_result > reacted_best[key]:
        min_result = reacted_best[key]
print(reacted_best) # Answer for part 2
