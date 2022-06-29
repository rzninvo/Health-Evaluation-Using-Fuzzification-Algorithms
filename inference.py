from typing import Dict, Tuple

def get_rule_parameters(rule: str) -> list[str]:
    rule = rule.replace('IF', '')
    rule = rule.replace('(', '')
    rule = rule.replace(')', '')
    rule = rule.replace('THEN', '')
    rule = rule.replace(';', '')
    rule = rule.replace('\n', '')
    rule = rule.split()[2:]
    return rule

def get_rule_value(rule: str, fuzzified_dict: Dict[str, dict]) -> Tuple[str, float]:
    rule_params = get_rule_parameters(rule)
    if 'AND' in rule:
        class_1, condition_1 = rule_params[0], rule_params[2]
        class_2, condition_2 = rule_params[4], rule_params[6]
        value = min(fuzzified_dict[class_1][condition_1], fuzzified_dict[class_2][condition_2])
        return (rule_params[9], value)
    elif 'OR' in rule:
        class_1, condition_1 = rule_params[0], rule_params[2]
        class_2, condition_2 = rule_params[4], rule_params[6]
        value = max(fuzzified_dict[class_1][condition_1], fuzzified_dict[class_2][condition_2])
        return (rule_params[9], value)
    else:
        class_1, condition_1 = rule_params[0], rule_params[2]
        value = fuzzified_dict[class_1][condition_1]
        return (rule_params[5], value)

def heart_disease_check(fuzzified_dict: Dict[str, dict]) -> Dict[str, float | int]:
    output = {f'sick_{i}': 0.0 for i in range(1, 4+1)}
    output['healthy'] = 0.0

    rules = open('rules.fcl', mode='r')
    for rule in rules.readlines():
        if len(rule) <= 0:
            continue
        sickness, value = get_rule_value(rule, fuzzified_dict)
        output[sickness] = max(output(sickness), value)
        
    return output