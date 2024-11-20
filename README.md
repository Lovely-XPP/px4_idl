# px4_idl
PX4 Interface Definition Language (IDL) message file for Fast-DDS application (ROS 2 independent).

## Introduction

This Repo is for whom want to use Fast-DDS application (ROS 2 independent) with px4 offboard control with latest PX4 Firmware (above 1.14). 

This repo provide idl files of all px4 messages in [px4_msg repo](https://github.com/PX4/px4_msgs).

## Requirements
```bash
Python >= 3.8
pathlib
```

## Implement

As we known, the latest ROS2 distribution support Fast-DDS middle-ware, so it must transform the .msg files (ROS message) to .idl files to use Fast-DDS.

Therefore, I searched the core module of ROS2 and found [rosidl](https://github.com/ros2/rosidl). Rosidl are the official ROS Packages which provide the ROS IDL (.msg) definition and code generation.

By rosidl, we can transform .msg files to .idl files.

## C++Messages

If you want to generate C++ Message files further, just run `GenerateCppMessages.bat`. Then, It will generate all C++ Message files from the .idl files.

**Tips: I have renamed the ".cxx" files to ".cpp" files.**

## Credits

- [px4_msg](https://github.com/PX4/px4_msgs)

- [rosidl](https://github.com/ros2/rosidl)