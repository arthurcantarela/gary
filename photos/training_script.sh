#/bin/bash

# Makes cascade directory if it doesn't exist already

mkdir -p cascade

#positives=$(ls -l positive_cropped/ | grep -E '.png|.jpg|.jpeg' | wc -l)
#negatives=$(ls -l negative/ | grep -E '.png|.jpg|.jpeg' | wc -l)

opencv_traincascade -data cascade/ -vec output.vec -bg negatives.txt -mem 1000 -h 30 -w 30 -numThreads 8

