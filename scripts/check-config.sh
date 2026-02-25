#!/usr/bin/env bash
# simple config check demo
if [ ! -f /etc/passwd ]; then
  echo "Missing /etc/passwd - unexpected!" >&2
  exit 1
fi
echo "Basic system file present - ok"
