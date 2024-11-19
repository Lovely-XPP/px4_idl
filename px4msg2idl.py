from rosidl_adapter.msg import convert_msg_to_idl
from rosidl_adapter.srv import convert_srv_to_idl
from pathlib import Path
import os


if __name__ == "__main__":
    # initialize path
    root_dir = os.path.dirname(__file__)
    px4_msg_folder = os.path.join(root_dir, "px4_msg/msg")
    px4_srv_folder = os.path.join(root_dir, "px4_msg/srv")
    process_msg_folder = os.path.join(root_dir, "px4_msg_modified/msg")
    process_srv_folder = os.path.join(root_dir, "px4_msg_modified/srv")
    output_folder = os.path.join(root_dir, "px4_idl")

    # preprocess msg, fastdds gen not support .idl files with .msg if first line is comment
    # create folders
    if not os.path.exists(process_msg_folder):
        os.makedirs(process_msg_folder)
    if not os.path.exists(process_srv_folder):
        os.makedirs(process_srv_folder)

    # convert .msg files
    for dirpath, _, filenames in os.walk(px4_msg_folder):
        for filename in filenames:
            msg_filename = os.path.join(dirpath, filename)
            msg_modified_filename = os.path.join(process_msg_folder, filename)
            with open(msg_filename, 'r', encoding='utf-8') as infile, open(msg_modified_filename, 'w', encoding='utf-8') as outfile:
                lines = infile.readlines()
                if lines:  # 确保文件不为空
                    # 确保文件开头不为注释
                    while "#" in lines[0][0:3]:
                        lines.pop(0)
                    outfile.writelines(lines)
            convert_msg_to_idl("px4_msg", Path(msg_modified_filename), Path(output_folder))

    # convert .srv files
    for dirpath, _, filenames in os.walk(px4_srv_folder):
        for filename in filenames:
            srv_filename = os.path.join(dirpath, filename)
            srv_modified_filename = os.path.join(process_srv_folder, filename)
            with open(srv_filename, 'r', encoding='utf-8') as infile, open(srv_modified_filename, 'w', encoding='utf-8') as outfile:
                lines = infile.readlines()
                if lines:  # 确保文件不为空
                    # 确保文件开头不为注释
                    while "#" in lines[0][0:3]:
                        lines.pop(0)
                    outfile.writelines(lines)
            convert_srv_to_idl("px4_msg", Path(srv_modified_filename), Path(output_folder))
    
    # handle strange error
    for dirpath, _, filenames in os.walk(output_folder):
        for filename in filenames:
            idl_filename = os.path.join(dirpath, filename)
            with open(idl_filename, 'r', encoding='utf-8') as f:
                content = f.read()
                # handle with relative path
                content = content.replace("px4_msg/msg/", "")
                # avoid interface reserver word
                content = content.replace("interface", "_interface")
                # avoid map reserver word
                content = content.replace("map", "_map")
            with open(idl_filename, 'w', encoding='utf-8') as f:
                f.write(content)
