from setuptools import setup, find_packages

setup(
    name='file_uploader',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'google-cloud-storage'
    ],
    entry_points={
        'console_scripts': [
            'file_uploader=file_uploader.main:main'
        ]
    },
    description='A module to upload files to AWS S3 and Google Cloud Storage.',
    author='Your Name',
    author_email='your-email@example.com',
    url='https://github.com/your-repository/file_uploader'
)