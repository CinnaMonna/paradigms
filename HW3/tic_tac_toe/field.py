class Field:
    def __init__(self, filling_list = ['_', '_', '_', '_', '_', '_', '_', '_', '_']):
       self.filling_list = filling_list

    def set_x(self, i):
        self.filling_list[i] = 'X'

    def set_0(self, i):
       self.filling_list[i] = '0'

    def drow_field(self):
        for i in range(3):
            print(self.filling_list[i], end = ' ')
        print()
        for i in range(3, 6):
            print(self.filling_list[i], end = ' ')
        print()
        for i in range(6, 9):
            print(self.filling_list[i], end = ' ')
        print("\n")
