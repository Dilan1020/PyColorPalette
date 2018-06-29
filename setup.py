import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name="PyColorPalette", version='1.2.2', author="Dilan Ozkaynak", author_email="DilanJames10@gmail.com", long_description=long_description, long_description_content_type="text/markdown", url="https://github.com/Dilan1020/PyColorPalette", packages=setuptools.find_packages())