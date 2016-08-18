sea_level = 0
dummy = input()
steps = input()
valley_count = 0
gone_down_the_valley = False

for step in steps:
    if step == 'U':
        sea_level+=1
    else:
        sea_level-=1

    if sea_level < 0:
        gone_down_the_valley = True
        
    if gone_down_the_valley and sea_level == 0:
        valley_count+=1
        gone_down_the_valley = False

print (valley_count)
