from typing import Dict, Tuple
from fuzzification import fuzzify
import numpy as np

def sick_1_fuzzify(x: float, mu: float) -> float:
    return min(mu, fuzzify(x, [0, 1, 2], 'spiked'))

def sick_2_fuzzify(x: float, mu: float) -> float:
    return min(mu, fuzzify(x, [1, 2, 3], 'spiked'))

def sick_3_fuzzify(x: float, mu: float) -> float:
    return min(mu, fuzzify(x, [2, 3, 4], 'spiked'))

def sick_4_fuzzify(x: float, mu: float) -> float:
    return min(mu, fuzzify(x, [3, 3.75], 'ascending'))

def healthy_fuzzify(x: float, mu: float) -> float:
    return min(mu, fuzzify(x, [0.25, 1], 'descending'))

KINDS_FUNCTIONS = {'sick_1': sick_1_fuzzify, 'sick_2': sick_2_fuzzify,
                   'sick_3': sick_3_fuzzify, 'sick_4': sick_4_fuzzify, 'healthy': healthy_fuzzify, }


def get_centroid(mu_s: Dict[str, float], period: Tuple[float, float] = (0, 4,), accuracy: float = 0.02) -> float:
    x = period[0]
    
    sum_1, sum_2 = 0, 0
    points = np.linspace(period[0], period[1], int((period[1] - period[0])/accuracy))
    for x in points:
        temp = max([f(x, mu_s[k]) for k, f in KINDS_FUNCTIONS.items()])
        
        sum_1 += temp*x
        sum_2 += temp
        
    return sum_1/sum_2