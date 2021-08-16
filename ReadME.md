# Log-Parser
This repository is implementation Most Active Cookie parsing technique.

## Installation
####prerequisites:
```bash
python >=3.8
pip3
```

####Install from Source:
```bash
$ pip install --editable .
```
## Most Active Cookie
This Algorithm is for process the log file and return the most active cookie for a specific day. 
Please include a -f parameter for the filename to process and a -d parameter to specify the date.

### Assumptions:
* If multiple cookies meet that criteria, please return all of them on separate lines.
* You can assume -d parameter takes date in UTC time zone.
* You have enough memory to store the contents of the whole file.
* Cookies in the log file are sorted by timestamp (most recent occurrence is the first line of the file).

###Usage
```bash
$ log_parser cookie most_active -f [filename] -d [date]
```
example:
```bash
$ log_parser cookie most_active -f sample.csv -d 2018-12-22
```
### Implementation Details
#### Naive Approach:
The Naive approach to solve this problems is simply read the file line by line and count each cookie 
frequency and at the end print the cookies which has max count.

The Time complexity of this problem is always O(n) where n being number of lines in the file

#### Identifying the Bottleneck for better solution.
We also have the information that the log file is sorted with most recent occurrence is fist.
If we can use this information then we can improve the above algorithm by simply stopping it 
if the current reading line has date less than the required one.

But still this also does not improve any performance if the date request is oldest record
then we still end up reading the whole file.

The bottleneck of this problem is identifying the fist occurrence of the day among all days in the file.
If we can optimize this then we can improve the performance.

If we can find the requested date in **O(log n)** then it will be a major boost for the performance.
To achieve that we can use binary search since the data is already sorted.

Binary search compares the target value to the middle element of the array. If they are not equal, 
the half in which the target cannot lie is eliminated and the search continues on the remaining half,
 again taking the middle element to compare to the target value, and repeating this until the target value is found.

This is one potential solution to improve the performance of the algorithm but one major issue is we are dealing with files
which is more difficult than the normal array.

#### Implementing Binary Search for Files in Python

Since we need to move in the file independently normal read() or readline() is 
not sufficient. We need to read the file in binary mode which has support for reading 
from both ends using seek() function.

* start with low as first line and high as last line
* Every time fine the mid line and every since the mid element can mostly not be first 
element of the line.
* Move the pointer every time to starting of the line to read the whole line.
* Every time compare and modify the low and high values util the current mid value has requested
date and the previous line has different date

Now that we have the first occurrence of requested date. we can simply iterate the file 
and calculate the frequency of each cookie to find the answer we need.

#### Time Complexity Analysis
* if there is **N** lines and **M** occurrence of the requested date then total time complexity is 
**O(logN + M)**
* if **M == N** then it will become **O(N)**



