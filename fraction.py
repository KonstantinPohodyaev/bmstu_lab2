class Fraction:
    def __init__(self, ch, zn):
        if zn == 0:
            raise ValueError(
                f'Знаменатель не может равняться 0!'
            )
        self.ch = ch
        self.zn = zn

    def __add__(self, f):
        return Fraction(
            self.ch * f.zn + self.zn * f.ch,
            self.zn * f.zn,
        )

    def __sum__(self, f):
            return Fraction(
                self.ch * f.zn - self.zn * f.ch,
                self.zn * f.zn,
            )

    def __str__(self):
        return f'{self.ch}/{self.zn}'

    def __repr__(self):
        return f'{self.ch}/{self.zn}'
