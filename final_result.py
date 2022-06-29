from fuzzification import *
from inference import heart_disease_check

class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        fuzzyfied_dict = get_fuzzyfied_set(input_dict)
        return str(heart_disease_check(fuzzyfied_dict))
