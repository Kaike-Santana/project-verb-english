class Verb:
    def __init__(self, verbo):
        self.verbo = verbo

    def passado(self):
        return self.verbo + "ed"

    def presente(self):
        return self.verbo

    def futuro(self):
        return "will " + self.verbo