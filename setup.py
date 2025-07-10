from setuptools import setup, find_packages

setup(
    name="password_manager",
    version="0.1.0",
    description="A simple password manager CLI tool.",
    author="Flaxa",
    packages=find_packages(),
    install_requires=[
        "argon2-cffi",
        "bullet",
        "cryptography",
    ],
    entry_points={
        "console_scripts": [
            "password-manager=password_manager.main:main",
        ],
    },
    python_requires=">=3.7",
)