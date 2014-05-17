from setuptools import setup, find_packages
import brutus

setup(name='brutus',
      version=brutus.__version__,
      classifiers=[
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Operating System :: OS Independent'],
      author='Sarah Janes, LLC.',
      author_email='sarahjanesllc@gmail.com',
      description="Farmers Market software stack",
      long_description=open("README.md").read(),
      url='https://github.com/sarahjanesllc-labs/brutus',
      license='MIT',
      packages=find_packages(),
      install_requires=["PyYAML", "requests", "tornado", "sqlalchemy"],
      entry_points={
          "console_scripts": [
              'brutus = brutus.cli:main']},
      )
