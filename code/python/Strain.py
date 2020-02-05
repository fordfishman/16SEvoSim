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
    def name(self):
        return self.__name

    def ssu(self):
        return self.__ssu

    def genome(self):
        return self.__genome

    def pop(self):
        return self.__pop

    """
    Modifiers
    """

    # change strain population size
    def setPop(self, pop:int):
        
        self.__pop = pop

        return None

    """
    Other Functions
    """

    # Return gene object with specified name
    def getGene(self, geneName):
        return self.__genome[geneName]

    # create new rRNA sequence
    def newRNA(self, length:int):

        return rRNA.rRNA(length=length)


    # add gene to the genome
    def addGene(self, gene:Gene.Gene):

        self.__genome[gene.name()] = gene

        return None

    # remove gene from genome by index or by name 
    def removeGene(self, name:str=None, i:int=None):

        try:

            if ((name is None) and (i is None)) or ((not name is None) and (not i is None)):

                raise er.FunctionError

        except er.FunctionError:

            print("Specify a name for the gene or its place in the genome")
            print()

        finally:
            
            if i is None: # if gene is specified by name

                i = self.__genome.index(name)

            self.__genome.pop(i)
              
        return None
    
    # change the allele type of a gene by gene name
    def changeAllele(self, geneName:str, newAllele:int):

        self.__genome[geneName].setAllele(newAllele)

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