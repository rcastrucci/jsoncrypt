from distutils.core import setup
setup(
  name = 'jsoncrypt',         
  packages = ['jsoncrypt'],   
  version = '0.1',      
  license='MIT',        
  description = 'Encryption and Decryption of JSON files. Option of reading JSON files encrypted and adding a password.',
  author = 'Renne C. (GRC Algoritmos)',                   
  author_email = 'grc.algoritmos@gmail.com',      
  url = 'https://github.com/grc-algoritmos/jsoncrypt',   
  download_url = 'https://github.com/grc-algoritmos/jsoncrypt/archive/refs/tags/v_01.tar.gz',
  keywords = ['JSON', 'ENCRYPTION', 'DECRYPTION', 'ENCODE', 'OBFUSCATE'],   
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha', # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
