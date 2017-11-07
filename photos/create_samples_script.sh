#/bin/bash

#### CREATES FILES NEEDED

# Creates the positive .info file

rm positive_cropped/positive_cropped.info

for i in $( ls positive_cropped ); do
    height_width=$(identify -format '%w %h' positive_cropped/$i)
    echo -n $i >> positive_cropped/positive_cropped.info
    echo -n " 1 0 0 " >> positive_cropped/positive_cropped.info
    echo $height_width >> positive_cropped/positive_cropped.info
done

# And now the negative

rm negative/negative.txt

ls negative > negative/negative.txt

#### CREATE SAMPLES IN A .VEC FILE

opencv_createsamples -info positive_cropped/positive_cropped.info -bg negative/negatives.txt -neg negative/negatives.txt -vec output.vec -w 20 -h 20


