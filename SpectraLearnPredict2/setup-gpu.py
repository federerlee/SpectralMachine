from setuptools import setup, find_packages

setup(
    name='SpectraLearnPredict2',
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib', 'pandas', 'scikit-learn', 'keras',
                    'pydot', 'graphviz', 'h5py', 'tensorflow-gpu'],
    entry_points={'gui_scripts' : ['SpectraLearnPredict2=SpectraLearnPredict2.__main__:main']},
    version='20180623a',
    description='Machine learning for spectral data - GPU version',
    long_description= """ Machine learning for spectral data """,
    author='Nicola Ferralis',
    author_email='ferralis@mit.edu',
    url='https://github.com/feranick/SpectralMachine',
    download_url='https://github.com/feranick/SpectralMachine/releases',
    keywords=['Machine learning', 'physics', 'spectroscopy', 'diffraction'],
    license='GPLv2',
    platforms='any',
    classifiers=[
     'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
     'Development Status :: 5 - Production/Stable',
     'Programming Language :: Python',
     'Programming Language :: Python :: 3',
     'Programming Language :: Python :: 3.5',
     'Programming Language :: Python :: 3.6',
     'Intended Audience :: Science/Research',
     'Topic :: Scientific/Engineering :: Chemistry',
     'Topic :: Scientific/Engineering :: Physics',
     ],
)
