#/bin/bash

# Makes cascade directory if it doesn't exist already

mkdir -p cascade

positives=$(ls -l positive_cropped/ | grep -E '.png|.jpg|.jpeg' | wc -l)
negatives=$(ls -l negative/ | grep -E '.png|.jpg|.jpeg' | wc -l)

opencv_traincascade -data cascade/ -vec output.vec -bg negatives.txt -numNeg=$negatives -numPos=$positives -w 20 -h 20 -mem 2048

