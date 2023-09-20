class Player:
    def __init__(self, id, move = 0):
        self.id = id
        self.move = move

    def make_move(self) -> str:
        while True:
            self.move = input("Player {}, please make move - input number of field (1-9):\n".format(self.id))
            try:
                int(self.move)
                break
            except ValueError:
                print("expected integer number in range 1-9")
