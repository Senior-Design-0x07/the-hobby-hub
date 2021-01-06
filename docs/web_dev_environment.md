<!-- This document tells users how to setup our Flutter Frontend Dev. Environment -->
<!-- Author: Anthony Bartman -->
<!-- Date: 12/20/20 -->

# Overview
* We will be developing our **Flutter Frontend** on our normal PC,
and our **Flask Backend** on our Beaglebone.
* Our Flutter Frontend will have it's own separate repo from the main ```the-hobby-hub``` repo 
because Flutter projects are massive
* The ```flutter-frontend``` repo will be used to store our main project, as well as hold the
build files for Android, IOS, and the Website. (I'll write a script to c/p them to our board and other repo)
* Our default IDE I'll be showing you guys how to setup is VS Code with Flutter. Android Studio
is a viable option as well, but I want everything in one IDE. Your choice though :).

# Basic Setup:
1. Follow this tutorial from 41:32 to 1:04:34.
   [LINK](https://www.youtube.com/watch?v=x0uinJvhNxI&t=2492s)

# Setting Up OUR Development Environment:
## Flutter Base Setup 
1. Visit [HERE](https://flutter.dev/docs/get-started/install/windows) to install Flutter
2. Install Git for Windows and the Flutter SDK on local machine
3. Wherever you saved Flutter SDK on your machine (mine is in C: drive), open ```flutter_console.bat```
4. In order to use flutter commands from Windows CMD, update environment variable PATH with location of
flutter bin file(mine is ```C:\flutter\bin```)
5. Open CMD, type in 'flutter' to verify if it is in the PATH correctly
**Flutter Web Config**(ref: [Link](https://flutter.dev/docs/get-started/web) )
6. Run: 'flutter channel beta', then 'flutter upgrade', and 'flutter config --enable-web'
(Let me know if this works for you guys)

## Setup Android Studio
1. Install Android Studio: [HERE](https://developer.android.com/studio)
  * Make sure you check ```Android Virtual Device``` when installing
2. Watch video to help with this install
## ** Load up our starter project**
1. Put project somewhere on local PC: ```git clone https://github.com/Senior-Design-0x07/flutter-frontend.git```
and open with android studio to setup virtual devices.
(Watch Video for the parts below if stuck)
2. Click ```Tools -> AVD Manager``` and create a new virtual device
3. We will use the ```Pixel 3a XL``` to test code for Android Devices, ```Release Q```, and ```Hardware Graphics - GLES 2.0```
4. Click the play button from the AVD manager to verify it works
5. On main Android Studio screen, a yellow header is there with the words: 'install dependencies' Click it.
6. After that click and Android Studio reboots, in bottom left click 'configure plugins' and install it.
7. On main Android Studio screen, Click ```Tools -> SDK Manager```, click tab SDK tools towards top of dialog box and install
the ```Google USB Driver```
8. Run cmd: ```flutter doctor``` to verify everything is working

## Run Project on Emulator(Mobile)
1. Click Green Play button on Android Studio while phone emulator is open to run our project on the emulator. It will take some
time the first time project is building. 
*All this is doing is running the command ```flutter run``` in the top-directory of project. Will use this if using VS Code
## Run Project on Website
1. **ONLY WORKS** by this...cd to project directory and run: ```flutter run -d chrome --release```

## Using VS Code as IDE
1. Open Repo in VS Code and go to extensions by CTRL+SHIFT+X
2. Search for 'flutter' and install that extension
3. Open cmd prompt by pressing ```CTRL + ` ```
4. Run command: ```flutter devices``` to see the hiearchy.
4a. To develop with mobile app, open Android Studio AVD Manager and open the phone emulator before performing
the ```flutter run``` command so that it will delegate to the phone emulator rather than chrome.
4b. Run command :```flutter run -d chrome --version``` to develop for website.

#Tips when developing with Flutter
1. Always have flutter 'running' when developing our UI because the full build/rebuilding process takes a long time.
 - > To view code changes, from cmd line type in ```r``` to hot reload app/website.
 - > To full reload app/website, from cmd line type in ```SHIFT+r```
 - > ```Ctrl + C``` to stop 'flutter run'
