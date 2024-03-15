def game(x, y, z):
    if x + y >= 100: return z%2==0
    if z == 0: return 0
    steps = [game(x+1,y,z-1), game(x,y+1,z-1), game(x*3,y,z-1), game(x,y*3,z-1)]
    return any(steps) if z%2!=0 else all(steps)

print("19:", [x for x in range(1,100) if game(10,x,2)])
print("20:", [x for x in range(1,100) if not game(10,x,1) and game(10,x,3)])
print("21:", [x for x in range(1,100) if not game(10,x,2) and game(10,x,4)]) 

# Written by Vsevolod Flovitskiy.