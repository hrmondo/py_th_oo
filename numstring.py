class NumString:
    def __init__(self, value): 
    # __init__ - Customize the initialization of your instances
        self.value = str(value)

    def __str__(self):
    # __str__ - Control how your instances turn into strings
        return self.value

    def __int__(self):
    # __int__ - Control int() conversion
        return int(self.value)

    def __float__(self):
        return float(self.value)



# >>> from numstring import NumString                                      
# >>> five = NumString(5)                                                              
# >>> five                                                                             
# <numstring.NumString object at 0x7f1a69fce6d8>                                       
# >>> str(five)                                                                        
# '5'                                                                                  
# >>> int(five)                                                                        
# 5                                                                                    
# >>> float(five)                                                                      
# 5.0                                                                                  
