from typing import Dict, List, Optional

def linier_function(x: float, x1: float, y1: float, x2: float, y2: float) -> float:
    '''
        calculate the y of given x for \ 
        the linier function, which specified with given points
    '''
    return y2 + ((y1 - y2)*(x - x2))/(x1 - x2)

def fuzzify(data, points: list, curve: str) -> float:
    if curve == 'ascending':
        if data <= points[0]:
            return 0.0
        elif data > points[0] and data <= points[1]:
            return linier_function(data, points[0], 0, points[1], 1)
        else:
            return 1.0
    if curve == 'descending':
        if data <= points[1]:
            return 1.0
        elif data > points[0] and data <= points[1]:
            return linier_function(data, points[0], 1, points[1], 0)
        else:
            return 0.0
    if curve == 'spiked':
        if data < points[0] or data > points[2]:
            return 0.0
        elif data >= points[0] and data < points[1]:
            return linier_function(data, points[0], 0, points[1], 1)
        else:
            return linier_function(data, points[1], 1, points[2], 0)

def calculate_fuzzy_values(data, sickness_stages: Dict[str, float]) -> Dict[str, float]:
    output = dict()
    
    for key in sickness_stages.keys():
        curve_type = sickness_stages[key][1]
        output[key] = fuzzify(data, sickness_stages[key][0], curve_type)
            
    return output

def age_fuzzification(age: str) -> Dict[str, float]:
    sickness_stages = dict()
    
    sickness_stages['young'] = [[29, 38], 'descending']
    sickness_stages['mild'] = [[33, 38, 45], 'spiked']
    sickness_stages['old'] = [[40, 48, 58], 'spiked']
    sickness_stages['very_old'] = [[52, 60], 'ascending']
    
    return calculate_fuzzy_values(int(age), sickness_stages)

def blood_pressure_fuzzification(pressure: str) -> Dict[str, float]:
    sickness_stages = dict()
    
    sickness_stages['low'] = [[111, 134], 'descending']
    sickness_stages['medium'] = [[127, 139, 153], 'spiked']
    sickness_stages['high'] = [[142, 157, 172], 'spiked']
    sickness_stages['very_high'] = [[154, 171], 'ascending']
    
    return calculate_fuzzy_values(int(pressure), sickness_stages)

def blood_sugar_fuzzification(sugar: str) -> Dict[str, float]:
    sickness_stages = dict()
    sickness_stages['true'] = [[105, 120], 'ascending']
    sickness_stages['false'] = [[105, 120], 'descending']
    
    return calculate_fuzzy_values(int(sugar), sickness_stages)

def cholestrol_fuzzification(cholestrol: str) -> Dict[str, float]:
    sickness_stages = dict()
    
    sickness_stages['low'] = [[151, 197], 'descending']
    sickness_stages['medium'] = [[188, 215, 250], 'spiked']
    sickness_stages['high'] = [[217, 263, 307], 'spiked']
    sickness_stages['very_high'] = [[281, 347], 'ascending']
    
    return calculate_fuzzy_values(int(cholestrol), sickness_stages)

def heart_rate_fuzzification(rate: str) -> Dict[str, float]:
    sickness_stages = dict()
    
    sickness_stages['low'] = [[100, 141], 'descending']
    sickness_stages['medium'] = [[111, 152, 194], 'spiked']
    sickness_stages['high'] = [[152, 210], 'ascending']
    
    return calculate_fuzzy_values(int(rate), sickness_stages)

def ecg_fuzzification(ecg: str) -> Dict[str, float]:
    sickness_stages = dict()
    
    sickness_stages['normal'] = [[0, 0.4], 'descending']
    sickness_stages['abnormal'] = [[0.2, 1, 1.8], 'spiked']
    sickness_stages['hypertrophy'] = [[1.4, 1.9], 'ascending']
    
    return calculate_fuzzy_values(float(ecg), sickness_stages)

def old_peak_fuzzification(old_peak: str) -> Dict[str, float]:
    sickness_stages = dict()
    
    sickness_stages['low'] = [[1, 2], 'descending']
    sickness_stages['risk'] = [[1.5, 2.8, 4.2], 'spiked']
    sickness_stages['terrible'] = [[2.5, 4], 'ascending']
    
    return calculate_fuzzy_values(float(old_peak), sickness_stages)

def chest_pain_fuzzification(pain: str) -> Dict[str, int]:
    sickness_kinds = ['typical_anginal', 'atypical_anginal', 'non_anginal_pain', 'asymptomatic']
    output = {k: 0 for k in sickness_kinds}
    output[sickness_kinds[int(pain)-1]] = 1
    return output

def exercise_fuzzification(exercise: str) -> Dict[str, int]:
    sickness_kinds = ['false', 'true']
    output = {k: 0 for k in sickness_kinds}
    output[sickness_kinds[int(exercise)-1]] = 1
    return output

def thallium_fuzzification(amount: str) -> Dict[str, int]:
    sickness_kinds = ['normal', 'medium', 'high']
    if amount in [0, 1, 2, 3]: amount = 1;
    elif amount in [4, 5, 6]: amount = 2;
    else: amount = 3;
    output = {k: 0 for k in sickness_kinds}
    output[sickness_kinds[int(amount)-1]] = 1
    return output

def sex_fuzzification(sex: str) -> Dict[str, int]:
    sickness_kinds = ['male', 'female']
    output = {k: 0 for k in sickness_kinds}
    output[sickness_kinds[int(sex)-1]] = 1
    return output

def get_fuzzyfied_set(input_dict: dict):
    output = dict()
    for key in input_dict.keys():
            output[key] = FUNCTIONS[key](input_dict[key])
    return output


FUNCTIONS = {'chest_pain': chest_pain_fuzzification, 'cholestrol': cholestrol_fuzzification, 
                  'ecg': ecg_fuzzification, 'exercise': exercise_fuzzification, 'thallium_scan': thallium_fuzzification, 
                  'age': age_fuzzification, 'blood_pressure': blood_pressure_fuzzification, 'blood_sugar': blood_sugar_fuzzification, 
                  'heart_rate': heart_rate_fuzzification, 'old_peak': old_peak_fuzzification, 'sex': sex_fuzzification}