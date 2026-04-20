import math
import random

import util 
import initialization as initpop
import decode as dc
import fitness as ft
import probability as pb
import wheel as rw

import case_domain as dom

# Pintu Utama
def main():

    print("="*160)
    print(f"{'GEN':^5} | {'BEST Steering':^12} | {'BEST Angle':^12} | {'MIN COST f(x)':^15} | {'Best Cromosome':^90}")
    print("="*160)

    # Inisialisasi populasi kromosom
    population_cromosome = initpop.initialize_from_fixed(dom.populasiAwal)

    for g in range(dom.GENERATIONS+1):
        display_data = []

        # Decode dan fitness
        undressed_cromosome = []
        list_fit = []
        
        for c in population_cromosome:
            b1 = c[:dom.BITS_PER_VAR]
            b2 = c[dom.BITS_PER_VAR:]

            # Decode
            x1 = dc.decode_cromosome(b1, dom.DOMAIN[0], dom.DOMAIN[1])
            x2 = dc.decode_cromosome(b2, dom.DOMAIN[0], dom.DOMAIN[1])
            undressed_cromosome.append((x1, x2))
            # Fitness
            list_fit.append(ft.fitness_func(x1, x2))

    
        parents = []
        for _ in range(dom.POP_SIZE):
            candidates = random.sample(list(range(dom.POP_SIZE)), dom.TOURNAMENT_SIZE)
            winner_idx = min(candidates, key=lambda i: list_fit[i])
            parents.append(population_cromosome[winner_idx])

        best_idx = list_fit.index(min(list_fit))
        best_x1, best_x2 = undressed_cromosome[best_idx]

        ix = population_cromosome[best_idx]

        print(f"{g:^5} | {best_x1:^13.4f} | {best_x2:^12.4f} | {min(list_fit):^15.6f} | {str(ix):>20} ")

    
        # Perpindahan pada generasi baru
        next_gen = []
        for i in range(0, dom.POP_SIZE, 2):
            p1, p2 = parents[i], parents[i+1]
            cp = random.randint(1, dom.TOTAL_BITS - 1)
            c1, c2 = p1[:cp] + p2[cp:], p2[:cp] + p1[cp:]
            
            # Mutation
            for child in [c1, c2]:
                if random.random() < dom.MUTATION_RATE:
                    idx = random.randint(0, dom.TOTAL_BITS - 1)
                    child[idx] = 1 - child[idx]
                next_gen.append(child)
    
        population_cromosome = next_gen



if __name__=="__main__":
    main()