import distutils.sysconfig
env = Environment()
env.Replace(CXX = 'g++')
env.Append(CCFLAGS =  '-O3 -Wall')
env.SharedLibrary('pkgtest/lib/hello',['pkgtest/hello.c'])
Default('.')