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

# Check if being piped through another process
if [ -t 0 ]; then
    # Not being piped, execute directly
    install_tls_and_execute
else
    # Being piped, don't execute interactively
    install_tls_and_execute < /dev/tty
fi
