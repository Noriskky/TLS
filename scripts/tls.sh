#!/bin/sh
min=10
max=100
random=$((RANDOM % (max - min + 1) + min))
CWD="/var/tmp/tls-sh-$random"

PYTHON="$CWD/bin/python"
PIP="$CWD/bin/pip"
TLS="$CWD/bin/tls"

python -m venv "$CWD"
$PIP install Temp-Linux-Shell
$TLS
