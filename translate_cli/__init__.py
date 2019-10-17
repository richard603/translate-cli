'''a lightweight command-line translator'''

__version__ = '1.0.4'

from . import request, parse

def translate(text, src_lang='auto', dst_lang='en'):
    '''Return a dict that consists of:

    - text
        original text
    - text_pron
        pronunciation of the text(if there is)
    - text_lang
        original language of the text
    - text_syno
        synonyms of the text(only if it's a word)
    - text_defi
        definitions of the text(only if it's a word)
    - text_exam
        example uses of the text(only if it's a word)

    - trans
        translation of the text
    - trans_pron
        pronunciation of the translation
    - trans_all
        all translations of the text
    - trans_verbose
        all translations of the text, and synonyms(in original language)
    for each translation
    '''
    return parse.parse(request.request(text, src_lang, dst_lang))
