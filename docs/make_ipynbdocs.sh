#jupyter nbconvert --to python ../tutorials/*ipynb --output-dir=./tutorials/
jupyter nbconvert --to markdown ./tutorials/*ipynb --output-dir=./tutorials/
jupyter nbconvert --to markdown ./gallery/*ipynb --output-dir=./gallery/
sed -i 's/\.ipynb/\.md/g' tutorials/*md
sed -i 's/\.ipynb/\.md/g' gallery/*md
