from collections import defaultdict
import copy
import time

class Player:
    def __init__(self,color):
        self.color = color
        self.pieces = dict()
        self.minor_count = {'R':0,'B':0,'N':0}
    def addPiece(self,piece,pos):
        self.pieces[piece]=pos
        #print (piece[0])
        if piece[0] in self.minor_count:
            self.minor_count[piece[0]]+=1
    def printInfo(self):
        print (self.color,self.pieces)

def input_board():
    global w
    global b
    global m
    global white
    global black
    global board
    

    bishop_count = 0
    rook_count = 0
    pawn_count = 0
    knight_count = 0
    board = [['']*4 for __ in range(4)]
    white = Player('W')
    black = Player('B')
    try:
        s=input()
        w,b,m = map(int,s.split())
    except:
        print (s)
        
    for __ in range(w):
        piece, col, row = map(str,input().split())
        if col=='A':
            col=0
        elif col=='B':
            col=1
        elif col=='C':
            col=2
        else:
            col=3
        board[int(row)-1][col]=piece+'W'

        if piece == 'B':
            piece = 'B1' if bishop_count else 'B0'
            bishop_count+=1
        elif piece == 'R':
            piece = 'R1' if rook_count else 'R0'
            rook_count+=1
        elif piece == 'P':
            piece = 'P1' if pawn_count else 'P0'
            pawn_count+=1
        elif piece == 'N':
            piece = 'N1' if knight_count else 'N0'
            knight_count+=1
            
        white.addPiece(piece,(int(row)-1,col))
        
    bishop_count = 0
    pawn_count = 0
    rook_count = 0
    knight_count = 0
    for __ in range(b):
        piece, col, row = map(str,input().split())
        if col=='A':
            col=0
        elif col=='B':
            col=1
        elif col=='C':
            col=2
        else:
            col=3

        board[int(row)-1][col]=piece+'B'

        if piece == 'B':
            piece = 'B1' if bishop_count else 'B0'
            bishop_count+=1
        elif piece == 'P':
            piece = 'P1' if pawn_count else 'P0'
            pawn_count+=1
        elif piece == 'R':
            piece = 'R1' if rook_count else 'R0'
            rook_count+=1
        elif piece == 'N':
            piece = 'N1' if knight_count else 'N0'
            knight_count+=1
        black.addPiece(piece,(int(row)-1,col))

'''
Returns True, x,y if the player is under attack by opponent
else
False, -1 -1

Opti - check in this order - pawn, knight, bishop, rook or queen

'''

def under_attack(player,tboard):
    if 'Q' not in player.pieces:
        return True, (-1,-1)
        
    q_pos = player.pieces['Q']
    opp_player = 'W' if player.color == 'B' else 'B'

    #check for pawn_attack
    i,j = q_pos[0],q_pos[1]
    sides = ((i+1,j+1),(i+1,j-1)) if opp_player=='B' else ((i-1,j-1),(i-1,j+1))
    for side in (sides):
        i,j = side[0],side[1]
        if not (0<=i<4 and 0<=j<4):
            continue
        cur_piece = tboard[i][j]
        if cur_piece!='' and cur_piece[1]==opp_player:
            if cur_piece[0]=='P':
                return True, (side)    
    
    #check for row
    i,j = q_pos[0]+1,q_pos[1]
    while (0<=i<4):
        cur_piece = tboard[i][j]
        if cur_piece:
            #check if oppn player piece
            if cur_piece[1]==opp_player:
                if cur_piece[0]=='R' or cur_piece[0]=='Q':
                    return True, (i,j)
            break
        i+=1

    i,j = q_pos[0]-1,q_pos[1]
    while (0<=i<4):
        cur_piece = tboard[i][j]
        if cur_piece:
            #check if oppn player piece
            if cur_piece[1]==opp_player:
                if cur_piece[0]=='R' or cur_piece[0]=='Q':
                    return True, (i,j)
            break
        i-=1

    i,j = q_pos[0],q_pos[1]-1
    while (0<=j<4):
        cur_piece = tboard[i][j]
        if cur_piece:
            #check if oppn player piece
            if cur_piece[1]==opp_player:
                if cur_piece[0]=='R' or cur_piece[0]=='Q':
                    return True, (i,j)
            break
        j-=1
    i,j = q_pos[0],q_pos[1]+1
    while (0<=j<4):
        cur_piece = tboard[i][j]
        if cur_piece:
            #check if oppn player piece
            if cur_piece[1]==opp_player:
                if cur_piece[0]=='R' or cur_piece[0]=='Q':
                    return True, (i,j)
            break
        j+=1

    #check for north east diagonals
    i,j = q_pos[0]+1,q_pos[1]+1
    while (0<=i<4 and 0<=j<4):
        cur_piece = tboard[i][j]
        if cur_piece:
            #check if oppn player piece
            if cur_piece[1]==opp_player:
                if cur_piece[0]=='B' or cur_piece[0]=='Q':
                    return True, (i,j)
            break
        i+=1
        j+=1

    i,j = q_pos[0]+1,q_pos[1]-1
    while (0<=i<4 and 0<=j<4):
        cur_piece = tboard[i][j]
        if cur_piece:
            #check if oppn player piece
            if cur_piece[1]==opp_player:
                if cur_piece[0]=='B' or cur_piece[0]=='Q':
                    return True, (i,j)
            break
        i+=1
        j-=1

    i,j = q_pos[0]-1,q_pos[1]+1
    while (0<=i<4 and 0<=j<4):
        cur_piece = tboard[i][j]
        if cur_piece:
            #check if oppn player piece
            if cur_piece[1]==opp_player:
                if cur_piece[0]=='B' or cur_piece[0]=='Q':
                    return True, (i,j)
            break
        i-=1
        j+=1

    i,j = q_pos[0]-1,q_pos[1]-1
    while (0<=i<4 and 0<=j<4):
        cur_piece = tboard[i][j]
        if cur_piece:
            #check if oppn player piece
            if cur_piece[1]==opp_player:
                if cur_piece[0]=='B' or cur_piece[0]=='Q':
                    return True, (i,j)
            break
        i-=1
        j-=1

    #check for knights
    i,j = q_pos[0],q_pos[1]
    valid_pos = [(i-2,j-1),(i-2,j+1),(i+2,j-1),(i+2,j+1),(i-1,j-2),(i-1,j+2),(i+1,j-2),(i+1,j+2)]
    while valid_pos:
        i,j = valid_pos.pop()
        if (0<=i<4 and 0<=j<4):
            if tboard[i][j]=='N'+opp_player:
                return True, (i,j)
    return False, (-1,-1)

'''
Special moves here - promotion moves
# capture and promote
= straight promotion

'''
def pawn_moves(p_pos,player,tboard):
    opp_player,step = ('B',1) if player == 'W' else ('W',-1)
    
    i,j = p_pos[0],p_pos[1]

    valid_pos = [(i+step,j-1),(i+step,j+1)]
    valid_moves = []

    for pos in valid_pos:
        i,j = pos[0],pos[1]
        if (0<=i<4 and 0<=j<4):
            piece = tboard[i][j]
            if piece=='':
                continue
            
            if piece[1]==opp_player:
                if i==3 or i==0:
                    valid_moves.append(('#',i,j))
                else:
                    valid_moves.append(('x',i,j))

    i,j = p_pos[0],p_pos[1]
    i,j = (i+step,j)
    if (0<=i<4 and 0<=j<4):
        if tboard[i][j]=='':
            if i==3 or i==0:
                valid_moves.append(('=',i,j))
            else:
                valid_moves.append((' ',i,j))

    return valid_moves
        
def knight_moves(k_pos,player,tboard):
    opp_player='B' if player == 'W' else 'W'
    
    i,j = k_pos[0],k_pos[1]
    valid_pos = [(i-2,j-1),(i-2,j+1),(i+2,j-1),(i+2,j+1),(i-1,j-2),(i-1,j+2),(i+1,j-2),(i+1,j+2)]
    valid_moves = []
    for pos in valid_pos:
        i,j = pos[0],pos[1]
        if 0<=i<4 and 0<=j<4:
            piece = tboard[i][j]
            if piece=='':
                valid_moves.append((' ',i,j))
            else:
                if piece[1] == opp_player:
                    valid_moves.append(('x',i,j))
    return valid_moves

def queen_moves(q_pos,player,tboard):
    opp_player='B' if player == 'W' else 'W'

    valid_moves = []
    i,j = q_pos[0],q_pos[1]
    attack_lines = [[(x,j) for x  in range(i+1,4)],[(x,j) for x  in range(i-1,-1,-1)],
               [(i,x) for x  in range(j+1,4)],[(i,x) for x  in range(j-1,-1,-1)],
               [(x,y) for x,y in zip(range(i+1,4),range(j+1,4))],[(x,y) for x,y in zip(range(i-1,-1,-1),range(j-1,-1,-1))],
               [(x,y) for x,y in zip(range(i+1,4),range(j-1,-1,-1))],[(x,y) for x,y in zip(range(i-1,-1,-1),range(j+1,4))]]
    for line in attack_lines:
        for pos in line:
            i,j = pos[0],pos[1]
            piece = tboard[i][j]
            if piece:
                if piece[1] == opp_player:
                    valid_moves.append(('x',i,j))
                break
            else:
                valid_moves.append((' ',i,j))

    return valid_moves

def bishop_moves(b_pos,player,tboard):
    opp_player='B' if player == 'W' else 'W'

    valid_moves = []
    i,j = b_pos[0],b_pos[1]
    attack_lines = [[(x,y) for x,y in zip(range(i+1,4),range(j+1,4))],[(x,y) for x,y in zip(range(i-1,-1,-1),range(j-1,-1,-1))],
                    [(x,y) for x,y in zip(range(i+1,4),range(j-1,-1,-1))],[(x,y) for x,y in zip(range(i-1,-1,-1),range(j+1,4))]]
    for line in attack_lines:
        for pos in line:
            i,j = pos[0],pos[1]
            piece = tboard[i][j]
            if piece:
                if piece[1] == opp_player:
                    valid_moves.append(('x',i,j))
                break
            else:
                valid_moves.append((' ',i,j))

    return valid_moves

def rook_moves(r_pos,player,tboard):
    opp_player='B' if player == 'W' else 'W'

    valid_moves = []
    i,j = r_pos[0],r_pos[1]
    attack_lines = [[(x,j) for x  in range(i+1,4)],[(x,j) for x  in range(i-1,-1,-1)],
               [(i,x) for x  in range(j+1,4)],[(i,x) for x  in range(j-1,-1,-1)]]
    for line in attack_lines:
        for pos in line:
            i,j = pos[0],pos[1]
            piece = tboard[i][j]
            if piece:
                if piece[1] == opp_player:
                    valid_moves.append(('x',i,j))
                break
            else:
                valid_moves.append((' ',i,j))

    return valid_moves

def getAllValidMoves(player,tboard):
    valid_moves = []
    color = player.color
    for piece,pos in player.pieces.items():
        name = piece[0]
        if name=='Q':
            valid_moves.append(['Q',pos,queen_moves(pos,color,tboard)])
        elif  name=='R':
            valid_moves.append(['R',pos,rook_moves(pos,color,tboard)])
        elif name=='B':
            valid_moves.append(['B',pos,bishop_moves(pos,color,tboard)])
        elif name=='P':
            valid_moves.append(['P',pos,pawn_moves(pos,color,tboard)])
        else:
            valid_moves.append(['N',pos,knight_moves(pos,color,tboard)])
    return valid_moves
            
class State:
    def __init__(self,player,opp_player,moves, board,m):
        self.moves = moves
        self.m = m
        self.player = player
        self.opp = opp_player
        self.mboard = [[board[j][i] for i in range(4)] for j in range(4)]

    def printState(self):
        print ('=================================')
        print ('BOARD\n',self.mboard)
        print ('Player info')
        self.player.printInfo()
        print ('Oppn info')
        self.opp.printInfo()
        print ('Moves\n',self.moves)
        print ('Moves remaining\n',self.m)
        

def checkwinner(board):
    b_present = False
    w_present = False
    for i in range(4):
        for j in range(4):
            if board[i][j] == 'QW':
                w_present = True
            elif board[i][j] == 'QB':
                b_present = True

    return 'W' if w_present and not b_present else 'B'

'''
Changes needed : pawn promotions and their backtracking
= straight promotion
# kill and promote

For each promotion move:- three more moves with each piece - N B R
'''
def analyse(state):
    if state.m == 1:
        if under_attack(state.opp,state.mboard)[0]:
            return state.player.color
        else:
            return 'B'
    else:
        tboard=[[x for x in y] for y in state.mboard]
        tplayer=Player(state.player.color)
        tplayer.pieces=dict.copy(state.player.pieces)
        tplayer.minor_count = dict.copy(state.player.minor_count)
        
        topp=Player(state.opp.color)
        topp.pieces=dict.copy(state.opp.pieces)
        topp.minor_count = dict.copy(state.opp.minor_count)

        #check if winning move is possible
        death = under_attack(topp, tboard)
        if death[0]:
            #print (state.printState())
            return state.player.color
        for piece in state.moves:
            moves = piece[2]
            i,j=piece[1][0],piece[1][1]            
            for move in moves:
                #making a move checking if fine else backtracking
                #so pawn promtion needs three iterations here
                tboard[i][j]=''
                tboard[move[1]][move[2]]=piece[0]+tplayer.color
                #print (piece[0])
                for key,value in tplayer.pieces.items():
                    if value == (i,j):
                        tplayer.pieces[key]=(move[1],move[2])
                        break
                if under_attack(tplayer,tboard)[0]:   
                    tboard=[[x for x in y]for y in state.mboard]
                    tplayer=Player(state.player.color)
                    tplayer.pieces=dict.copy(state.player.pieces)
                    tplayer.minor_count = dict.copy(state.player.minor_count)
                    continue
                
                promotions =[None] # by default
                next_move = move[0]
                #print ('Move chosen','depth','Board','Player')
                #print (piece[0]+str(move),state.m,tboard,tplayer.color)
                #print ()
                if move[0] == '#' or move[0] == '=':
                    #loop the below statements thrice with N B R
                    #update piece[0] as N B R
                    #change move[0] = # = x
                    promotions = ['R','B','N']
                    if move[0]=="#":
                        next_move='x'
                if promotions[0]!=None:
                    promo_player=Player(tplayer.color)
                    promo_player.pieces=dict.copy(tplayer.pieces)
                    promo_player.minor_count = dict.copy(tplayer.minor_count)
                #remove pawn from the board and change it to promotions one byone
                for promotion in promotions:
                    if promotion != None:
                        tboard[i][j]=''
                        tboard[move[1]][move[2]]=promotion+tplayer.color
                        for key,value in tplayer.pieces.items():
                            if value == (move[1],move[2]):
                                tplayer.\
                                          pieces[promotion+str(tplayer.minor_count[promotion])]=tplayer.pieces.pop(key) # needs change
                                tplayer.minor_count[promotion]+=1
                                break
                    if next_move == 'x':
                        for key,value in topp.pieces.items():
                            if value == (move[1],move[2]):
                                topp.pieces.pop(key)
                                break
                            
                    if analyse(State(topp,tplayer, getAllValidMoves(topp,tboard), tboard, state.m-1)) == tplayer.color:
                        return state.player.color
                    else:
                        tboard=[[x for x in y]for y in state.mboard]
                        if next_move=='x':
                            topp=Player(state.opp.color)
                            topp.pieces=dict.copy(state.opp.pieces)
                            topp.minor_count = dict.copy(state.opp.minor_count)
                            
                        if promotion!=None:
                            tplayer=Player(promo_player.color)
                            tplayer.pieces=dict.copy(promo_player.pieces)
                            tplayer.minor_count = dict.copy(promo_player.minor_count)
                tplayer=Player(state.player.color)
                tplayer.pieces=dict.copy(state.player.pieces)
                tplayer.minor_count = dict.copy(state.player.minor_count)
                            


        #if state.player.color=='B':state.printState() 
        return state.opp.color
n=int(input())
start=time.clock()
res=''
for __ in range(n):
    try:
        input_board()
    except:
        break
    #print (getAllValidMoves(white,board))
    if m==1:
        if under_attack(black,board)[0]:
            res+='YES\n'
        else:
            res+='NO\n'
        continue
    state = State(white,black,getAllValidMoves(white,board), board,m)
    res+=('YES\n' if analyse(state) == 'W' else 'NO\n')

print (res)
print (time.clock()-start)





'''
analyse(state):
  if moves_remaining == 1:
     if opponent_under_attack():
        return player_color
     else:
        return black_wins #This is no true no matter what
  else:
     saved_state = copy(state)
     
     #check if winning move is possible again
     if opponent_under_attack()
        return player_color
     for move in available_moves():
        
        make_the_move()
        update_the_state()
            
        if player_under_attack:
           #this is to check if player
           #has got his own queen killed

           #if that's the case recopy the saved state
           state = copy(saved_state)
           continue

        promotions = [None]
            
        if move == promotion_move:   #depends on your implementation
           #loop the below statements thrice with N B R
           promotion = ['R','B','N']
            
        for promotion in promotions:
           if promotion != None:  #regular move if None
              update_the_state_with_promotion()
                    
           if a_kill_move:
              update_opponents_pieces
                    
           if analyse(changed_state) == player:  
              return player_color
           else:
              #that was a bad move so recopy
              state = copy(saved_state)  

   #if all moves are bad moves then opponenet wins
   return opponent_color
'''
