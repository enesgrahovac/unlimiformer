from setuptools import setup, find_packages

setup(
    name='unlimiformer',
    version='0.1.0',
    package_dir={'': 'src'},  # This line tells setuptools to look for packages in the 'src' folder
    packages=find_packages(where='src'),
    install_requires=[
        "faiss-cpu",
        "faiss-gpu",
        "transformers"
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
