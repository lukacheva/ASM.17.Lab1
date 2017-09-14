class MenuItem:
    id: int
    text: str
    func: classmethod

    def __init__(self, _id, _text, _func):
        self.id = _id
        self.text = _text
        self.func = _func

