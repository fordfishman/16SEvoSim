## Ford Fishman
# class for strain, defined here by differences in protein coding genes

# import modules
import rRNA
import Gene
import Error as er

class Strain:

    """
    Constructor
    -----------
    name (str) - name of strain
    ssu (rRNA) - represents rRNA of strain
    ssuLength (int) - how long rRNA will be
    genome (dict) - a collection of Genes in strain genome - geneName:gene
    #startingGeneNum (int) - how many genes a new strain starts with
    pop (int) - population size, discrete 
    """
    def __init__(self, name:str, genome:dict, pop:int=1, ssu:rRNA=None, ssuLength:int=1400):

        # unimplemented code for adding genome of first strains 
        # self.__genome = dict()

        # # no genome given to start
        # if genome is None:
        #     self.newGenes()
        
        # else:
        self.__name = name
        self.__genome = genome

        # no specific ssu given
        if ssu is None:
            ssu = self.newRNA(ssuLength)

        self.__ssu = ssu
        self.__pop = pop

    """
    Attributes
    """
    def name(self): return self.__name

    def ssu(self): return self.__ssu

    def genome(self): return self.__genome

    def pop(self): return self.__pop

    def getGeneNames(self): return list(self.__genome.keys())

    """
    Modifiers
    """

    def setPop(self, pop:int):
        """Change strain population size"""
        self.__pop = pop

        return None

    """
    Other Functions
    """
    
    def getGene(self, geneName):
        """Return gene object with specified name"""
        return self.__genome[geneName]

    def newRNA(self, length:int):
        """Create new rRNA sequence"""
        return rRNA.rRNA(length=length)

    
    def addGene(self, gene:Gene.Gene):
        """Add gene to the genome"""
        self.__genome[gene.name()] = gene

        return None

    
    def removeGene(self, name:str=None, i:int=None):
        """Remove gene from genome by index or by name""" 
        try:

            if ((name is None) and (i is None)) or ((not name is None) and (not i is None)):

                raise er.FunctionError

        except er.FunctionError:

            print("Specify a name for the gene or its place in the genome")
            print()

        else:
            
            if i is None: # if gene is specified by name

                i = self.__genome.index(name)

            self.__genome.pop(i)
              
        return None
    
    
    def changeAllele(self, geneName:str, newAllele:int):
        """Change the allele type of a gene by gene name"""
        self.__genome[geneName].setAllele(newAllele)

        return None

    def changeSSU(self):
        """Mutate the strain's SSU"""
        self.__ssu.mutate()

        return None

    def growth(self):
        return None

    # unimplemented 
    # add newly created gene(s) to the strain
    # num(int): number 
    # names (list[str]): names of genes
    # def newGenes(self, names:list, num:int=1):

    #     genes = dict()
        

    #     return None