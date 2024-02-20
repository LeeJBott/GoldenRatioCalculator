#!/bin/bash
echo -e "Setup Starting\n"
sleep 1
echo "Writing Alias file"
sleep 2
echo -e "\nalias golden='python3 /home/$USER/GoldenRatioCalculator/GoldenRatio.py'" >> ~/.bashrc
source ~/.bashrc
echo "File Updated, use the 'golden' command to run the calculator!"
echo "Thanks"
