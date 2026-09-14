class Matrix:
    def __init__(self, size):
        self.matrix = [
            [0 for _ in range(size)]
            for _ in range(size)
        ]
        self.size = size
