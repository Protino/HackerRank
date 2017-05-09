import copy
import traceback

def checkWinner(plies):
    moves=[]
    parts=1
    for key,value in plies.items():
        for num in S:
            if key%num==0:
                parts=value
                moves.append([key,num])
    return (moves,(parts%2==0))
        

def solve(plies,player,opp):
    temp_plies=copy.deepcopy(plies)
    result = checkWinner(plies)
    if len(result[0])<2:
        return player if result[1] else opp
    moves = result[0]
    print ('moves',moves)
    for move in moves:
        num,divider=move[0],move[1]
        plies[num]-=1
        if plies[num]==0:
            plies.pop(num)
        if num//divider!=1:
            plies[num//divider]=divider
        if not plies:
            plies=copy.deepcopy(temp_plies)
            continue
        '''
        result = checkWinner(plies)
        if len(result[0])<2:
            return opp if result[1] else player
        '''
        winner=solve(plies,opp,player)
        if winner!=player:
            plies=copy.deepcopy(temp_plies)
        else:
            return winner
    return opp
    
for __ in range(int(input())):
    n,m=map(int,input().split())
    S=set(map(int,input().split()))
    plies=dict()
    plies[n]=1
    print (solve(plies,'f','s'))
        
    
