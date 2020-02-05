## Ford Fishman
## Class for community: sets of strains

import Error as er
import Strain


class Community:

    """
    Constructor
    -----------
    strains (dict): dictionary of strain_id:strain
    """
    def __init__(self, strains:dict):

        self.__strains = strains
        self.__richness = len(self.__strains)

    """
    Attributes
    ----------
    richness (int) - number of strains in the community
    """

    def strains(self):
        return self.__strains

    def richness(self):
        return self.__richness

    """
    Functions
    """

    # take a strain from the community and change it by one allele
    def speciate(self, strainName:str, geneName:str, newStrainName:str):

        focal_strain = self.__strains[strainName]
        focal_gene = focal_strain.getGene(geneName)
        new_allele = focal_gene.allele() + 1 # change this to be more complicated
        new_strain = focal_strain.changeAllele(geneName=geneName, newAllele=new_allele)
        self.__strains[newStrainName] = new_strain
        self.__richness += 1

        return None