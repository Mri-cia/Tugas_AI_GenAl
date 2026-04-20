import math
import util 
import decode as dc
import fitness as ft
import probability as pb

import case_domain as dom

# Pintu Utama
def main():

    # Decode semua populasi awal
    list_decode = []

    for i in range (0, len(dom.populasiAwal)):
        list_x = []

        for j in range (0, len(dom.populasiAwal[i])):
            list_x.append(dc.decode_cromosome(util.to_bin(dom.populasiAwal[i][j])))
        
        list_decode.append(list_x)

    list_fit = []

    for i in range (0, len(dom.populasiAwal)):
        list_fit.append(ft.fitness_func(list_decode[i][0], list_decode[i][1]))

    print(list_fit)

    list_prob = []

    for f in list_fit:
        list_prob.append(pb.probability_function(f, list_fit))

    print(list_prob)

if __name__=="__main__":
    main()