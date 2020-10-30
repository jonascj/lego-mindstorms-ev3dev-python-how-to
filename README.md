# Getting started with ev3dev and Python for LEGO Mindstorms EV3 (from the command line)
A short guide on how to run the [ev3dev](https://www.ev3dev.org) 
Linux-based operating system on your LEGO Mindstorms EV3 brick,
interact with it using the command line and program it using Python.



# Setup

## Prepare microSD-card 

Download the latest ev3dev image from https://www.ev3dev.org/downloads/ 
(e.g. [ev3dev-stretch-ev3-generic-2020-04-10.zip](https://github.com/ev3dev/ev3dev/releases/download/ev3dev-stretch-2020-04-10/ev3dev-stretch-ev3-generic-2020-04-10.zip))
unpack/unzip it and flash the img-file to a microSD-card:

```
unzip ev3dev-stretch-ev3-generic-2020-04-10.zip

cd ev3dev-stretch-ev3-generic-2020-04-10

sudo dd bs=4M if=ev3dev-stretch-ev3-generic-2020-04-10.img of=/dev/mmcblk0 conv=fdatasync status=progress
```

## Wireless network adapter
Obtain a nano-style usb wireless network adapter like the 
[tp-link TL-WN725N](https://www.tp-link.com/dk/home-networking/adapter/tl-wn725n/)
or one of the adapters listed (and tested) here https://www.ev3dev.org/docs/networking/.

## Plug in
Insert the microSD-card in the microSD card slot 
and your wireless network adapter into the USB-A port.

<img alt="Photograph of sd-card slot and USB-A port" src="docs/sd-slot-usb-port.jpg" height="200">

## Power on / boot
Power on the EV3 brick by pressing button ``[1]``.

It will take 100-140 seconds to boot, 
during this time you'll the LEDs will flash yellow/orange
and a boot screen with an EV3DEV logo.

<img alt="Photograph of the EV3 brick" src="docs/ev3-brick-labeled.jpg" height="400">

Once the boot process is complete the display will look like this
and the LEDs will be green.

<img src="docs/brickman-boot-complete.jpg" height="200">

# Connect to a wireless network
Using the menus and buttons to connect to a wireless network.

Buttons `[3]`, `[4]`, `[5]`, `[6]` change selection 

Botton `[1]` selects

Button `[2]` goes back

1. Navigate to `Wireless and Networks` >> `Wi-Fi`

2. Select `Start Scan` to scan for available networks

3. Select your desired wireless network from the list.

   <img src="docs/brickman-wifi-list.jpg" height="200">

4. Select `Connect` 

5. If your network protected by a passphrase you'll see
   a dialog `Please enter passphrase for <network name>`.

   Press button `[1]` once to access an on-screen keyboard.

   <img src="docs/brickman-passphrase-keyboard.jpg" height="200">

   Use the buttons to type in your passphrase.

   Use the tabs `[ABC]` and `[abc]` to get lower and upper case letters,
   `[123]` to get numbers and `[!@#]` to get special characters.

   Finish by selectin `[OK]` and `[Accept]`.

6. The IP address assigned to your EV3 (by the DHCP server of the network)
   can now be seen in the top of the display, e.g. 192.168.1.202.

   <img src="docs/brickman-ip-address.jpg" height="200">

   
# Connect to your robot using SSH
From the command line (Windows Powershell, macOS Terminal, Linux shell/terminal)
issue the following command

```
ssh robot@<ev3 ip address>
```

The first time you connect you will likely see a prompt like

```
The authenticity of host '10.13.37.101 (10.13.37.101)' can't be established.
ECDSA key fingerprint is SHA256:sNNNlUWTtDtWX0CbCLcC83h8Yohuql2x2f6elfXKf+c.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Type `yes` and press [Enter] 
(if you want to know more do an internet search for `ssh fingerprint`
it is an important concept).

Proceed to type in the default ev3dev password (for the user robot)
which is `maker` and press [Enter]. 
Note you will likely not see any characters as you type.

The process is complete once you see the following prompt in your terminal

```
Linux ev3dev 4.14.117-ev3dev-2.3.5-ev3 #1 PREEMPT Sat Mar 7 12:54:39 CST 2020 armv5tejl
             _____     _
   _____   _|___ /  __| | _____   __
  / _ \ \ / / |_ \ / _` |/ _ \ \ / /
 |  __/\ V / ___) | (_| |  __/\ V /
  \___| \_/ |____/ \__,_|\___| \_/

Debian stretch on LEGO MINDSTORMS EV3!
Last login: Thu Oct 29 17:45:03 2020 from 10.13.37.13
robot@ev3dev:~$
```

This (a terminal showing `robot@ev3dev:`) is I will call the **ev3dev shell**.

Here you can enter Linux commands and have them executed by ev3dev and the EV3.

Try a few:

* pwd
* ls -la
* ping 8.8.8.8
* touch newfile.txt
* wget https://www.random.org/integers/?num=10&min=1&max=6&col=1&base=10&format=plain&rnd=new

# Change password
Change the default password 
(as you should do with all new devices)
by issuing the command

```
passwd
```
It will aks you for you current password (`maker`) and a new password (twice).

After you see the message `passwd: password updated successfully`
close your terminal and connect again with ssh using your new password.

# Your first Python program for your EV3

In order for ev3dev and EV3 to run a Python program 
a Python file needs to be created on or transfered to the ev3dev filesystem. 
There are several ways to do this.

## TL;DR; Using the ev3dev shell and a command line editor
If you are **experienced** with **linux** or the **command line in general**
you can write and execute programs like this:

1. Create and edit a .py file with editors vim or nano
(or any other CLI way of writing files)

2. Execute the program as `micropython <file.py>` 

3. If you perform `chmod +x <file.py>` (and have the proper shebang in your file)
you can also execute the program from the menu `File Browser` on the EV3.

Try something like:

```
#!/usr/bin/env micropython
import time
for i in range(10):
    print("Hello")
time.sleep(2)
```

## Using your local text editor and scp
In this workflow you'll be creating Python proggrams
in your usual (maybe graphical) text editor / IDE 
and transfering them to the ev3dev using a command line utility called scp.

1. Create a Python file with the following content 
   somewhere meaningful in your local filesystem / on your local storage.

   ```
   #!/usr/bin/env micropython
   import time
   for i in range(10):
       print("Hello")
   time.sleep(2)
   ```

2. From the command line 
   (remember to change working directory to where you saved your .py-file)
   issue the following command which transfers the file to your EV3:

   ```
   scp <file.py> robot@<ev3 ip address>
   ```

   You'll be asked the password for the user robot 
   (hopefully it is not `maker` since you changed it, right?).

3. From an ev3dev shell verify the file is there by using `ls -l`


Now the program is ready to be executed by the ev3dev/EV3.
There are two ways of doing this:

### Run from command line
In some respects the easiest way of executing a program is
from the command line (the ev3dev shell).

1. Open an ev3dev shell

2. Run the program by issuing the command

   ```
   micropython <file.py>
   ```

Any output (from ``print()``) will be shown in the ev3dev shell
as will any errors.

### Run from the EV3 menus (brickman)
Another option is to run the program from the menus on the EV3 display
(called brickman, short for brick manager).

1. First the file needs to be made executable.
   From an ev3dev shell issue the command
   
   ```
   chmod +x <file.py>
   ```
2. Use the `File Browser` menu on the EV3 display 
   to select and thereby execute your file.

   Output from `print()` will be shown on the display.
   The output, however, disappears once the program terminates.
   Hence the output of a program consisting of a few `print()` statements
   will not be visible (it disappears to quickly).
   That is why the example program above has a ``time.sleep(2)`` statement
   at the end to keep the output visible for 2 seconds.


# Using Python to control motors and sensors
ev3dev comes with a Python module which allows easy control 
of the EV3 motors and sensors.

Connect two **large motors** to output A and B:

<img alt="Photograph of motor ports A, B, C, D" src="docs/motor-ports.jpg" height="200">

Connect a **color sensor** to any input port:

<img alt="Photograph of sensor ports 1, 2, 3, 4" src="docs/sensor-ports.jpg" height="200">

Try (and review) the program `examples/test-motor-colorsensor.py`.

It turns the two motors slowly and prints the color sensor value.
The program can be stopped by pressing any of the buttons on the EV3
or by pressing [ctrl]+[c] in the ev3dev shell
(if running the program from the command line).
