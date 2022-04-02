import random
import string

class Utilities:
    def __init__(self, db_check, db_adder):
        self.check_db = db_check
        self.add_to_db = db_adder

    def generate_raw_pass(self, len: int=16) -> str:
        return "".join(random.choices(string.ascii_letters+string.digits+string.punctuation, k=len))
    
    def generate_pass(self, password_length):
        p = self.generate_raw_pass(password_length)
        check = self.check_db(p)
        if check:
            return self.generate_pass()
        self.add_to_db(p)
        return p