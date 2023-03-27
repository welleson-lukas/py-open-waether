import os
from setuptools import setup, find_packages

requirements = []

requirements_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'src/dependencies/requirements.txt')

with open(requirements_path) as req_file:
    for req_line in req_file:
        req_line = req_line.strip()
        if req_line.count('==') == 1:
            requirements.append(req_line)

setup(
    name='py-open-weather',
    version='1.0.0',
    description='SDK description',
    classifiers=[
      'Programming Language :: Python'
    ],
    author='Welleson Colares',
    author_email='<contato@provu.com.br>',
    url='https://github.com/welleson-lukas/sdk-open-weather.git',
    keywords=['python', 'open', 'weather', 'lib'],
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    setup_requires=['wheel'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    extras_require={},
    dependency_links=[]
)