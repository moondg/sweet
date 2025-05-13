# SWEET Workflow for Efficient data Evaluation Tool

## Setup

1. Install [VSCode](https://code.visualstudio.com/).
2. In File Explorer, double-click the `OPEN.code-workspace` file to open it.
3. Install the recommended extensions.
   *(Wait for the popup in the lower-right corner prompting you to install them.)*
4. Install Python 3.9 or later. *(Not covered here; I'm using 3.13.3)*
5. Open `program.ipynb` from the Explorer in VSCode.
6. Click **Select Kernel** → **Python Environments...** → **Create Python Environment** → **Venv**.
7. You may see a list of Python versions — choose the one you installed.
8. See [Next](#how-to-use).

## How to use

1. Put your data folder in `data`. Make it if not exists. For example:
```
data
├── 25.04.15
│   ├── pfoa
│   │   ├── 1
│   │   │   ├── 032410023904.dat
│   │   │   ├── 032410023915.dat
│   │   ├── 2
│   │   │   ├── 032410024828.dat
│   │   │   ├── 032410024857.dat
│   │   ├── 3
│   │   │   ├── 032410031711.dat
│   │   │   ├── 032410031758.dat
│   │   └── 4
│   │       ├── 032410032628.dat
│   │       ├── 032410032655.dat
```
2. Open `program.ipynb` and set the appropriate data folder path in the second cell by passing it to `Manager()`. For example, if you want to analyze folder ***2*** inside ***pfoa***, set `Manager()` as follows:
```python
# Use '/' to express folder
manager = Manager(r"25.04.15/pfoa/1")
```

3. Cells can be run with `Shift + Enter`. Run the cells in `program.ipynb` from top to bottom — execution order matters. Or, you can simply click ***Restart*** -> ***Run All***.


## How to set parameters
The linear traversal is performed from the far right of the attach signal graph. The program first traverses the horizontal (flat) section, then the linear section. The graph assumes that, when read from right to left, the horizontal section ends and the linear section begins immediately afterward.

+ `window_size` (default 5): Determines how much data to average in the [moving average](https://en.wikipedia.org/wiki/Moving_average). A larger window will smooth the graph more, which can cause horizontal region detection to fail.
+ `gradient_threshold` (default 0.003): If the slope exceeds this value, the flat region is considered to be over.
+ `curvature_threshold` (default 0.3): If the curvature does not exceed this value, it is considered a linear region. If it exceeds the value, the linear region is considered to be over.
+ `minimum_search_range` (default 30): Since the curvature-based minimum location is not exact(but close), the exact minimum is searched for within this range.


## Troubleshooting
### No ipykernel
Error Message
> Running cells with '.venv (Python 3.13.3)' requires the ipykernel package.\
> Install 'ipykernel' into the Python environment.

Install ***ipykernel***
### No library
Error Message
> ModuleNotFoundError: No module named 'numpy'

This is because your computer does not have a specific library — in this case, ***numpy***. Find the cell that contains:
```python
# !pip install numpy
```
`!pip install *` installs a specific library on your computer. Remove the `#` and run the cell with `Shift + Enter`. You may want to add the `#` back afterward.
