import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        counts = kwargs.copy()
        self.contents = [ k for k, v in counts.items() for _ in range(v) ]
        self.dtcontents = counts

    def draw(self, nb):
        population = self.contents # no copy
        lng = len(population)

        if nb > lng: return population
                
        rmvlst = random.sample(population, k=nb) # unique
        for im in rmvlst:
            population.remove(im) # removed from original array

        return rmvlst
        

def experiment(hat, 
               expected_balls, 
               num_balls_drawn, 
               num_experiments):

    population = hat.contents[:] # list
    dtpop = hat.dtcontents.copy()
    psize = len(population)

    counts = expected_balls.copy() # dict
    btrlst = [ k for k, v in counts.items() for _ in range(v) ]

    nbd = num_balls_drawn
    probability = 1
    
    allblinbasketcheck = all( map( lambda k: counts[k] <= dtpop[k], counts ) )
    if nbd > psize and allblinbasketcheck: 
        return probability
    
    success = num_experiments    
    tries = range(num_experiments)
    for _ in tries:
        smp = random.sample(population, k=nbd) # list
        for bl in btrlst:
            try:
                smp.remove(bl)
            except:
                # print(bl, "not in smp")
                success -= 1
                break
        # print(success)

    # print("End of loop")

    probability = success / num_experiments
    return probability
