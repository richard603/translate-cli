import setuptools

with open('README.rst', 'r') as f:
    README = f.read()

setuptools.setup(
        name = 'translate-cli',
        version = '0.0.1',
        author = 'Harryl',
        author_email = 'harryl.mail@protonmail.com',
        description = 'A lightweight cli translate tool',
        long_description = README,
        packages = setuptools.find_packages(),
        py_modules = [
            'translate_cli.lang_map',
            'translate_cli.format'
        ],
        scripts = ['trans'],
        classifiers = [
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Operating System :: OS Independent',
            'Development Status :: 4 - Beta',
            'Environment :: Console',
        ],
        url = 'https://github.com/harrylw/translate-cli',
        python_requires = '>=3.6',
)
