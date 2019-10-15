import setuptools

with open('README.rst', 'r') as f:
    README = f.read()

setuptools.setup(
        name='translate-cli',
        version='1.0.3',
        author='Harryl',
        author_email='harryl.mail@protonmail.com',
        description='A lightweight cli translate tool',
        long_description=README,
        packages=setuptools.find_packages(),
        entry_points={
            'console_scripts': [
                'trans=translate_cli.interface:main',
            ]
        },
        classifiers=[
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Operating System :: OS Independent',
            'Environment :: Console',
        ],
        url='https://github.com/harrylw/translate-cli',
        python_requires='>=3.6',
)
