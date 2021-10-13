# Dott Technical Assignment
### Description
Given a bitmap of size n x m, where each pixel is either white(1) or black(0), but at least one is white, we compute for each pixel the distance the nearest white.<br/>
The distance between two pixels p1(i1,j1) and p2(i2,j2) is given as follows d(p1,p2) = |i2-i1| + |j2-j1|.

#### Solution
This solution uses DFS and dynamic programming in order to compute the distance from the nearest white point.<br/>
The logic behind my idea is that the shortest path between any pixel and the closest white point should not include opposing directions.<br/>
Therefore, I proposed to traverse the bitmap 4 four times, each time taking into consideration two different non opposing directions (up-left, up-right, down-left, down-right).<br/>
For example, if we take the down-right case, for a pixel (i,j), the distance to the closed white point is <br/> d(i,j) = min(d(i+1, j) + d(i, j+1)) + 1.<br/>
In the end, for each pixel, the minimal distance is the minimum of the 4 distances obtained from the 4 traversals.<br/>

### Installation
Install python with version 3.7 or later https://www.python.org/downloads/ . <br/>
Use the package manager [pip](https://pip.pypa.io/en/stable/)  and requirements.txt to install the necessary python packages.
````bash
pip install -r requirements.txt
````
### Usage
Run the main file
````bash
python main.py
````
1. Enter number of test cases
2. Enter number of lines and columns of the bitmap separated by as space
3. Enter the bitmap line by line 

### Unittests
To apply the implemented unittests, run the following command
````bash
pytest test.py
````


