from player import Player


player_1 = Player(1)
player_2 = Player(2)



def is_valid_move(move: str, taken_fields_x: set, taken_fields_0: set) -> bool:        
    if 1 <= int(move) <= 9:
        if int(move) not in (taken_fields_x | taken_fields_0):
            return True
        else:
            print("this field is already taken")
            return False
    else:
        print("expected int number in range 1-9")
        return False

def winner(taken_fields_x: set, taken_fields_0: set) -> int:
    w_1, w_2, w_3, w_4, w_5, w_6, w_7, w_8 = {1, 2, 3}, {4, 5, 6}, {7, 8, 9},\
                                            {1, 4, 7}, {2, 5, 8}, {3, 6, 9},\
                                            {1, 5, 9}, {3, 5, 7}
    if (w_1 & taken_fields_x) == w_1 or\
        (w_2 & taken_fields_x) == w_2 or\
        (w_3 & taken_fields_x) == w_3 or\
        (w_4 & taken_fields_x) == w_4 or\
        (w_5 & taken_fields_x) == w_5 or\
        (w_6 & taken_fields_x) == w_6 or\
        (w_7 & taken_fields_x) == w_7 or\
        (w_8 & taken_fields_x) == w_8:
        return 1
    if (w_1 & taken_fields_0) == w_1 or\
        (w_2 & taken_fields_0) == w_2 or\
        (w_3 & taken_fields_0) == w_3 or\
        (w_4 & taken_fields_0) == w_4 or\
        (w_5 & taken_fields_0) == w_5 or\
        (w_6 & taken_fields_0) == w_6 or\
        (w_7 & taken_fields_0) == w_7 or\
        (w_8 & taken_fields_0) == w_8:
        return 2
    else:
        return 0
    
# def drow_field(taken_fields_x: set, taken_fields_0: set) -> None:

       
def game() -> None:
    taken_fields_x = set()
    taken_fields_0 = set()
    win = 0

    while win == 0:
        valid_move_flag = False
        while not valid_move_flag:
            player_1.make_move()
            valid_move_flag = is_valid_move(player_1.move, taken_fields_x, taken_fields_0)
        taken_fields_x.add(int(player_1.move))
        win = winner(taken_fields_x, taken_fields_0)
        if win != 0:
            break

        valid_move_flag = False
        while not valid_move_flag:
            player_2.make_move()
            valid_move_flag = is_valid_move(player_2.move, taken_fields_x, taken_fields_0)
        taken_fields_0.add(int(player_2.move))
        win = winner(taken_fields_x, taken_fields_0)
        if win != 0:
            break

    print(taken_fields_x, taken_fields_0)
    print("Player №{} wins!".format(win))


# print('numbering of fields:\n\
# 1 2 3\n\
# 4 5 6\n\
# 7 8 9')
game()