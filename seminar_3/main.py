from tictactoe import Board
from play_console import ConsolePlay


def main():
    board = Board(3)
    gameplay = ConsolePlay(board)
    msg = None
    while True:
        msg = msg or gameplay.get_default_input_message()
        gameplay.draw_board()
        if gameplay.draw_state():
            break
        inp = input(msg)
        msg = gameplay.handle_input(inp)


if __name__ == "__main__":
    main()
