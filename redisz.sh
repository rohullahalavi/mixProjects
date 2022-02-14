
#store only files not folders in Desktop inside variable and echo it to the screen
files=($(ls -A $HOME/Desktop))
echo ${files[@]}



