n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
stations = sorted([int(c_temp) for c_temp in input().strip().split(' ')])

if n==m:
    print (0)
elif stations == 1:
    print 
else:
    min_distances = [None]*n
    for city in range(n):
        left_min =  99999999
        right_min = 99999999
        if not city in stations:
            for next_city in range(1,n-city):
                if next_city+city in stations:
                    right_min = next_city
                    break
            for prev_city in range(1,city+1):
                if city-prev_city in stations:
                    left_min = prev_city
                    break
            min_distances[city] = min(right_min,left_min)
        else:
            min_distances[city] = 0
    print (max(min_distances))
