import os

if __name__ == "__main__":
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    cpp_messages_dir = os.path.join(root_dir, "CppMessages")

    # handle with cxx files
    for dirpath, _, filenames in os.walk(cpp_messages_dir):
        for filename in filenames:
            # get basename and extension
            basename, extension = os.path.splitext(filename)

            # exclude not cxx files
            if extension != ".cxx":
                continue

            # read cxx file
            cxx_filename = os.path.join(dirpath, filename)
            with open(cxx_filename, 'r') as f:
                cxx_content = f.read()

            # generate cpp file
            cpp_filename = os.path.join(dirpath, basename + ".cpp")
            cpp_content = "#pragma warning(disable : 4583)\n#pragma warning(disable : 4583)\n" + cxx_content
            with open(cpp_filename, 'w') as f:
                f.write(cpp_content)
            
            # remove cxx file
            os.remove(cxx_filename)
            print(f"已导出消息文件 {basename + ".cpp"}.")
            