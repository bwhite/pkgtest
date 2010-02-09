from distutils.core import setup
setup(name='pkgtest',
      version='1.0',
      packages=['pkgtest'],
      package_data = {'pkgtest' : ['lib/*']}
      )
