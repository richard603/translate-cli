'''parse module'''

from textwrap import dedent

def parse(data):
    '''parse data from `request()` into a dict'''
    result = {
        'text': '', 'text_pron': '', 'text_lang': '',
        'text_syno': [], 'text_defi': [], 'text_exam': [],
\
        'trans': '', 'trans_pron': '',
        'trans_all': [], 'trans_verbose': [],
        }

    codes = (
        "result['trans'] = data[0][0][0]",
        "result['text'] = data[0][0][1]",
        "result['text_pron'] = data[0][1][3]",
        "result['trans_pron'] = data[0][1][2]",

        '''\
        for g in data[1][0]:
            word_type = g[0]
            type_synonyms = []
            result['trans_verbose'].append((word_type, type_synonyms))
            for _g in g[2]:
                synonyms = _g[0]
                translation = _g[1]
                result['trans_verbose'][-1][1].append(synonyms, translation)''',

        "result['text_lang'] = data[2]",

        '''\
        for h in data[5][0][2]:
            result['trans_all'].append(h[0])''',

        '''\
        for i in data[11]:
            word_type = i[0]
            type_synonyms = []
            for _i in i[1]:
                type_synonyms.append(_i[0])
            result['text_syno'].append((word_type, type_synonyms))''',

        '''\
        for j in data[12]:
            word_type = j[0]
            type_definitions = []
            for _j in j[1]:
                type_definitions.append(_j[0])
            result['text_defi'].append((word_type, type_definitions))''',
        '''\
        for k in data[13][0]:
            result['text_exam'].append(k[0])'''
        )

    for code in codes:
        try:
            exec(dedent(code))
        except (IndexError, TypeError):
            ...

    return result
