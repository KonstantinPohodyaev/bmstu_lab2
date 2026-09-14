class Matrix:
    def __init__(self, size):
        if size < 1:
            raise ValueError(
                f'Кол-во строк не может быть меньше 1: {size}'
            )

        self.matrix = [
            [0 for _ in range(size)]
            for _ in range(size)
        ]
        self.size = size
