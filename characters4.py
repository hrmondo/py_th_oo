import random 


class Character:
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)


class Thief(Character):
    sneaky = True

    def __init__(self, name, sneaky= True, **kwargs):
        super().__init__(name, **kwargs)
        self.sneaky = sneaky

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