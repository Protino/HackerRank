col, row = map(int,input().split())
prev_row = [int(x) for x in input().split()]
if row<10000:
    for i in range(row-1):
        new_row = [prev_row[j] ^ prev_row[j+1] for j in range(0,col-1)]
        new_row.append(prev_row[0] ^ prev_row[col-1])
        prev_row = new_row
        print (i+1,prev_row)
    result = ' '.join(map(str,prev_row))
    print (result)
else:
    base = row.bit_length()-1
    while (base):
        for i in range(base):
            new_row = [prev_row[j] ^ prev_row[j+1] for j in range(0,col-1)]
            new_row.append(prev_row[0] ^ prev_row[col-1])
            prev_row = new_row
        row=row-(2**base)
        base = row.bit_length()-1
        if base<=0:
            break
    result = ' '.join(map(str,prev_row))
    print (result)
    
'''
col, row = map(int,input().split())
prev_row = [int(x) for x in input().split()]
if not (col&(col-1)) and row>=col==0:
    print (' '.join('0'*col))
else:
    for __ in range(row-1):
        new_row = [prev_row[j] ^ prev_row[j+1] for j in range(0,col-1)]
        new_row.append(prev_row[0] ^ prev_row[col-1])
        prev_row = new_row
        print (prev_row)
print (*prev_row)
''' 
