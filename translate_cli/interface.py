#!/usr/bin/env python3

import sys
import argparse
import os.path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))
from translate_cli import translate
from translate_cli.format import BOLD, ITALIC, UNDERLINE
from translate_cli.lang_codes import LANG_MAP

def list_codes():
    for index, i in enumerate(LANG_MAP.items()):
        if index % 2 == 0:
            print(f'{i[1]["name"]:20} \
-->   {UNDERLINE.format(BOLD.format(i[0])):3}', end=f'{"":3}')
        else:
            print(f'{i[1]["name"]:20} \
-->   {UNDERLINE.format(BOLD.format(i[0])):3}')

def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        prog='trans',
        description='A simple cli tool to translate',
        usage='trans [OPTIONS] [SOURCES]:[TARGETS] [TEXT]...',
        epilog="""examples:
    trans awesome :fr
        translate 'awesome' to French
    trans python -d
        lookup 'python' using dictionary mode""",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        '-l', '--list',
        action='store_true',
        help='list supported language codes'
    )
    parser.add_argument(
        '-d', '--dictionary-mode',
        action='store_true',
        default=False,
        help='dictionary mode'
    )
    parser.set_defaults(
        src_lang='auto',
        dst_lang='en'
    )
    args, texts = parser.parse_known_args(argv)

    if args.list:
        list_codes()
        sys.exit(0)
    for text in texts[:]:
        if ':' in text:
            languages = text.split(':')
            args.src_lang = languages[0] if languages[0] else 'auto'
            args.dst_lang = languages[1] if languages[1] else 'en'
            texts.remove(text)
    if not texts:
        parser.print_help()
        sys.exit(0)
    args.text = ' '.join(texts)
    if not LANG_MAP.get(args.src_lang) or not LANG_MAP.get(args.dst_lang):
        raise ValueError('Invalid language code.')
    return args

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

    text_lang = LANG_MAP[translation['text_lang'][:2]]['name'] \
    if LANG_MAP.get(translation['text_lang'][:2]) \
    else translation['text_lang']
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
    args = parse_args(argv)
    translation = translate(args.text, args.src_lang, args.dst_lang)
    translation['trans_lang'] = args.dst_lang
    if args.dictionary_mode:
        dict_print(translation)
    else:
        trans_print(translation)

if __name__ == '__main__':
    sys.exit(main())
