class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
    
    def __str__(self):
        dot_dash_str = []
        for x in self.pattern:
            if x == '.':
                dot_dash_str.append('dot')   
            if x == '_':
                dot_dash_str.append('dash')
        return '-'.join(dot_dash_str)


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)