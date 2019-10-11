from textwrap import dedent

def parse(data):
    result = {
            'translation': '',
            'source': '',
            'source_pronunciation': '',
            'target_pronunciation': '',
            'translations_verbose': [],
            'src_language': '',
            'translations': [],
            'synonyms': [], 
            'definitions': [],
            'examples': []
            }

    codes = [
    "result['translation'] = data[0][0][0]",
    "result['source'] = data[0][0][1]",
    "result['source_pronunciation'] = data[0][1][3]",
    "result['target_pronunciation'] = data[0][1][2]",

    '''\
    for g in data[1][0]:
        word_type = g[0]
        type_synonyms = []
        result['translations_verbose'].append((word_type, type_synonyms))
        for _g in g[2]:
            synonyms = _g[0]
            translation = _g[1]
            result['translations_verbose'][-1][1].append(synonyms, translation)''',

    "result['src_language'] = data[2]",

    '''\
    for h in data[5][0][2]:
        result['translations'].append(h[0])''',

    '''\
    for i in data[11]:
        word_type = i[0]
        type_synonyms = []
        for _i in i[1]:
            type_synonyms.append(_i[0])
        result['synonyms'].append((word_type, type_synonyms))''',

    '''\
    for j in data[12]:
        word_type = j[0]
        type_definitions = []
        for _j in j[1]:
            type_definitions.append(_j[0])
        result['definitions'].append((word_type, type_definitions))''',
    '''\
    for k in data[13][0]:
        result['examples'].append(k[0])'''
            ]

    for code in codes:
        try:
            exec(dedent(code))
        except IndexError:
            ...
        except TypeError:
            ...

    return result

