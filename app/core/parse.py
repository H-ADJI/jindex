'''
File: parse.py
File Created: Wednesday, 1st February 2023 7:02:12 pm
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''
from app.utils.constants import SPEACIAL_SEPARATOR


def normalize_text(text: str | list[str]):
    if isinstance(text, list):
        # removing white spaces from each text element
        text = map(str.strip, text)
        # joining text by this special separator
        text = SPEACIAL_SEPARATOR.join(text)
        return text
    return text.strip()
