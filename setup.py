from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'vk_162_gps'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*_launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ralph',
    maintainer_email='tom.j.watters@gmail.com',
    description='Simple Solution to plug and play with the VK 162 Gps unit',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gps = vk_162_gps.gps_pub:main'
        ],
    },
)
