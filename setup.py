import os
from setuptools import setup 

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(name='lemons',
      version='0.1.0',
      description='dl framework for non-normies of ai, dependencies free',
      author='Y0N1N1',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages = ['lemons'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
      ],
      install_requires=[],
      python_requires='>=3.8',
      extras_require={
        'dev': [
            "math",
            "os",
            "random",
        ],
      },
      include_package_data=True)
