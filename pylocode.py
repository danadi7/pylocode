from countries import countries
from locode import locode

def get_name_by_locode(code):
    country = code[:2]
    port_code = code[2:]
    return locode.get(country).get(port_code)
