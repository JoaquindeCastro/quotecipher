from setuptools import setup

APP=['app.py']

OPTIONS = {
	'argv_emulation':True,
}

setup(
	APP=APP,
	OPTIONS={'py2app':OPTIONS},
	setup_requires=['py2app']
)