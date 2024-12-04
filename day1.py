# read in data

data = open('input/day1.txt', 'r').read().split('\n')

# part 1

# split into two lists, convert to int, sort

list_a, list_b = sorted([int(i.split()[0]) for i in data]),\
                 sorted([int(i.split()[1]) for i in data])

# zip over lists and get dist, sum

diff = 0

for a,b in zip(list_a, list_b):
    
    diff += abs(a-b)
    
# part 2

# loop over values in list a

sim_score = 0

for value in list_a:
    
    # check freq in list b
    
    freq = list_b.count(value)

    # calc figure to add to similarity score
    
    sim_score += value * freq
