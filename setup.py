from distutils.core import setup
setup(
  name = 'langchain_discord',         # How you named your package folder (MyLib)
  packages = ['langchain_discord'],   # Chose the same as "name"
  version = '0.0.14',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This package offers some easy-to-use tools to integrate Discord into LangChain for agents.',   # Give a short description about your library
  author = 'Lennard Dorst',                   # Type in your name
  author_email = 'lennardsolana@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/0w9/langchain-discord',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['AI', 'LangChain', 'Discord'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'langchain',
          'typing',
    ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)