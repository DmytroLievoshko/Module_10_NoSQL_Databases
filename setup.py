from setuptools import setup, find_namespace_packages

setup(name='pyCliAddressBook',
      version='1.0.2',
      description='Personal assistant with command line interface',
      url='https://github.com/DmytroLievoshko/Module_9_Object_Relational_Mapping.git',
      author='Dmytro Levoshko',
      author_email='contract@restriction.com',
      license='MIT',
      packages=find_namespace_packages(),
      include_package_data=True,
      install_requires=['prompt-toolkit<=3.0.31', 'phonenumbers<=8.12.55'],
      entry_points={'console_scripts': [
          'assistant=pyCliAddressBook.main:cli']}
      )
