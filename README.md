# Images of Code: Lossy Compression of Native Instructions

This is the repository containing the source code for the code transformations and tools we used to perform the experiments described in our NIER@ICSE paper. 

We performed two experiments in the paper. The first one evaluated the size of the forgiving zones in the programs of our dataset. The secod experiment transformed a program so the compression ratio obtained with three different algorithms (Huffman, RLE and LZ77) would be improved and then, the transformed program was run to see if it actually produced a correct output.

The instructions to repeat these experiments are as folllows:



- [How to compile the C++ tools used to perform our experiments](https://github.com/lossycomp/imagesofcode/wiki/How-to-compile-the-programs-used-in-our-experiments).
- [How to compile the programs of our dataset](https://github.com/lossycomp/imagesofcode/wiki/How-to-compile-our-dataset's-programs).
- [How to set-up the Python scripts used in the experiments](https://github.com/lossycomp/imagesofcode/wiki/How-to-set-up-the-Python-Scripts-used-in-our-experiments)
- [How to repeat experiment 1: Size of Forgiving Zones](https://github.com/lossycomp/imagesofcode/wiki/How-to-repeat-experiment-1:-Size-of-Forgiving-Zones)
- [How to repeat experiment 2: Compression Ratio](https://github.com/lossycomp/imagesofcode/wiki/How-to-repeat-experiment-2:-Compression-Ratio)
- Description of our data

If you have any problem repeating the experiments, please open an issue. We will try to solve it as soon as possible.
