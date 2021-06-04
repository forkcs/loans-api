from setuptools import setup, find_packages

setup(
    name='loans-api',
    version='0.1',
    packages=find_packages(),
    author='Fedor Soldatkin',
    author_email='forkcs@yandex.ru',
    scripts=['loans_api/main.py'],
    install_requires=[
        'bottle==0.12.19',
        'pony==0.7.14'
    ]
)
