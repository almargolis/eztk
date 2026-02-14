from setuptools import setup
import os

readme_path = os.path.join(os.path.dirname(__file__), "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    long_description = "eztk - A simplified Tkinter widget framework"

setup(
    name="eztk",
    version="0.1.0",
    author="Albert Margolis",
    author_email="almargolis@gmail.com",
    description="A simplified Tkinter widget framework with grid layout engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/almargolis/eztk",
    project_urls={
        "Bug Tracker": "https://github.com/almargolis/eztk/issues",
        "Source Code": "https://github.com/almargolis/eztk",
    },
    package_dir={"": "src"},
    packages=["eztk"],
    install_requires=[],
    extras_require={
        "images": [
            "opencv-python>=4.5.0",
            "numpy>=1.19.0",
            "Pillow>=8.0.0",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="tkinter gui widgets layout",
)
