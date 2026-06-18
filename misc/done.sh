#!/bin/bash
set -e


git status

git add main.py
git add main.cpp

# value of first command line arg
NAME="$1"

git commit -m "done problem - ${NAME}"
git push
