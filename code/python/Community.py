## Ford Fishman
## Class for community: sets of strains

import Error as er
import Strain
import numpy as np


class Community:

    """
    Constructor
    -----------
    strains (dict): dictionary of strain_id:strain
    richness (int): number of strains present in the community
    """
    def __init__(self, strains:dict):

        self.__strains = strains
        self.__richness = len(self.__strains)
        self.__selection_gradient = {}
        self.initializeGradient()

    """
    Attributes
    ----------
    richness (int) - number of strains in the community
    """

    def getStrain(self, strainName): return self.__strains[strainName]

    def richness(self): return self.__richness
        

    """
    Functions
    """

    def speciate(self, strainName:str, newStrainName:str, changeSSU:bool, geneName:str=""):
        """
        take a strain from the community and change it by one allele
        changeSSU (boolean): is the speciation due to change in SSU?
        """
        focal_strain = self.__strains[strainName]
        if changeSSU:

            new_strain = focal_strain.changeSSU()

        else:

            focal_gene = focal_strain.getGene(geneName)
            new_allele = focal_gene.allele() + 1 # change this to be more complicated
            new_strain = focal_strain.changeAllele(geneName=geneName, newAllele=new_allele)

        self.__strains[newStrainName] = new_strain
        self.__richness += 1

        return None

    def initializeGradient(self):
        """
        Initializes relative fitness gradient of the population
        All alleles start as equals
        """
        for strain in self.__strains:

            genome = strain.genome()
            
            for gene in genome:

                gene_name = gene.name()
                allele_name = gene.allele()
                # new genes start at relative fitness of 1
                if gene_name not in self.__selection_gradient:
                    # nested dictionary - gene_name: allele_name: relative fitness
                    self.__selection_gradient[gene_name] = {allele_name:1} 

                elif allele_name not in self.__selection_gradient[gene_name]:
                    self.__selection_gradient[gene_name][allele_name] = 1

        return None
                
    def randomSelection(self):
        """
        Picks random allele and changes its fitness to a random value normally distributed around
        the previous value. 
        """
        # Pick a random allele
        gene_names = list(self.__selection_gradient.keys()) # take the gene names of the population
        focal_gene_ind = np.random.choice(range(1,len(gene_names))) # pick a random gene
        focal_gene = gene_names[focal_gene_ind]
        allele_names = list(self.__selection_gradient[focal_gene].key())
        allele_ind = np.random.choice(range(1,len(allele_names))) # pick a random allele of the gene
        focal_allele = allele_names[allele_ind]
        # change the relative fitness of that gene
        rel_fit = -1 # start off fit at non-reasonable number for while loop
        while rel_fit < 0:

            rel_fit = np.random.normal( # use a normal distribution around the starting fitness
                loc = self.__selection_gradient[focal_gene][focal_allele],
                scale = 0.2
                )

        self.__selection_gradient[focal_gene][focal_allele] = rel_fit # assign allele new rel_fit 

        return None       

