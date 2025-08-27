from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).resolve().parent
readme_path = here / "README.md"
long_description = ""
if readme_path.exists():
    long_description = readme_path.read_text(encoding="utf-8")

setup(
    name="umjunsik",
    version="2.0.2",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "umjunsik = umjunsik_lang_python.__main__:main",
        ],
    },
    author="rycont",
    author_email="rycont@outlook.kr",
    description="어떻게 엄준식이 언어이름이냐🤣",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rycont/umjunsik-lang",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
