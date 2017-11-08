# Please read this before using

To train your haar cascade algorithm, place negative photos (in which the objects you want to detect are NOT in) in negative/

After that, crop all your positive pictures so that only the desired object is displayed and place the cropped version in positive_cropped/

After that just run create_samples_script.sh and it's going to do all the work (just remember to chmod 755 it before running).

Run then the training_script.sh, which will generate the .xml files to detect the object using opencv.

Keep in mind that you can change the parameters inside these scripts, like height, width, etc.

Obs: Be sure to have imagemagick installed. On Ubuntu you can install it by typing:

```$ sudo apt-get install imagemagick```
