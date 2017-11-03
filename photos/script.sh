#!/bin/bash

COUNTER=0

for i in $( ls positive_cropped ); do
	opencv_createsamples -img positive_cropped/$i -bg negative/negatives.txt -vec samples/sample_$COUNTER.vec -maxxangle 0.6 -maxyangle 0.1 -maxzangle 0.3 -maxxidev 100 -bgcolor 0 -bgthresh 0 -w 80 -h 40
	let COUNTER+=1
done


