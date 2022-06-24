from collections import Counter

def isValidChessBoard(board):
    '''Checks if inputed chess board is valid. Keys are square of board, values are pieces'''
    #pieceCount = Counter(board.values())
    # returns dict with number of each piece on board

    pieceCount = {}
    for piece in board.values():
        pieceCount.setdefault(piece, 0)
        pieceCount[piece] += 1

    #squares = []
    #for number in [1,2,3,4,5,6,7,8]:
    #    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
    #        squares.append(str(number) + letter)

    #print(squares)


    if 'wking' not in board.values() or 'bking' not in board.values():
        return False
    elif pieceCount.get('wking', 0) != 1 or pieceCount.get('bking', 0) != 1:
        return False
    elif len(board.values()) > 32: # max 32 pieces in total on board
        return False
    elif pieceCount.get('wpawn', 0) > 8 or pieceCount.get('bpawn', 0) > 8:
        return False
    elif pieceCount.get('wpawn', 0) + pieceCount.get('wrook', 0) + pieceCount.get('wknight', 0) + pieceCount.get('wbishop', 0) \
    + pieceCount.get('wqueen', 0) + pieceCount.get('wking', 0) > 16: # white can have at most 16 pieces
        return False
    elif pieceCount.get('bpawn', 0) + pieceCount.get('brook', 0) + pieceCount.get('bknight', 0) + pieceCount.get('bbishop',0) \
    + pieceCount.get('bqueen', 0) + pieceCount.get('bking', 0) > 16: # white can have at most 16 pieces
        return False

    for location in board.keys():
        row = int(location[:1])
        column = location[1:]
        if not ((1 <= row <= 8) and ('a' <= column <= 'h')):
            print(f"Invalid to have {board[location]} at positon {location}")
            return False

    return True

chessBoard = {'1h': 'bking', '6c': 'wqueen',
'2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

print(isValidChessBoard(chessBoard))


