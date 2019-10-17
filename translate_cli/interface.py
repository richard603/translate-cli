#!/usr/bin/env python3

import sys
import os.path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))
from translate_cli import translate
from translate_cli.format import BOLD, ITALIC, UNDERLINE
from translate_cli.lang_codes import LANG_MAP

def get_help():
    print('''usage: trans [OPTIONS] [SOURCE_LANGUAGE]:[TARGET_LANGUAGE] [TEXT]
    A simple cli tool to translate text with google translate
OPTIONS:
    -h, --help
        print help message
    -d, --dict
        dictionary mode
    -l, --list
        list supported language codes
EXAMPLES:
    trans awesome :fr
        translate 'awesome' to French
    trans python -d
        lookup 'python' using dictionary mode''')
    sys.exit(0)

def list_codes():
    for index, i in enumerate(LANG_MAP.items()):
        if index % 2 == 0:
            print(f'{i[1]["name"]:20} \
-->   {UNDERLINE.format(BOLD.format(i[0])):3}', end=f'{"":3}')
        else:
            print(f'{i[1]["name"]:20} \
-->   {UNDERLINE.format(BOLD.format(i[0])):3}')
    sys.exit(0)

def parse_args(argv=None):
    args = argv if argv else sys.argv[1:]
    global dictionary_mode
    dictionary_mode = False
    src_lang, dst_lang = 'auto', 'en'

    for arg in args[:]:
        if arg in ('-h', '--help'):
            get_help()
        elif arg in ('-l', '--list'):
            list_codes()
        elif arg in ('-d', '--dict'):
            dictionary_mode = True
            args.remove(arg)
        if ':' not in arg:
            continue
        languages = arg.split(':')
        src_lang = languages[0] if languages[0] else 'auto'
        dst_lang = languages[1] if languages[1] else 'en'
        args.remove(arg)

    if not args:
        get_help()
    if not LANG_MAP.get(src_lang) or not LANG_MAP.get(dst_lang):
        raise ValueError('Invalid language code.')
    text = ' '.join(args)

    return text, src_lang, dst_lang

def dict_print(translation):
    text = translation['text']

    text_pron = translation['text_pron']\
    if translation['text_pron'] and \
        isinstance(translation['text_pron'], str) else None

    print(text)
    if text_pron:
        print(f'/{ITALIC.format(text_pron)}/')
    print()
    for i in translation['text_defi']:
        print(i[0])
        for _i in i[1]:
            print(f'{" ":4}{_i}\n')

    if translation['text_syno']:
        print('Synonyms')
    for j in translation['text_syno']:
        print(f'{" ":4}{j[0]}')
        for _j in j[1]:
            print(f'{" ":8}- {BOLD.format(", ".join(_j))}')
        print()

    if translation['text_exam']:
        print('Example')
    for k in translation['text_exam']:
        k = k.replace('<b>', '\033[1m\033[4m')
        k = k.replace('</b>', '\033[0m')
        print(f'{" ":4}- {k}\n')


def trans_print(translation):
    text = translation['text']

    text_lang = LANG_MAP[translation['text_lang']]['name']
    text_pron = translation['text_pron']\
    if translation['text_pron'] and \
        isinstance(translation['text_pron'], str) else None

    trans = translation['trans']
    trans_lang = LANG_MAP[translation['trans_lang']]['name']
    trans_all = ', '.join(translation['trans_all'])

    trans_pron = translation['trans_pron']\
    if translation['trans_pron'] and \
        isinstance(translation['trans_pron'], str) else None

    print(text)
    if text_pron:
        print(f'/{ITALIC.format(text_pron)}/')
    print()
    print(f'{BOLD.format(trans)}')
    if trans_pron:
        print(f'/{ITALIC.format(trans_pron)}/')
    print()
    print(f'Translation of {UNDERLINE.format(text)}')
    print(f'[ {UNDERLINE.format(text_lang)} -> {BOLD.format(trans_lang)} ]')
    print()
    print(f'{UNDERLINE.format(text)}')
    print(f'    {BOLD.format(trans_all)}')

def main(argv=None):
    arguments = parse_args(argv)
    translation = translate(*arguments)
    translation['trans_lang'] = arguments[2]
    if dictionary_mode:
        dict_print(translation)
    else:
        trans_print(translation)

if __name__ == '__main__':
    sys.exit(main())
