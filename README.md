# TLS - Temporary Linux(Alpine) Shell/System

🚀 TLS provides a convenient way to start a temporary Alpine Linux shell/system using Python.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Alpine Linux](https://img.shields.io/badge/Alpine_Linux-%230D597F.svg?style=for-the-badge&logo=alpine-linux&logoColor=white)

[![PyPI download month](https://img.shields.io/pypi/dm/Temp-Linux-Shell.svg)](https://pypi.python.org/pypi/Temp-Linux-Shell/) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/Temp-Linux-Shell.svg)](https://pypi.python.org/pypi/Temp-Linux-Shell//)

![Screenshot of TLS](https://github.com/Noriskky/TLS/blob/main/pictures/screenshot.png?raw=true) 

## Installation

You can install TLS via pip:

```bash
pip install Temp-Linux-Shell
```

## Usage

Once installed, you can start a temporary Alpine Linux shell by running the `tls` command.

### Options

- `-h` or `--help`: Display the help message.
- `-d`: Specify a custom directory.
- `-hn` or `--hostname`: Specify a custom hostname.
- `-c` or `--command`: Specify a command to be executed at the start. After the completion of the command, the session closes.

## Support

There currently only Support for Linux because it is using ``Chroot`` it's planned to migrate to Docker or something else.
