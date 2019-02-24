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



import random 

class Thief:
    sneaky = True

    def pickpoket(self):
        if self.sneaky:
            return bool(random.randint(0,1))
        return False




>>> from characters import Thief                                                     
>>> kenneth = Thief()
>>> kenneth.sneaky = False
>>> kenneth.pickpocket()








import random

class Thief:
    sneaky = True  # class attribute (will exist in all class instances)

    def pickpocket(self):
        """method to determine if thief successfully picks a pocket
        based on sneaky attribute and a bit of luck.
        """

        # if attribute is True, use chance to see if successful
        if self.sneaky:
            # return 50-50 chance on being successful
            return bool(random.randint(0, 1))
        # if not returned above, self.sneaky must be false.
        # so no chance at success. return False (failure)
        return False