#/bin/sh

# Author : 
# Description :

echo ""
echo ""
echo "Running hobby-hub setup script."
echo "This may take a few moments..."

mkdir -p /etc/hobby-hub/

echo "Processing sub-scripts:"
for f in scripts/*.sh
do
  echo "$f"
  sh $f
done

echo "Setup Complete! The device will now restart..."
echo ""
sleep 3
#reboot
