#!/bin/sh
#
# Export a variable that modifies the path where it installs to, making it more flexible
UCPINSTALL=/usr/local
cp ucp.py ${UCPINSTALL}/bin/ucp
chmod +x ${UCPINSTALL}/bin/ucp
# Unset the variable
unset UCPINSTALL
