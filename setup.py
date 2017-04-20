from setuptools import setup

with open('requirements.txt','rb') as f:
      requirements = f.read()
setup(name='Dashboard',
      version='1.0',
      description='Dashbord App',
      author='Cesar Herdenez',
      author_email='Caherdenez@gmail.com',
      url='http://cesarh.co',
      install_requires= requirements,
     )
