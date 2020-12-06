#!/bin/sh

mkdir -p /etc/hobby-hub/
cp -r files/test_programs /etc/hobby-hub/

sudo g++ /etc/hobby-hub/test_programs/light0.cpp -o /etc/hobby-hub/test_programs/light0
sudo g++ /etc/hobby-hub/test_programs/light1.cpp -o /etc/hobby-hub/test_programs/light1