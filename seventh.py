class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    @staticmethod
    def is_position_on_board(position):
        row, col = position
        return 1 <= row <= 8 and 1 <= col <= 8


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        if self.color == "white":
            if self.is_position_on_board((row + 1, col)):
                moves.append((row + 1, col))
        elif self.color == "black":
            if self.is_position_on_board((row - 1, col)):
                moves.append((row - 1, col))
        return moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        for i in range(1, 8):
            moves += [
                (row + i, col + i),
                (row + i, col - i),
                (row - i, col + i),
                (row - i, col - i)
            ]
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        for i in range(1, 8):
            moves += [
                (row + i, col), (row - i, col),
                (row, col + i), (row, col - i)
            ]
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        bishop_moves = Bishop(self.color, self.position).possible_moves()
        rook_moves = Rook(self.color, self.position).possible_moves()
        return bishop_moves + rook_moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 1, col), (row - 1, col),
            (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1),
            (row - 1, col + 1), (row - 1, col - 1)
        ]
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


def main():
    print("Šachový simulátor - výpočet možných tahů")
    print("Zadejte figurku: Pawn, Knight, Bishop, Rook, Queen, King")
    piece_type = input("Typ figurky: ").strip().capitalize()

    if piece_type not in ["Pawn", "Knight", "Bishop", "Rook", "Queen", "King"]:
        print("Neplatný typ figurky.")
        return

    color = input("Barva figurky (white/black): ").strip().lower()
    if color not in ["white", "black"]:
        print("Neplatná barva.")
        return

    try:
        position = tuple(map(int, input("Zadejte pozici figurky (řádek sloupec, např. 2 2): ").strip().split()))
        if len(position) != 2 or not Piece.is_position_on_board(position):
            print("Neplatná pozice.")
            return
    except ValueError:
        print("Neplatný formát pozice.")
        return

    piece = None
    if piece_type == "Pawn":
        piece = Pawn(color, position)
    elif piece_type == "Knight":
        piece = Knight(color, position)
    elif piece_type == "Bishop":
        piece = Bishop(color, position)
    elif piece_type == "Rook":
        piece = Rook(color, position)
    elif piece_type == "Queen":
        piece = Queen(color, position)
    elif piece_type == "King":
        piece = King(color, position)

    print(piece)
    print("Možné tahy:", piece.possible_moves())


if __name__ == "__main__":
    main()
