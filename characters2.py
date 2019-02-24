import random 

class Thief:
    sneaky = True
    # sneaky: doing things in a secret and unfair way

    def pickpoket(self):
        print("Called by []".format(self))
　　　#the self in python is used to point to the current instance much in the same manner as the this is used in JavaScript to point to the current object. 

            return bool(random.randint(0,1))
    # bool: True or Flase
    # random.randient: produces a random integer in the range specified, boundaries included



#
# >>> from characters import Thief                                                     
# >>> kenneth = Thief()
# >>> kenneth.sneaky = False
# >>> kenneth.pickpocket()

