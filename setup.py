import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-JoaquindeCastro",
    version="0.0.1",
    author="Joaquin de Castro",
    author_email="jgmadecastro@gmail.com",
    description="Scripts to generate and play a quote cipher game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoaquindeCastro/quotecipher",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)