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






# >>> from characters import Thief                                                     
# >>> kenneth = Thief()
# >>> kenneth.sneaky = False
# >>> kenneth.pickpocket()








