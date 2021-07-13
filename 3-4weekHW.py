class Cell:
    """Класс клетка"""

    def __init__(self, nums):
        self.nums = nums
    def maker_order(self, rows):
        return '\n'.join(['клетка' * rows for _ in  range(self.nums // rows)])  + '\n' + 'клетка' * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print("Сумма клеток:")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("Разность клеток: ")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "ячеек в клетке меньше второй, вычетание невозможно"

    def __mul__(self, other):
        print("Умножение: ")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("Истина")
        return Cell(self.nums // other.nums)

cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
