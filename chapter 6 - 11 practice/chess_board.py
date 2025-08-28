def isValidChessBoard(board: dict[str, str]) -> bool:
    VALID_SQUARES = {
    "a1","a2","a3","a4","a5","a6","a7","a8",
    "b1","b2","b3","b4","b5","b6","b7","b8",
    "c1","c2","c3","c4","c5","c6","c7","c8",
    "d1","d2","d3","d4","d5","d6","d7","d8",
    "e1","e2","e3","e4","e5","e6","e7","e8",
    "f1","f2","f3","f4","f5","f6","f7","f8",
    "g1","g2","g3","g4","g5","g6","g7","g8",
    "h1","h2","h3","h4","h5","h6","h7","h8"
    }
 
    VALID_PIECES = {
    "wP","wN","wB","wR","wQ","wK",
    "bP","bN","bB","bR","bQ","bK"
    }


    if not board: #Return false on empty dictionary
        return False
    
    for i, x in board.items(): #Checks if square tiles and pieces are valid
        if i not in VALID_SQUARES:
            return False
        if x not in VALID_PIECES:
            return False

    counts = {"w": 0, "b": 0}     # total pieces per color
    pawns  = {"w": 0, "b": 0}     # pawn counts per color
    kings  = {"w": 0, "b": 0}     # king counts per color
    
    
    #To get colours and pieces from VALID_PIECES, extract using a for loop (strings are iterable)

    for i in board.values():
        colour = i[0] #w or b
        kind = i[1] #all the other pieces

        #From here you can start the frequency counter

        counts[colour] += 1 #Counts the pieces overall
        if counts[colour] > 16:
            return False

        if kind == 'P':  #Count pawns per colour
            pawns[colour] += 1
            if pawns[colour] > 8:
                return False

        if kind == 'K': #Count kind per colour
            kings[colour] += 1
            if kings[colour] > 1:
                return False


    return kings['w'] == 1 and kings['b'] == 1

#First mistake was I tried to perform a membership test with a container object instead of pairs, if i compared a container with another container, it would fail because of the mismatch of elements
#Second mistake was mixing up validation sets
#Third mistake was Rule interpretation