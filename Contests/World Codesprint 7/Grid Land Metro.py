from collections import defaultdict
from operator import itemgetter

n,m,k = map(int,input().split())
tracks = []

if k==0:
    print (n*m)
elif k==1:
    row,start,end = map(int,input().split())
    print (n*m-(end-start))
else:
    for __ in range(k):
        row,start,end = map(int,input().split())
        tracks.append([row,(start,end)])
    
    tracks = sorted(tracks,key=itemgetter(0))
    
    merged_tracks = defaultdict(list)
    for track in tracks:
        merged_tracks[track[0]]+=[track[1]]

    rows = sorted(merged_tracks)

    row_expected = 1
    free_space = n*m
    for row in rows:
        crazy_tracks = sorted(merged_tracks[row])
        valid_tracks = []
        for crazy_track in crazy_tracks:
            start = crazy_track[0]
            end = crazy_track[1]
            if not valid_tracks:
                valid_tracks.append((start,end))
                continue
            replaced=False
            for index in range(len(valid_tracks)):
                v_track = valid_tracks[index]
                v_start = v_track[0]
                v_end = v_track[1]
                if start<=v_start:
                    if end<=v_end and end>v_end:
                        valid_tracks[index]=(start,v_end)
                        replaced=True
                    elif end>=v_end:
                        valid_tracks[index]=(start,end)
                        replaced=True
                elif start>v_start and start <=v_end:
                    if end<=v_end:
                        replaced=True
                        continue
                    elif end>=v_end:
                        valid_tracks[index]=(v_start,end)
                        replaced=True
                        
            if not replaced:
                valid_tracks.append((start,end))

        #calculate free space
        space_taken=0
        print (valid_tracks)
        for track in valid_tracks:
            space_taken+=track[1]-track[0]+1
        free_space-=space_taken
            
    print (free_space)

'''
10 555555555 10
2 3 5
6 78 412
5 7 32
34 23 27
2 34 543
2 3433 32331
2 43242 23423423
1 32 2323
1 1 2342334
8 2342 23232342


10 7 5
2 1 3
3 1 7
9 3 5
9 2 4
2 5 6
'''
