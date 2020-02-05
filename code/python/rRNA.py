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

    def length(self):
        return self.__length

    """
    Functions
    """
    # generate a new rRNA sequence
    def newSeq(self, length):
        seq = np.random.choice(self.NUCLEOTIDES,  # sample nucleotides with replacement 
            size = length, 
            replace = True)
        return seq

    # Mutate portions of SSU genome
    # Can substitute @ multiple consecutive positions
    def mutate(self, i=int):

        return None