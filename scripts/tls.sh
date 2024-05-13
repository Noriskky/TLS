#!/bin/sh
set -e

min=10
max=100
random=$((RANDOM % (max - min + 1) + min))
CWD="/var/tmp/tls-sh-$random"

PYTHON="$CWD/bin/python"
PIP="$CWD/bin/pip"
TLS="$CWD/bin/tls"

# Function to install Temp-Linux-Shell and execute tls
install_tls_and_execute() {
    python -m venv "$CWD"
    "$PIP" install Temp-Linux-Shell
    "$TLS"
}

# Check if being run interactively
if [ -t 0 ] && [ -t 1 ]; then
    # Being run interactively, execute directly
    install_tls_and_execute
else
    # Not being run interactively, execute without controlling terminal
    install_tls_and_execute < /dev/null
fi
