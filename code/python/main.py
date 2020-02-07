## Ford Fishman
## run simulation

import rRNA; import Gene; import Strain; import Strain; import Community
import Error as er
import numpy as np

"""
Parameters
"""
ssuChange = 0.006
alleleChange = 0.02
fitnessChange = 0.05
geneAddition = 0
geneRemoval = 0 

time = 0

rate = ssuChange + alleleChange + fitnessChange + geneAddition + geneRemoval
"""
Main function for running simulation
"""
def main():

    initialize()
    
    return None

def initialize(numStrains:int=1):

    seq = rRNA.rRNA(length=5)
    print(seq.seq())
    gene = Gene.Gene("A",1)
    strain = Strain.Strain(name="asdasd",genome={gene.name():gene},ssu=seq)
    community = Community.Community({strain.name():strain})
    print(community.richness())
    community.speciate(strainName=strain.name(),newStrainName="B", changeSSU = True)
    print(community.richness())
    print(community.getStrain(strain.name()).ssu().seq())

    return None


"""
Execute main function
"""
if __name__ == "__main__":
    main()

def event():
    """

    """
    