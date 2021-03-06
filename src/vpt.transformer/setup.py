import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'celery==3.0.19',
    'pyramid_celery',
    'cornice',
    'Pillow',
    'lxml',
    'libxml2-python',
    'waitress',
    'Babel',
    'lingua',
    'requests',
    'rhaptos.cnxmlutils',
    'pytidylib', # required by rhaptos.cnxmlutils
    'oerpub.rhaptoslabs.cnxml2htmlpreview',
    ]

setup(name='vpt.transformer',
      version='0.0',
      description='VOER Platform - Transformer',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="vpt.transformer",
      entry_points="""\
      [paste.app_factory]
      main = vpt.transformer:main
      """,
      message_extractors = { '.': [
        ('**.py',   'lingua_python', None ),
        ('**.pt',   'lingua_xml', None ),
      ]},
      )
