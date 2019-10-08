from . import request
from . import parse


def translate(text, source_lang = 'auto', target_lang = 'en'):
    '''return a dict that consists of:
    - translation
    - source
    - source_pronunciation
    - target_pronunciation
    - translations_verbose
    - src_language
    - translations
    - synonyms
    - definitions
    - examples'''
    return parse.parse(request.request(text, source_lang, target_lang))

