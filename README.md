# Concept
Adding annexes can be a pain in reports. This script aims to optimize this process by adding a link to the annex path in the main report file. The script then merges the reports for you.

# How it works 
The code reads the pdf, looks for a user sepecified symbol, e.g. `**__**` which is wrapped around a path so: `**__**Input/Test_simple/drawing.pdf**__**`. The pdf converter will then add this drawing pdf in the location of the path. **Currently it overwrites this page which is likely wanted**.

# Packages
Requires a python install and PyPDF2/pikepdf. The python file installs these. For development jupyter lab was used. 

# Useage
Feel free to use! Advised is to use [a github client to clone](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop) and run the .py file in a [python](https://www.python.org/downloads/) instance. 
