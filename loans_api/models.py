from pony.orm import *


db = Database()


class Product(db.Entity):
    uid = PrimaryKey(str, auto=True)
    name = Required(str)
