import random 

class Thief:
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs):
        self.name = name
        self.sneaky = sneaky

        for key, value in kwargs.items():
            setattr(self, key, value)


    def pickpoket(self):
        if self.sneaky:
            return bool(random.randint(0,1))
        return False

    def hide(self, light_level):
        return self.sneaky and light_level < 10



#
#>>> from characters import Thief                                                     
#>>> kenneth = Thief()                                                                
#Traceback (most recent call last):                                                   
#  File "<stdin>", line 1, in <module>                                                
#TypeError: __init__() missing 1 required positional argument: 'name'                 
#>>> kenneth = Thief("Kenneth", scars=None, favorite_weapon="Wit")                    
#>>> kenneth.name                                                                     
#'Kenneth'                                                                            
#>>> kenneth.sneaky                                                                   
#True                                                                                 
#>>> kenneth.favorite_weapon                                                          
#'Wit'     