n = int(input())
petals = [int(i) for i in input().split(" ")]

def has_average(i, j):
    # Returns whether the flowers between i and j (inclusive) has an "average flower"
    
    avg_petals = sum(petals[i:j + 1]) / (j - i + 1)
    if avg_petals != int(avg_petals): # Not an integer
        return False
        
    for index in range(i, j + 1):
        if petals[index] == avg_petals:
            return True
            
    return False
    

photos = 0
for i in range(n):
    for j in range(i, n):
        photos += has_average(i, j)
        
print(photos)