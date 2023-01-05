## Setup rshell in WSL2

1. Install rshell with pip
```shell
pip install rshell
```

2. Setup serial port permission
```shell
sudo usermod -a -G dialout $USER
```

3. Setup udev rules
```shell
sudo vi /etc/udev/rules.d/49-stmdiscovery.rules
```
Save the following to the file:
```shell
# f055:9800 - STM32F4 Discovery running MicroPython in USB Serial Mode (CN5)
ATTRS{idVendor}=="f055", ENV{ID_MM_DEVICE_IGNORE}="1"
ATTRS{idVendor}=="f055", ENV{ID_MM_PORT_IGNORE}="1"
ATTRS{idVendor}=="f055", ENV{MTP_NO_PROBE}="1"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="f055", MODE:="0666"
KERNEL=="ttyACM*", ATTRS{idVendor}=="f055", MODE:="0666"
# 0483:df11 - STM32F4 Discovery in DFU mode (CN5)
SUBSYSTEMS=="usb", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="df11", MODE:="0666"
```

Apply the rules:
```shell
sudo service udev restart
sudo udevadm control --reload-rules
```

reference:
https://github.com/dhylands/rshell


## Connecting mindstorm 51515 to WSL2 via USB

1. Connect robot to PC via USB and power it on

2. Make sure WSL is already running

3. On Windows PowerShell, attach USB device to WSL2 with
```shell
$ usbipd wsl list
BUSID  VID:PID    DEVICE                                                        STATE
2-2    1462:7d09  USB Input Device                                              Not attached
2-5    046d:0891  罗技高清网络摄像机 C930c                                      Not attached
2-12   046d:c338  USB Input Device                                              Not attached
3-1    0a12:0001  Generic Bluetooth Radio                                       Not attached
3-3    413c:301d  USB Input Device                                              Not attached
3-4    0694:0010  USB Serial Device (COM4)                                      Not attached

$ usbipd wsl attach --busid 3-4
```

4. On WSL terminal
```shell
$ lsusb
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 005: ID 0694:0010 Lego Group LEGO Technic Large Hub in FS Mode
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

$ rshell -p /dev/ttyACM0
$ rshell repl
```

Troubleshoot:
- If rshell repl failed, try on detach and attach again on Host:
```shell
usbipd wsl detach --busid 3-4
usbipd wsl attach --busid 3-4
```
- If problem persists, restart the service
```shell
sudo service udev restart
sudo udevadm control --reload-rules
```

## Frequently used commands

### list modules
help('modules')

### run file
repl ~ execfile('/projects/test/main.py')

