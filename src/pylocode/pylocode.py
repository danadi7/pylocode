from countries import countries
from locodes import locodes

def _clean(code):
    if len(code) > 6 or (len(code) == 6 and code[2] != " "):
        raise ValueError("Not a valid country code")
    return code.upper()

def _extract_country_code(code):
    return code[:2]

def _extract_location_code(code):
    return code[-3:]

def get_name_by_locode(code):
    code = _clean(code)
    country = _extract_country_code(code)
    port_code = _extract_location_code(code)
    name = locodes.get(country).get(port_code)
    if not name:
        raise ValueError("Not a valid locode")
    return name

def get_country_name_by_country_code(code):
    code = _clean(code)
    name = countries.get(code)
    if not name:
        raise ValueError("Not a valid country code")
    return name

def get_country_name_by_locode(code):
    code = _clean(code)
    country = _extract_country_code(code)
    name = countries.get(country)
    if not name:
        raise ValueError("Not a valid locode")
    return name
