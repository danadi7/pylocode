# PyLocode
---
The United Nations Code for Trade and Transport Locations, otherwise known as the UN/LOCODE, is used by major shipping companies, freight forwarders, and the manufacturing industry around the world. Each code consists of 5 characters - the first two indicate the country, while the last 3 indicate the name of the place. Examples include FRPAR, USNYC, and JPTYO.

This library makes it easier to work with UN/LOCODE in Python, by providing the entire list of codes, and methods for easy lookup.
---
## Usage
Looking up location name by UN/LOCODE:
```
> from pylocode import get_name_by_locode
> get_name_by_locode('SGPPT')
'PASIR PANJANG Terminal'
```

Looking up country name by UN/LOCODE:
```
> from pylocode import get_name_by_locode
> get_name_by_locode('SGPPT')
'SINGAPORE'
```
