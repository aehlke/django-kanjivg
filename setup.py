from setuptools import find_packages, setup
import os

setup(
    name='django-kanjivg',
    description='KanjiVG support lib for Manabi.',

    author='Alex Ehlke',
    author_email='alex.ehlke@gmail.com',
    url='http://github.com/aehlke/kanjivg',
    license='BSD',
    #packages=find_packages(exclude=['ez_setup']),
    packages=['kanjivg'],
    #namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django==1.3',
        'lxml',
    ],
)

