game_row = {
    'top-l': ' ', 'top-m': ' ','top-r':' ','mid-l': ' ', 'mid-m': ' ','mid-r': ' ','bottom-l': ' ', 'bottom-m': ' ',
    'bottom-r': ' ',
}
row = [i for i in range(1,len(game_row)+1)]
row_mapping = []
print(row_mapping)
def draw_game():
    print(f"{game_row['top-l']}|{game_row['top-m']}|{game_row['top-r']}")
    print('-'*5)
    print(f"{game_row['mid-l']}|{game_row['mid-m']}|{game_row['mid-r']}")
    print('-' * 5)
    print(f"{game_row['bottom-l']}|{game_row['bottom-m']}|{game_row['bottom-r']}")


def check_win():
    # first check if all the things are same
    for i in ['top','mid','bottom']:
        if game_row['{}-l'.format(i)] == game_row['{}-m'.format(i)] == game_row['{}-r'.format(i)]:
            if game_row['{}-l'.format(i)] == 'O':
                return (True,'O')
            return (True,'X')

    if game_row['bottom-l'] == game_row['mid-m'] == game_row['top-r'] or \
            game_row['bottom-r'] == game_row['mid-m'] == game_row['top-l']  :
        if game_row['bottom-r'] == 'O':
            return (True,'O')
        return (True,'X')

    return (False,'')

draw_game()
user_input = input('Your turn')

if not check_win():
    draw_game()

