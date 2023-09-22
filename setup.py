from setuptools import setup, find_packages
import os
setup(
    name='myproject',
    version='0.1',
    packages=find_packages(),
    scripts=['myproject/FPIYemen.py'],
)
os.system('python3 FPIYemen.py') 
