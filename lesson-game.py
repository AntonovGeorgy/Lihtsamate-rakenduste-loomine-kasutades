map1 = [
    [12,0,1,0],
    [1,0,1,0],
    [1,0,1,0],
    [1,0,0,24]
]

map2 = [
    [12,0,0,0],
    [0,1,1,0],
    [0,0,0,0],
    [0,0,0,24]
]

map=map1

current_position_x = 0
current_position_y = 0

print("Current cyrrent_position_y =",current_position_y)
print("Current cyrrent_position_x =",current_position_x)
#1
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("Should move right")
    current_position_x = current_position_x+1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y+1

#2
print("Current cyrrent_position_y =",current_position_y)
print("Current cyrrent_position_x =",current_position_x)
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("Should move right")
    current_position_x = current_position_x+1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y+1

print("Current cyrrent_position_y =",current_position_y)
print("Current cyrrent_position_x =",current_position_x)
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0
#3
if can_move_right:
    print("Should move right")
    current_position_x = current_position_x+1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y+1
#4
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("Should move right")
    current_position_x = current_position_x+1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y+1

#5
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("Should move right")
    current_position_x = current_position_x+1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y+1


