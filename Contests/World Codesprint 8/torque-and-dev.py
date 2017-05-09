def read_input(n,m):
    land={city:set() for city in range(1,n+1)}
    for a1 in range(m):
        city_1,city_2 = map(int,input().split())
        land[city_1].add(city_2)
    return land

q = int(input().strip())
for a0 in range(q):
    n,m,clib,croad = map(int,input().split())
    land = read_input(n,m)
    #find disconnected graphs

    un_cities = set([i+1 for i in range(n)])
    subgraphs = []

    #traverse
    while un_cities:
        print (un_cities)
        temp=un_cities.pop()
        cities=land[temp]
        if not cities:
            land[temp]=set()
            continue
        else:
            count=1
            nun_cities=cities
            while nun_cities:
                city=nun_cities.pop()
                un_cities.discard(city)
                count+=1
                new_cities = land[city].intersection(un_cities)
                print (city,new_cities)
                nun_cities.update(new_cities)

            subgraphs.append(count)

    #calulate min cost
    print (min(clib*n,sum[croad*(i-1)+clib for i in subgraphs]))
