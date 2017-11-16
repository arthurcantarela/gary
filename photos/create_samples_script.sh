#/bin/bash

#### CREATES FILES NEEDED

# Creates the positive .info file

echo Generating text files...

rm -f positive_cropped/positive_cropped.info
rm -f positive_cropped.info

touch positive_cropped.info

for i in $( ls positive_cropped ); do
    height_width=$(identify -format '%w %h' positive_cropped/$i)
    echo -n positive_cropped/ >> positive_cropped.info
    echo -n $i >> positive_cropped.info
    echo -n " 1 0 0 " >> positive_cropped.info
    echo $height_width >> positive_cropped.info
done

# And now the negative

rm -f negative/negatives.txt
rm -f negatives.txt

touch negatives.txt

for i in $( ls negative ); do
    echo -n negative/ >> negatives.txt
    echo $i >> negatives.txt
done


echo Done

#### CREATE SAMPLES IN A .VEC FILE

echo There are $number_pics pictures in your positive_cropped directory.

echo Starting opencv_createsamples executable...

COUNTER=0

rm -r -f vecs/
rm -f output.vec

number_negatives=$( ls -l negative/ | grep -E '.png|.jpg|.jpeg' | wc -l )

for i in $( ls positive_cropped ); do
    opencv_createsamples -img positive_cropped/$i -num $number_negatives -bg negatives.dat -info positive_cropped.info -vec vecs/output$COUNTER.vec -maxxangle 0.6 -maxyangle 0 -maxzangle 0.3 -maxidev 100 -bgcolor 0 -bgthresh 0 -w 30 -h 30
    let COUNTER=$COUNTER+1
done

### MERGING .VECs

python mergevec.py -v vecs/ -o output.vec
