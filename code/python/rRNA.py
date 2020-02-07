## Ford Fishman
# Meant to model the 16S rRNA

import Error as er
import numpy as np

class rRNA:

    """
    Constructor
    -----------
    seq (str): the sequence of nucleotides representing the gene
    length (int): length of seq
    NUCLEOTIDES (tuple): set of A, G, C, T
    """
    def __init__(self, seq:str=None, length:int=1400):

        self.NUCLEOTIDES = ("A","C","G","T")
        # if no sequence is given
        if seq is None:
            seq = self.newSeq(length=length)

        self.__seq = seq
        self.__length = length


    """
    Attributes
    """

    def seq(self, asString:bool=False):
        
        if asString:
            seq = "".join(self.__seq)

        else:
            seq = self.__seq
            
        return seq

    def length(self): return self.__length

    """
    Functions
    """    
    def newSeq(self, length):
        """Generate a new rRNA sequence"""
        seq = np.random.choice(self.NUCLEOTIDES,  # sample nucleotides with replacement 
            size = length, 
            replace = True)
        return seq


    def mutate(self, i:int=None):
        """Mutate positions of SSU genome"""
        if i is None or i >= len(self.__seq) or i < 0:
            i = np.random.choice( list( range(0,len(self.__seq)) ) ) # an integer indexing the gene
        
        noChange = True # sequence hasn't yet been changed
        while noChange:
            oldNT = self.__seq[i]
            self.__seq[i] = np.random.choice(self.NUCLEOTIDES)
            noChange = oldNT == self.__seq[i]

        return None