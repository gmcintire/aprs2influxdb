from distutils.core import setup

setup(
    name='APRS2InfluxDB',
    version='0.1.0',
    author='Bryce Salmi',
    author_email='Bryce@FaradayRF.com',
    packages=['aprs2influxdb'],
    url='https://github.com/FaradayRF/aprs2influxdb',
    license='GPLv3',
    description='Connects to APRS-IS and saves packets to InfluxDB',
    long_description=open('README.txt').read(),
    install_requires=[
        "aprslib>=0.6.46",
        "certifi>=2017.7.27.1",
        "chardet>=3.0.4",
        "configparser>=3.5.0",
        "idna>=2.6",
        "influxdb>=4.1.1",
        "pbr>=3.1.1",
        "python-dateutil>=2.6.1",
        "pytz>=2017.2",
        "requests>=2.18.4",
        "six>=1.11.0",
        "urllib3>=1.22",
    ],
)
