def done_or_not(board): #board[i][j]
    setZone = []
    for i in range(0, 3):
        setZone.append([])
        for j in range(0, 3):
            setZone[i].append(set())
    setLines = set()
    SetColumn = []
    for i in range(0, len(board)):
        SetColumn.append(set())
    for i in range(0, len(board)):
        setLines = set()
        for j in range(0, len(board)):
            if board[i][j] in setZone[int(i/3)][int(j/3)]:
                print("setZOne")
                print((i,j))
                print(board[i][j])
                print(setZone[int(i/3)][int(j/3)])
                return "Try again!"            
            elif board[i][j] in setLines:
                print("setLine")
                return "Try again!"            
            elif board[i][j] in SetColumn[j]:
                print("setColumn")
                return "Try again!"            

            setZone[int(i/3)][int(j/3)].add(board[i][j])
            setLines.add(board[i][j])
            SetColumn[j].add(board[i][j])
    return "Finished!"

print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]))