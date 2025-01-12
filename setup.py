from setuptools import setup, find_namespace_packages

setup(
    name="macos-screenshot",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src", include=["*"]),
    package_data={
        "stubs": ["*.pyi", "py.typed"],
    },
    install_requires=[
        "pyobjc-core",
        "pyobjc-framework-Cocoa",
        "pyobjc-framework-Quartz",
        "Pillow",
        "numpy",
    ],
    python_requires=">=3.11",
)
