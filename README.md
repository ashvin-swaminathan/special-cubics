# special-cubics

This is a code supplement for our paper entitled "Counting integral points on symmetric varieties with applications to arithmetic statistics." Our paper may be found on the arXiv at https://arxiv.org/pdf/2304.01050.

The code supplement can be used according to the following steps:

(1) Use the python script generate_fields.py to generate a list of pairs of values (b,c). In terminal, this can be done using the command

python3 generate_fields.py

(2) Use the magma script avg.txt to compute the average 2-torsion in the class groups of the cubic fields corresponding to the output of step (1). In magma, this can be done using the command

load "NEW avg.txt"; 

The code is adapted from a program originally written by Manjul Bhargava.

The data included in the tables in our paper can be found in the directory "new-special-cubics".
