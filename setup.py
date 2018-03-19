import glartifacts.version
import setuptools

setuptools.setup(
    name='glartifacts',
    version=glartifacts.version.__version__,
    description='Tools for managing GitLab CI build artifacts',
    license='MIT',
    keywords='GitLab',
    author='Mike Haboustak',
    author_email='haboustak@gmail.com',
    url='https://gitlab.com/haboustak/gitlab-artifact-tools',
    packages=['glartifacts'],
    entry_points={
        'console_scripts': [
            'glartifacts = glartifacts.__main__:main',
        ]
    },
    install_requires=[
        'psycopg2==2.6',
    ],
)