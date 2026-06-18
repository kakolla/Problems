#!/bin/bash
set -e


# value of first command line arg
NAME="$1"

if [[ -z "$NAME" ]]; then
	echo "first arg should be <name>"
	exit 1
fi


if [[ -f main.py && $(wc -l < main.py) -gt 1 ]]; then
	cat main.py >> misc/${NAME}.py
elif [[ -f main.cpp && $(wc -l < main.cpp) -gt 1 ]]; then
	cat main.cpp >> misc/${NAME}.cpp
fi

git status
read -p "continue? (y/n)" confirm 
if [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]]; then
	git commit -m "done problem - ${NAME}"
	git push
else
	exit 1
fi


