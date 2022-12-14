class Game:

    def __init__(self):
        self.field = {'a': [' ', ' ', ' '],
                      'b': [' ', ' ', ' '],
                      'c': [' ', ' ', ' ']}

    def win(self, symbol):
        for i_key in self.field:
            if self.field[i_key][0] == self.field[i_key][1] == self.field[i_key][2] == symbol:
                return True
        for num in range(3):
            if self.field['a'][num] == self.field['b'][num] == self.field['c'][num] == symbol:
                return True
        if self.field['a'][0] == self.field['b'][1] == self.field['c'][2] == symbol \
                or self.field['a'][2] == self.field['b'][1] == self.field['c'][0] == symbol:
            return True

    def presentation(self):
        print('Игровое поле: ')
        print(f"   1   2   3\n"
              f"a  {self.field['a'][0]} | {self.field['a'][1]} | {self.field['a'][2]}\n"
              f"   {'-' * 9}\n"
              f"b  {self.field['b'][0]} | {self.field['b'][1]} | {self.field['b'][2]}\n"
              f"   {'-' * 9}\n"
              f"c  {self.field['c'][0]} | {self.field['c'][1]} | {self.field['c'][2]}\n")


class Players:
    def move(self, symbol, field):
        cell = input(f'Укажите пустую клетку (Вы играете {symbol}): ').lower()
        if field[cell[0]][int(cell[1]) - 1] == ' ':
            field[cell[0]][int(cell[1]) - 1] = symbol
        else:
            print('Указанная клетка уже занята. Выберите другую.\n')
            self.move(symbol, field)


game = Game()
player_1 = Players()
player_2 = Players()

game.presentation()

while True:
    try:
        print('Ход ПЕРВОГО игрока.', end='')
        player_1.move('x', game.field)
        game.presentation()
        if game.win('x'):
            print('Игра окончена! Победил ПЕРВЫЙ игрок!')
            break
        if ' ' in [i[num] for i in game.field.values() for num in range(3)]:
            print('Ход ВТОРОГО игрока.', end='')
            player_2.move('0', game.field)
            game.presentation()
            if game.win('0'):
                print('Игра окончена! Победил ВТОРОЙ игрок!')
                break
        else:
            print('Игра окончена! Больше нет пустых клеток.')
            break
    except (IndexError, KeyError, ValueError):
        print('Нет такой клетки.')
