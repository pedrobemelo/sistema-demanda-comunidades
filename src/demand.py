import uuid

class Demand:
    def __init__(self, title, description, category):
        if not title:
            raise ValueError("Título não pode ser vazio")

        self.id = int(uuid.uuid4().int % 10000)
        self.title = title
        self.description = description
        self.category = category
        self.status = "Aberto"

    def to_dict(self):
        return self.__dict__