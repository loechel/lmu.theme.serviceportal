from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='lmu.theme.serviceportal',
      version=version,
      description="LMU Theme for ZUV-Serviceportal",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='Plone Theme LMU ZUV Serviceprotal Diazo',
      author='Alexander Loechel',
      author_email='Alexander.Loechel@lmu.de',
      url='https://github.com/loechel/lmu.theme.serviceportal',
      license='GPLv2',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['lmu', 'lmu.theme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'z3c.jbot',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
