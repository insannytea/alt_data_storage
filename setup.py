from setuptools import setup, find_packages

setup(
    name='alt_data_storage',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'Pillow',
        'imageio',
        'imageio[ffmpeg]',
    ],
)