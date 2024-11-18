from rosidl_adapter.msg import convert_msg_to_idl
from rosidl_adapter.srv import convert_srv_to_idl
from pathlib import Path
import os


if __name__ == "__main__":
    # initialize path
    root_dir = os.path.dirname(__file__)
    px4_msg_folder = os.path.join(root_dir, "px4_msg/msg")
    px4_srv_folder = os.path.join(root_dir, "px4_msg/srv")
    output_folder = os.path.join(root_dir, "px4_idl")

    # convert .msg files
    for dirpath, _, filenames in os.walk(px4_msg_folder):
        for filename in filenames:
            msg_filename = os.path.join(dirpath, filename)
            convert_msg_to_idl("px4_msg", Path(msg_filename), Path(output_folder))

    # convert .srv files
    for dirpath, _, filenames in os.walk(px4_srv_folder):
        for filename in filenames:
            srv_filename = os.path.join(dirpath, filename)
            convert_srv_to_idl("px4_msg", Path(srv_filename), Path(output_folder))
            
