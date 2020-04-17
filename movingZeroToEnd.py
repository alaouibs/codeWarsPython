def move_zeros(array):
    compteur = 0
    output = []
    for c in array:
        if c == 0 and (type(c) == int or type(c) == float): 
            compteur = compteur + 1
        else:
            output.append(c)
    for i in range(compteur):
        output.append(0)
    print(output)
    return output
    #your code here

print(move_zeros([1,2,0,1,0,1,0,3,0,1]))
if move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]) == ['a', 'b', None, 'c', 'd', 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
    print("yes")