## Ford Fishman
# Meant to model the protein coding gene

class Gene:

    """
    Constructor
    -----------
    seq (str): the sequence of nucleotides representing the gene
    allele (int): type of allele 
    name (str): type of gene
    """
    def __init__(self, name:str, allele:int, seq:str=""):
        self.__seq = seq; self.__allele = allele; self.__name = name

    """
    Attributes
    """

    def seq(self, asString:bool=False):
        
        if asString:
            seq = "".join(self.__seq)

        else:
            seq = self.__seq
            
        return seq

    def allele(self): return (self.__allele)

    def name(self): return (self.__name)

    """
    Modifiers
    """

    def setAllele(self, allele:int):

        self.__allele = allele

        return None


