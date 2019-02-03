# AI Algorithms
Hill Climbing and Local Beam Search applied 100 random generated points to find the max value in 2 functions

A. HILL CLIMBING RESULTS: 
f1 = sin(x/2) + cos(2y);				 f2 = -|x-2| - |0.5y +1| +3
DATA:

Step Size

0.01

f1

Max Vals Mean = 1.9999826678717116

Max Vals Std = 1.5000981845884203e-05

Num of Steps Mean = 258.75

Num of Steps Std = 166.9455824512886

f2

Max Vals Mean = 2.996196939694454

Max Vals Std = 0.001608590085086108

Num of Steps Mean = 765.72

Num of Steps Std = 256.75058247256226

0.05

f1

Max Vals Mean = 1.9995613270879218

Max Vals Std = 0.0003294947319420252

Num of Steps Mean = 57.95

Num of Steps Std = 34.906553825893496

f2

Max Vals Mean = 2.9822831575303734

Max Vals Std = 0.00828210341167628

Num of Steps Mean = 147.9

Num of Steps Std = 51.59215056575952

0.1

f1

Max Vals Mean = 1.9981502082615163

Max Vals Std = 0.00153905766515908

Num of Steps Mean = 30.16

Num of Steps Std = 19.115815441670282

f2

Max Vals Mean = 2.9640322976036493

Max Vals Std = 0.01612094093067947

Num of Steps Mean = 74.14

Num of Steps Std = 25.756172075834563

0.2

f1

Max Vals Mean = 1.9936011019230013

Max Vals Std = 0.006045561175013421

Num of Steps Mean = 14.18

Num of Steps Std = 8.74

f2

Max Vals Mean = 2.9277022317351578

Max Vals Std = 0.031222771678639075

Num of Steps Mean = 38.32

Num of Steps Std = 12.468263712321777


Analysis:

Max Value:

As Step Size increases, the mean is further from real max (getters progressively lower) as the jump is bigger and less precise.
The mean’s std increases since the numbers are less precise (we have higher ‘jumps’ between neighbour points)

Total number of Steps:

As Step Size increases, the # steps decreases since we approach the max faster with higher ‘jumps’.
As Step Size increases. std lowers because it takes less steps to reach the goal overall and the average number of steps will be clustered around a smaller value (there is less of them)

---------------------
B. LOCAL BEAM SEARCH RESULTS: STEP SIZE 0.01 

f1 = sin(x/2) + cos(2y); 				f2 = -|x-2| - |0.5y +1| +3

DATA:

Beam Size
2

f1

Max Vals Mean = 1.99998142866

Max Vals Std = 1.57452148488e-05

Num of Steps Mean = 184.67

Num of Steps Std = 183.110243023

f2

Max Vals Mean = 2.99620987643

Max Vals Std = 0.00165756924315

Num of Steps Mean = 687.63

Num of Steps Std = 260.08439611

4

f1

Max Vals Mean = 1.99998413309

Max Vals Std = 1.35782545281e-05

Num of Steps Mean = 222.9

Num of Steps Std = 191.715700974

f2

Max Vals Mean = 2.996564007

Max Vals Std = 0.0015751994408

Num of Steps Mean = 713.49

Num of Steps Std = 269.408704202

8

f1

Max Vals Mean = 1.99998241483

Max Vals Std = 1.54285853596e-05

Num of Steps Mean = 175.01

Num of Steps Std = 183.020681618

f2

Max Vals Mean = 2.99641857993

Max Vals Std = 0.00159090246889

Num of Steps Mean = 740.17

Num of Steps Std = 251.720005363

16

f1

Max Vals Mean = 1.99998166154

Max Vals Std = 1.56654944678e-05

Num of Steps Mean = 160.74

Num of Steps Std = 172.25484724

f2

Max Vals Mean = 2.99624250874

Max Vals Std = 0.0015880752523

Num of Steps Mean = 670.48

Num of Steps Std = 264.889995281

Analysis:

Max Value:

The mean and Standard deviation seem identical for all beam sizes. These numbers are similar to the results from Hill Climbing. By the looks of it, Beam Size seems to affect how quickly we find the solution, not how precisely.

Total number of Steps:

For F1:

The mean values are lower due to the algorithm finding the solution much faster by considering multiple points simultaneously. The mean increases a bit at beam-size 4. There is a random factor from the initial points which could explain the bump.
 
For F2:

Compared to Hill Climbing for Step Size 0.01, the Mean is lower (as we get to the solution faster with more simultaneous runs. It increases for beam size 4 and 8, then decreases for 16. The std does not change much (between 250 - 270).
