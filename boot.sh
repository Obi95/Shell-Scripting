#!/bin/bash

read -p "Do you want to play Rock, Paper, Scissors? (yes/no):" choice

if [[ $choice == "yes" ]]; then
	python3 rockpaperscisorsgame.py
elif [[ $choice == "no" ]]; then
	echo "Maybe next time!"
else
	echo "Invalid choice. Please enter 'yes' or 'no'."
fi

