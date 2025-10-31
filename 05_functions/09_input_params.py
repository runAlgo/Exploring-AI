# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Preparing:", order)

# prepare_chai(chai)

chai = [1, 2, 3]

def edit_chai(cup):
   cup[1] = 42
   print("Chai:", chai)
edit_chai(chai)


def make_chai(tea, chai, coffee):
    print(tea, chai, coffee)
# make_chai("green tea", "lemon chai", "Cold Coffee")
# make_chai(tea="green", coffee="hot", chai="Lemon")

def special_chai(*ingredients, **extras): #kwargs
    print("Ingredients", ingredients)
    print("Extra", extras)

special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="yes")


# def chai_order(order = []):
#     order.append("Masala")
#     print(order)


def chai_order(order = None):
    if order is None:
        order = []
        order.append("chai tea")
    print(order)
chai_order()
chai_order()