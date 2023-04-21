# Concept
adding annexes can be a pain in reports. This script aims to optimize this process by adding a link to the annex path in the file.

# How it works 
The code reads the pdf, looks for a user sepecified symbol, e.g. `**__**` which is wrapped around a path so: `**__**Input/Test_simple/drawing.pdf**__**`. The pdf converter will then add this drawing pdf in the location of the path. **Currently it overwrites this page which is likely wanted**.

# Packages
Requires a python install and PyPDF2/pikepdf, for development jupyter lab was used. 

# Useage
Feel free to use!