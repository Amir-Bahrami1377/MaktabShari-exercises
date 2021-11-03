import pickle
import dill


class User:
    usernames: list = []

    def __init__(self, id, first_name, last_name, phone) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    @classmethod
    def sorted(cls):
        pass

    @classmethod
    def unpickling(cls, file_path: str):
        with open(file_path, 'rb') as f:
            return pickle.loads(f.read())

    def save_names(self):
        with open('output-q-3-3.txt', "wb") as dill_file:
            dill_file.write(dill.dumps(User.usernames))

    def __repr__(self) -> str:
        return f"<{self.id}> <{self.first_name}> <{self.last_name}> <{self.phone}>"


def fullname() -> str:
    pass


u1 = User.unpickling('users.pickled')
print(u1.__repr__())



