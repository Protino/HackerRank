from collections import defaultdict
from copy import deepcopy

class Player:
    def __init__(self,color):
        self.color = color
        self.pieces = dict()
    def addPiece(self,piece,pos):
        self.pieces[piece]=pos
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
    knight_count = 0
    board = [['']*4 for __ in range(4)]
    white = Player('W')
    black = Player('B')
    
    w,b,m = map(int,input().split())
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
        elif piece == 'N':
            piece = 'N1' if knight_count else 'N0'
            knight_count+=1
            
        white.addPiece(piece,(int(row)-1,col))
        
    bishop_count = 0
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
        elif piece == 'R':
            piece = 'R1' if rook_count else 'R0'
            rook_count+=1
        elif piece == 'N':
            piece = 'N1' if knight_count else 'N0'
            knight_count+=1
        black.addPiece(piece,(int(row)-1,col))


def under_attack(player,tboard):
    if 'Q' not in player.pieces:
        return True, (-1,-1)
        
    q_pos = player.pieces['Q']
    opp_player = 'W' if player.color == 'B' else 'B'
    
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


def analyse(state):
    if state.m == 1:
        if under_attack(state.opp,state.mboard)[0]:
            return state.player.color
        else:
            return 'B'
    else:
        tboard=deepcopy(state.mboard)
        tplayer=deepcopy(state.player)
        topp=deepcopy(state.opp)

        #check if winning move is possible
        death = under_attack(topp, tboard)
        if death[0]:
            return state.player.color
        for piece in state.moves:
            moves = piece[2]
            i,j=piece[1][0],piece[1][1]            
            for move in moves:
                tboard[i][j]=''
                tboard[move[1]][move[2]]=piece[0]+tplayer.color
                for key,value in tplayer.pieces.items():
                    if value == (i,j):
                        tplayer.pieces[key]=(move[1],move[2])
                        break
                if under_attack(tplayer,tboard)[0]:   
                    tboard=deepcopy(state.mboard)
                    tplayer=deepcopy(state.player)
                    topp=deepcopy(state.opp)
                    #print ('discarded')
                    continue
                print ('move chosen--',(piece[0]+tplayer.color,piece[1]),(move[1],move[2]),state.m)
                if move[0] == 'x':
                    for key,value in topp.pieces.items():
                        if value == (move[1],move[2]):
                            topp.pieces.pop(key)
                            break
                if analyse(State(topp,tplayer, getAllValidMoves(topp,tboard), tboard, state.m-1)) == tplayer.color:
                    return state.player.color
                else:
                    tboard=deepcopy(state.mboard)
                    tplayer=deepcopy(state.player)
                    topp=deepcopy(state.opp)
        return state.opp.color
    
for __ in range(int(input())):
    input_board()
    if m==1:
        print (under_attack(black,board))
        if under_attack(black,board)[0]:
            print ('YES')
        else:
            print ('NO')
        continue
    state = State(white,black,getAllValidMoves(white,board), board,m)
    print ('YES' if analyse(state) == 'W' else 'NO')

