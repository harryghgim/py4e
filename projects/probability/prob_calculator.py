import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        contents = list()
        counts = dict()
        for k in kwargs:
            counts[k] = counts.get(k, 0) + 1
        for k, v in counts.items():
            for _ in range(v):
                contents.append(k)
                
        self.contents = contents

    def draw(self, nb):
        population = self.contents
        rmvlst = list()
        lng = len(population)

        if nb > lng: return population
                
        rmvlst = random.choices(population, k=nb)
        for it in rmvlst:
            self.contents.remove(it) # remove from original array

        return rmvlst
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 1
    return probability
