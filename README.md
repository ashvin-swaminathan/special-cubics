# special-cubics

This is a Magma code supplement for our paper entitled "Counting integral points on symmetric varieties with applications to arithmetic statistics." Our paper may be found on the arXiv at https://arxiv.org/pdf/2304.01050.

Copy the file file avg.txt into your directory. Then it can be loaded into magma using the command 

load "avg.txt"; 

This defines a function avg(signature,a,d,bmin,bmax,cmin,cmax) which takes the following as input:
-- a real signature with value 1 or -1 (corresponding to totally real or complex cubic fields),
-- x^3 and y^3 coefficients a and d for the defining binary cubic forms,
-- bounds bmin, bmax and cmin, cmax for the values of b and c.
The function prints the average 2-torsion in the class groups of the cubic number fields with the specified real 
signature defined by maximal binary cubic forms of the shape ax^3 + bx^2y + cxy^2 + dy^3 with b lying in [bmin,bmax] 
and c lying in [cmin,cmax]. For comparison, it also prints the average predicted by our results.


The code is adapted from a program originally written by Manjul Bhargava.
