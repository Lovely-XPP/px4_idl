# Copyright 2018 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pathlib import Path

from rosidl_adapter.parser import parse_service_string
from rosidl_adapter.resource import expand_template, SrvData


def convert_srv_to_idl(package_name: str, input_file: Path, output_dir: Path) -> Path:
    assert input_file.is_absolute()
    assert input_file.suffix == '.srv'

    print(f'Reading input file: {input_file}')
    content = input_file.read_text(encoding='utf-8')
    srv = parse_service_string(package_name, input_file.stem, content)
    
    output_file = output_dir / input_file.with_name(input_file.stem + "Service").with_suffix('.idl').name
    abs_output_file = output_file.absolute()
    print(f'Writing output file: {abs_output_file}')
    data: SrvData = {
        'pkg_name': package_name,
        'relative_input_file': input_file.as_posix(),
        'srv': srv,
    }

    expand_template('srv.idl.em', data, output_file, encoding='iso-8859-1')
    return output_file
