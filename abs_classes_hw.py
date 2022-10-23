#Поскольку условие задачи довольно-таки расплывчатое и, как я поняла, мы можем его немного варьировать,
#чтобы полученная структура данных была адекватной и удобной.
#В программе считаем, что на вход нам даётся одна последовательность: рнк или кодирующая цепь днк (name). 
#И по ней либо у нас и есть рнк,
#либо строим матричную цепь днк. 
#PS потому что если считать днк как список из строк, то общих методов в класс Nucleo_sequence особо и не напишешь

from abc import abstractmethod
import random

class Nucleo_sequence:
    @abstractmethod
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def __add__(self, other):
        if not isinstance(other, Nucleo_sequence):
            return TypeError
        
        return self.name + other.name
        
    @abstractmethod
    def __index_of_base__(self, index):
        if 0 <= index < len(self.name):
            return self.name[index]
        else:
            raise IndexError("Error of index")
    
    @abstractmethod
    def __equal__(self, other):
        if not isinstance(other, Nucleo_sequence):
            return TypeError
        
        if self.name == other.name:
            return 'Sequences are equal'
        else:
            return 'Sequences are not equal'
            
    @abstractmethod
    def complementary(self):
        pass
        
    @abstractmethod
    def __multiplication__(self, other):
        if not isinstance(other, Nucleo_sequence):
            return TypeError
        
        multipl_seq = ''
        for i in range(min(len(self.name), len(other.name))):
            multipl_seq += random.choice([self.name[i], other.name[i]])
        if len(self.name) > len(other.name):
            multipl_seq += self.name[len(other.name):]
        else:
            multipl_seq += other.name[len(self.name):]
        
        return multipl_seq



class RNA(Nucleo_sequence):
    def __init__(self, name):
        rna_bases = set(['A', 'U', 'C', 'G'])
        super().__init__(name)
        if not(set(self.name) <= rna_bases):
            raise Exception('Input bases are incorrect')
        
    def __str__(self):
        return f'{self.name}'
        
    def __repr__(self):
        return f'{self.name}'
        
    def complementary(self):
        complementary_date =  {
                                    'A': 'T',
                                    'U' : 'A',
                                    'G' : 'C',
                                    'C' : 'G'
                                    }
        dna_seq = ''
        for base in self.name:
            dna_seq += complementary_date[base]
            
        return dna_seq[::-1]


class DNA(Nucleo_sequence):
    def __init__(self, name):
        dna_bases = set(['A', 'T', 'C', 'G'])
        super().__init__(name)
        if not(set(self.name) <= dna_bases):
            raise Exception('Input bases are incorrect')
    
    def __str__(self):
        return f'{self.name}'
        
    def __repr__(self):
        return f'{self.name}'
    
    def __index_of_base__(self, index):
        base = super().__index_of_base__(index)
        self.complementary()
        return base, self.matrix_seq[index]
    
    def complementary(self):
        complementary_date = {
                                'A': 'T',
                                'T' : 'A',
                                'G' : 'C',
                                'C' : 'G'
                                }
        matr_seq = '' #будем строить матричную цепь по кодирующей
        for base in self.name:
           matr_seq += complementary_date[base]
        self.matr_seq =matr_seq[::-1]

