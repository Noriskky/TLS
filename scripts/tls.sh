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

# Check if stdin is not a terminal
if [ ! -t 0 ]; then
    # Being piped, execute without waiting for user input
    install_tls_and_execute < /dev/null
else
    # Not being piped, execute normally
    install_tls_and_execute
fi
