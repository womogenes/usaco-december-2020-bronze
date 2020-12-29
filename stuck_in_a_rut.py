# Parse input

# Sort cows by north/east
north_cows = []
east_cows = []

n = int(input())
for i in range(n):
    line = input().split(" ")
    direction = line[0]
    x = int(line[1])
    y = int(line[2])
    
    if direction == "N":
        north_cows.append((x, y, i))
    
    else:
        east_cows.append((x, y, i))
        
        
# Sort the cows
north_cows.sort(key=lambda cow: cow[0])
east_cows.sort(key=lambda cow: cow[1])


# Where the cows stop
stops = [None] * n

for nc in north_cows:
    # We don't care about direction and index
    for ec in east_cows:
        if nc[0] > ec[0] and nc[1] < ec[1]:
            nc_to_travel = ec[1] - nc[1]
            ec_to_travel = nc[0] - ec[0]
            
            if nc_to_travel < ec_to_travel and stops[ec[2]] == None:
                stops[ec[2]] = (nc[0], ec[1])
                
            elif nc_to_travel > ec_to_travel and stops[ec[2]] == None:
                # This cow stops!
                stops[nc[2]] = (nc[0], ec[1])
                break

eaten = [-1] * n
for nc in north_cows:
    if stops[nc[2]] != None:
        eaten[nc[2]] = stops[nc[2]][1] - nc[1]
        
for ec in east_cows:
    if stops[ec[2]] != None:
        eaten[ec[2]] = stops[ec[2]][0] - ec[0]
        

for i in eaten:
    if i == -1:
        print("Infinity")
    else:
        print(i)