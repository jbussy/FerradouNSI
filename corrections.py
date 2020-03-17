from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

from math import sqrt

#------------

# Fonction solution du probleme
def __estPair(n):
    return n%2==0

# Jeu de donnees sur lequel la fonction de l'eleve sera testee
inputs_estPair = [
    Args(1), Args(2), Args(3), Args(8), Args(17), Args(1001)
]

# Fabrication de l'instance pour l'autoevaluation
sol_estPair = ExerciseFunction(
    __estPair,       # La fonction solution du probleme
    inputs_estPair,  # Le jeu de donnees
)

#------------

# Fonction solution du probleme
def __carre(x):
    return x**2

# Jeu de donnees sur lequel la fonction de l'eleve sera testee
inputs_carre = [
    Args(-2), Args(0), Args(1), Args(1.5), Args(17)
]

# Fabrication de l'instance pour l'autoevaluation
sol_carre = ExerciseFunction(
    __carre,       # La fonction solution du problème
    inputs_carre,  # Le jeu de donnees
)
