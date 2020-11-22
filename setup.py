from distutils.core import setup

setup(
  name = 'DEL.py',
  packages=['delpy'],
  version = '0.0.5',
  license='MIT',
  description = 'API wrapper for discordextremelist',
  author = 'Moksej',
  author_email = 'moksej@gmail.com',
  url = 'https://github.com/TheMoksej/delpy-test',
  download_url = 'https://github.com/TheMoksej/delpy-test.git',
  install_requires=['aiohttp'],
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
)