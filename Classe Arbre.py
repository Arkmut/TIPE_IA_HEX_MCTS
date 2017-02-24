
#pour mettre des couleurs dans la console
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#un noeud d'un arbre contient: les coords de la case où le coup est joué,
# et la liste des coups possibles à partir de ce coup (fils)
class Arbre:
    def __init__(self,racine):
        self.racine = racine
        self.fils = []
        self.isSelected=False;#sert au debug
    
    def ajout(self,elements):
        (self.fils).append(elements)
    #gaffe aux params par defaut!!
    def affiche(self, nEtage):
        if self.fils == []:
            if(self.isSelected):
                print("   " * nEtage, bcolors.WARNING+self.racine + bcolors.ENDC)
            else:
                print("   " * nEtage, self.racine)
        else:
            if(self.isSelected):
                print("   " * nEtage, bcolors.WARNING+self.racine + bcolors.ENDC)
            else:
                print("   " * nEtage, self.racine)
            for elt in self.fils:
                elt.affiche(nEtage + 1)
    def afficheRacine(self):
        print(self.racine)
