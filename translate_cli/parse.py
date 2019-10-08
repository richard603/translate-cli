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

    try:
        result['translation'] = data[0][0][0]
    except IndexError:
        pass
    except TypeError:
        pass

    try:
        result['source'] = data[0][0][1]
    except IndexError:
        pass
    except TypeError:
        pass

    try:
        result['source_pronunciation'] = data[0][1][3]
    except IndexError:
        pass
    except TypeError:
        pass

    try:
        result['target_pronunciation'] = data[0][1][2]
    except IndexError:
        pass
    except TypeError:
        pass

    try:
        for g in data[1][0]:
            word_type = g[0]
            type_synonyms = []
            result['translations_verbose'].append((word_type, type_synonyms))
            for _g in g[2]:
                synonyms = _g[0]
                translation = _g[1]
                result['translations_verbose'][-1][1].append(synonyms, translation)
    except IndexError:
        pass
    except TypeError:
        pass

    try:
        result['src_language'] = data[2]
    except IndexError:
        pass
    except TypeError:
        pass

    try:
        for h in data[5][0][2]:
            result['translations'].append(h[0])
    except IndexError:
        pass
    except TypeError:
        pass

    try:
        for i in data[11]:
            word_type = i[0]
            type_synonyms = []
            for _i in i[1]:
                type_synonyms.append(_i[0])
            result['synonyms'].append((word_type, type_synonyms))
    except IndexError:
        pass
    except TypeError:
        pass

    try:
        for j in data[12]:
            word_type = j[0]
            type_definitions = []
            for _j in j[1]:
                type_definitions.append(_j[0])
            result['definitions'].append((word_type, type_definitions))
    except IndexError:
        pass
    except TypeError:
        pass

    try:
        for k in data[13][0]:
            result['examples'].append(k[0])
    except IndexError:
        pass
    except TypeError:
        pass

    return result

