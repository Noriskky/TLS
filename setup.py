import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tls",
    version="0.1.0",
    author="Noriskky",
    author_email="Noriskky44@proton.me",
    description="Wrapper around Chroot to make it easy to use temporary Linux Shells.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Noriskky/tls",
    keywords="cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires=[
        "requests",
        "tqdm"
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "tls=tls.main:main",
        ],
    },
)
