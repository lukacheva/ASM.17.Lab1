class MenuItem:
    id: int = None
    text: str = None
    func: classmethod = None

    def __init__(self, id, text, func):
        self.id = id
        self.text = text
        self.func = func

