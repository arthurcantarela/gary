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

rm -f output.vec # Just in case

number_pics=$(ls -l positive_cropped/ | grep -E '.png|.jpg|.jpeg' | wc -l)

echo There are $number_pics pictures in your positive_cropped directory.

echo Starting opencv_createsamples executable...

opencv_createsamples -info positive_cropped.info -bg negatives.txt -vec output.vec -w 20 -h 20

