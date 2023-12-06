from functools import reduce
from typing import Tuple, Any, Iterable
1

class Board:
    def __init__(self, s):
        val = self.get_empty_cell_value()
        self.size = s
        self.current_player = 'X'
        sizes = self.get_sizes()
        self.cells = [val] * self.calc_idx((sizes[0],) + (0,) * (len(sizes) - 1))

    def get_sizes(self) -> tuple[Any, Any]:
        return self.size, self.size

    @classmethod
    def get_empty_cell_value(cls) -> str:
        return ' '

    def switch_to_next_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_rules(self, idx: Tuple[int, ...], val: str):
        if val != self.current_player:
            raise WrongPlayerMoveError('Wrong player move.')
        if self[(idx)] != self.get_empty_cell_value():
            raise WrongCellChosenError('Cell is already occupied.')
        return True

    def __setitem__(self, key, value):
        if self.check_rules(key, value):
            self.cells[self.calc_idx(key)] = value
        self.switch_to_next_player()

    def get_winner(self) -> None | Tuple[str, Tuple[int, ...], Tuple[int, ...]]:
        size = self.size
        e = self.get_empty_cell_value()

        # Main diagonal
        v = self[(0, 0)]
        if v != e:
            for i in range(1, size):
                if self[(i, i)] != v:
                    break
            else:
                return v, (0, 0), (1, 1)

        # Secondary diagonal
        v = self[(0, size - 1)]
        if v != e:
            for i in range(1, size):
                if self[(i, size - 1 - i)] != v:
                    break
            else:
                return v, (0, size - 1), (1, -1)

        # Horizontals/verticals
        for j in range(size):
            v = self[(0, j)]
            if v != e:
                for i in range(1, size):
                    if self[(i, j)] != v:
                        break
                else:
                    return v, (0, j), (1, 0)
            v = self[(j, 0)]
            if v != e:
                for i in range(1, size):
                    if self[(j, i)] != v:
                        break
                else:
                    return v, (j, 0), (0, 1)

        # Has room to put a figure — game is not over
        if e in self.cells:
            return None

        # No room and no win conditions met — so draw
        return e, (0, 0), (0, 0)

    def calc_idx(self, idx: Tuple[int]) -> int:
        sizes = self.get_sizes()
        return reduce(lambda acc, szidx: acc * szidx[0] + szidx[1], zip(sizes, idx), 0)

    def __getitem__(self, idx: Iterable[int]):
        return self.cells[self.calc_idx(tuple(idx))]


class WrongPlayerMoveError(ValueError):
    pass


class WrongCellChosenError(ValueError):
    pass