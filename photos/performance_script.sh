#/bin/bash

# Makes cascade directory if it doesn't exist already

mkdir -p cascade_performance_test

positives=$(ls -l positive_cropped/ | grep -E '.png|.jpg|.jpeg' | wc -l)
negatives=$(ls -l negative/ | grep -E '.png|.jpg|.jpeg' | wc -l)

opencv_haartraining -data cascade_performance_test/ -vec output.vec -bg negative/negatives.txt -npos $positives -nneg $negatives -w 20 -h 20 -mem 1024

opencv_performance -data cascade_performance_test -info positive/positive_cropped.info
