import os
from setuptools import setup, find_packages

media_files = []

for dirpath, dirnames, filenames in os.walk('src/django_yaba/media'):
        media_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

setup(
    name = "django-yaba",
    version = "0.2.7",
    author = "Mark Rogers",
    author_email = "f4nt@f4ntasmic.com",
    url = "http://www.f4ntasmic.com",
    
    packages = find_packages('.'),
    package_dir = {'':'.'},
    data_files = media_files,
    package_data = {
        'django_yaba':
        ['templates/admin/*.html',
        'templates/blog/*.html',
        'templates/comments/*.html',
        'templates/feeds/*.html']
    },
    include_package_data=True,
    license = "BSD License",
    keywords = "django yaba blog",
    description = "Yet Another Blog Application",
    install_requires=[
        'django>=1.4',
        'setuptools',
        'python-twitter',
        'twitter',
        'simplejson',
        'feedparser',
        'django-tagging',
        'six', 
        'pytz', 
        'pillow',
    ],
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        'Programming Language :: Python',
    ]
)
