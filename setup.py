from setuptools import find_packages,setup
setup(
    name = 'MCDGenerator',
    version = '0.0.1',
    author = 'Omar AboElnaga',
    author_email='omaraboalnaga7@gmail.com',
    install_requires = ['openai','langchain','streamlit','python-dotenv','PyPDF2'],
    packages=find_packages()
)