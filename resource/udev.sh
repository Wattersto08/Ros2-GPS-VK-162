echo 'Copying UDEV rules for VK-162 gps '
sudo cp udev.txt /etc/udev/rules.d/gps.rules

echo 'Rerunning Udev Rules'
sudo udevadm control --reload-rules 
echo 'Complete.' 