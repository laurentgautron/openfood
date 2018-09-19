
class MonNom:

    def __init__(self, nom):

        self.nom = nom

    @staticmethod
    def ecrire(nom):

        print('je suis: %s'%nom)

class Main:

    MonNom.ecrire('laurent')

if __name__ == '__main__':
    main = Main()