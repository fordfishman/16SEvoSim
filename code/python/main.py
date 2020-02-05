## Ford Fishman
## run simulation

import Strain
import rRNA
import Gene
import Strain
import Community
import Error as er

"""
Main function for running simulation
"""
def main():

    initialize()
    
    return None

def initialize(numStrains:int=1):

    seq = rRNA.rRNA(length=20)
    gene = Gene.Gene("A",1)
    strain = Strain.Strain(name="asdasd",genome={gene.name():gene},ssu=seq)
    community = Community.Community({strain.name():strain})
    print(community.richness())
    community.speciate(strainName=strain.name(),geneName=gene.name(),newStrainName="B")
    print(community.richness())

    return None


"""
Execute main function
"""
if __name__ == "__main__":
    main()
    