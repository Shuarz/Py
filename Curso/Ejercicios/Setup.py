from ensurepip import version
from importlib.resources import Package
from unicodedata import name
from setuptools import setup


setup(
        name="paqueteCalculos",
        version="1.0",
        description="paquete de redondeo y potencia",
        author="Shuarz",
        author_email="shuarz.wolfz@gmail.com",
        url="https://github.com/Shuarz",
        Packages=["Calculadora","CalculosGenerales"]
     )