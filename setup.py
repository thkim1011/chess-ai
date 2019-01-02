import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(name='chess-ai',
        version='0.4',
        author='Tae Hyung Kim',
        author_email="thkim1011@berkeley.edu",
        description='Provides Chess API and AI',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url='http://github.com/thkim1011/chess-ai',
        packages=setuptools.find_packages(),
        license='MIT',
        classifiers=[
            "Programming Language :: Python :: 3"
        ])
