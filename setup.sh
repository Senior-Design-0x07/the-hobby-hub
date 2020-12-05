#/bin/sh

# Author : 
# Description :

echo ""
echo ""
echo "Running hobby-hub setup script."
echo "This may take a few moments..."
echo""

echo "||||||||||||||||||||||||||||||||"
echo "||| updating device packages |||"
echo "||||||||||||||||||||||||||||||||"
echo ""
sudo apt-get update
sudo apt-get upgrade

mkdir -p /etc/hobby-hub/


echo "||||||||||||||||||||||||||||||||"
echo "||| processing sub-scripts  ||||"
echo "||||||||||||||||||||||||||||||||"
echo""
for f in scripts/*.sh
do
  echo "$f"
  sh $f
done
echo"" 

echo "||||||||||||||||||||||||||||||||"
echo "||||||| setup complete! ||||||||"
echo "||||||| restarting...   ||||||||"
echo "||||||||||||||||||||||||||||||||"
echo ""
sleep 3

#sudo reboot
