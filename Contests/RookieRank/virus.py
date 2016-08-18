a,b,seconds = map(int,input().split())
growth = 0
cell_size = 1
for __ in range(seconds):
    cell_size = 0.5*a*cell_size + 0.5*b*cell_size

print (int(cell_size % (10**9 + 7)))
    
