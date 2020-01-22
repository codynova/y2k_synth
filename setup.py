import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="y2k_synth",
    version="0.0.1",
    author="Cody Nova",
    author_email="codyrnova@gmail.com",
    description="Simple synthesizer for the new millenium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codynova/y2k_synth",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pyaudio",
        "numpy",
        "scipy"
    ]
)