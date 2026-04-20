import math

def fitness_func(x1, x2):
    
    first_part = (math.sin(x1) * math.cos(x2) * math.tan(x1 + x2))
    second_part = math.pow((1/2), 1 - math.sqrt(math.pow(x2, 2)))

    result = - (first_part + second_part)

    return result