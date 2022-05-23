class Client:
    def __init__(self, nom, prenom, age, adresse, identifiant):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse
        self.identifiant = identifiant
        self.comptes = {}

    def creer_compte(self, compte):
        pass

    def donner_solde_compte(self, numero_compte):
        pass
