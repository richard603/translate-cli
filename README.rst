Translate-Cli
=============
Translate-cli is a lightweight command-line translator written in Python. Using Google's public translate API as source.


Features
--------
- Translate words, sentences inside your shell.

- Detect source language automaticly.

- Dictionary mode.

- Formatted output (refered to `Translate Shell`_)

- SSL Default, query text with HTTPS instead of insecure HTTP.

- Also available as a Python module.


Installation
------------
::

    $ [sudo] pip install translate-cli


Getting Started
---------------
Translate text::

    $ trans Nothing is impossible :zh
    Nothing is impossible

    没有什么是不可能的
    /Méiyǒu shé me shì bù kěnéng de/

    Translations of Nothing is impossible
    [ English -> Chinese ]

    Nothing is impossible
        没有什么是不可能的, 一切皆有可能

Lookup a word::

    $ trans bonjour -d
    bonjour

    noun
        Formule de salutation utilisée pendant la journée.

    Synonyms
        noun
            - salut
            - dodo, salut, adieu, au revoir
            - après-midi
            - matin, matinée

    Example
        - Dire bonjour .


Use As A Python Module
----------------------
::

    >>> import translate_cli
    >>> translate_cli.translate("whatever you want to translate", source_language, target_language)

Then you will get a dict as return, which consists of:
::

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


.. _Translate Shell: https://github.com/soimort/translate-shell
