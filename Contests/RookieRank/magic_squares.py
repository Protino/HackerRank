import operator
def generate_all_magic_squares():
    distinct_magic_squares = [[6,7,2,1,5,9,8,3,4],[4,3,8,9,5,1,2,7,6],
                              [6,3,6,5,5,5,4,7,4],[4,7,4,5,5,5,6,3,6],
                              [6,1,8,7,5,3,2,9,4],[4,9,2,3,5,7,8,1,6],
                              [6,5,4,3,5,7,6,5,4],[4,5,6,7,5,3,4,5,6],
                              [2,9,4,7,5,3,6,1,8],[2,7,6,9,5,1,4,3,8],
                              [8,3,4,1,5,9,6,7,2],[8,1,6,3,5,7,4,9,2]]

    input_matrix = [1,2,3,4,5,6,7,8,9]
    """
    for __ in range(3):
        a,b,c = map(int,input().split())
        input_matrix.append(a)
        input_matrix.append(b)
        input_matrix.append(c)
    """
    min_cost = []
    for magic_square in distinct_magic_squares:
        cost = sum([abs(x) for x in map(operator.sub,magic_square,input_matrix)])
        min_cost.append(cost)
    print (min(min_cost))
        
        
generate_all_magic_squares()        
