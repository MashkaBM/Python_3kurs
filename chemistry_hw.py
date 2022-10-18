# вещества
class Acid():
    def __init__(self, name='acid'):
        self.name = name
    def __str__(self):
        return f'{self.name}'
    def __repr__(self):
        return f'{self.name}'
    def __add__(self, other):
        if other.name == 'base':
            return Sault(), Water()
        elif other.name == 'sault':
            return Sault(), Acid()
        elif other.name == 'phenolphthalein':
            return Phenolphthalein(color = 'бесцветный')
        elif other.name == 'litmus':
            return Litmus(color = 'красный')
        elif other.name == 'methylOrange':
            return MethylOrange(color = 'розовый')
        else:
            return TypeError

class Base:
    def __init__(self, name='base'):
        self.name = name
    def __str__(self):
        return f'{self.name}'
    def __repr__(self):
        return f'{self.name}'
    def __add__(self, other):
        if other.name == 'acid':
            return Sault(), Water()
        elif other.name == 'sault':
            return Sault(), Base()
        elif other.name == 'phenolphthalein':
            return Phenolphthalein(color = 'малиновый')
        elif other.name == 'litmus':
            return Litmus(color = 'синий')
        elif other.name == 'methylOrange':
            return MethylOrange(color = 'желтый')
        else:
            return TypeError    
        
class Sault:
    def __init__(self, name='sault'):
        self.name = name
    def __str__(self):
        return f'{self.name}'
    def __repr__(self):
        return f'{self.name}'
    def __add__(self, other):
        if other.name == 'acid':
            return Sault(), Acid()
        elif other.name == 'base':
            return Sault(), Base()
        else:
            return TypeError    
        
        
class Water:
    def __init__(self, name='water'):
        self.name = name
    def __str__(self):
        return f'{self.name}'
    def __repr__(self):
        return f'{self.name}'
        
#  индикаторы
class Phenolphthalein:
    def __init__(self, name='phenolphthalein', color='бесцветный'):
        self.name = name
        self.color = color
    def __str__(self):
        return f'{self.name}, {self.color}'
    def __repr__(self):
        return f'{self.name},{self.color}'
    def __add__(self, other):
        if other.name == 'acid':  
            self.color = 'бесцветный'
            return Phenolphthalein(color = 'бесцветный')
        elif other.name == 'base':
            self.color = 'малиновый'
            return Phenolphthalein(color = 'малиновый')
        else:
            return TypeError     
            
                
class Litmus:
    def __init__(self, name='litmus', color='бесцветный'):
        self.name = name
        self.color = color
    def __str__(self):
        return f'{self.name}, {self.color}'
    def __repr__(self):
        return f'{self.name},{self.color}'
    def __add__(self, other):
        if other.name == 'acid':  
            self.color = 'красный'
            return Litmus(color = 'краcный')
        elif other.name == 'base':
            self.color = 'синий'
            return Litmus(color = 'синий')
        else:
            return TypeError      
        
class MethylOrange:
    def __init__(self, name='methylOrange', color='бесцветный'):
        self.name = name
        self.color = color
    def __str__(self):
        return f'{self.name}, {self.color}'
    def __repr__(self):
        return f'{self.name},{self.color}'
    def __add__(self, other):
        if other.name == 'acid':  
            self.color = 'розовый'
            return MethylOrange(color = 'розовый')
        elif other.name == 'base':
            self.color = 'желтый'
            return MethylOrange(color = 'желтый')
        else:
            return TypeError


acid = Acid()
base = Base()
sault = Sault()
water = Water()

methylOrange = MethylOrange()
litmus = Litmus()
phenolphthalein = Phenolphthalein()
 
reaction_products = acid + base

print(reaction_products)
p = MethylOrange()
print (p)