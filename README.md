## VK-162 GPS Ros Node

Currently supports ROS2 Humble

This Package is to run and support the DIYmalls VK-162 usb GPS module. this is a low cost way in for ROS users to access GPS functionality. 

Lots of scope for optimisation.

If no signal is found the module will default to posting:

- Lat:  0.0 
- Long: 0.0 
- Alt:  0.0

For reference the module used can be found [here](https://www.amazon.co.uk/gp/product/B07FKRXXSM/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

### initial setup

1. Clone this repo into the src directory of your workspace via:

```
cd <your workspace>/src

git clone 
```

2. connect the gps module to the host. 

3. configure UDEV rules. 

```
cd <your workspace>/src/vk_162_gps/resource/

sudo source udev.sh 
```
*this will copy the udev.txt to the udev rules file and rerun the rules*

4. The package can be run or launched via the following: 

```
ros2 run vk_162_gps gps

    - - - OR - - - 

ros2 launch vk_162_gps vk_162.launch.py
```

If successful the following message will be visiable: 

```
[INFO] [1736712132.123092412] [gps_publisher]: GPS initialised
```

5. Enjoy!