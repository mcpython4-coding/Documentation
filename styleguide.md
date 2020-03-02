How to create documentation files?

Every python file of the program should have at the same level in the 
documentation an .md file named the same as the corresponding python 
file. If there is not one, it will be created.

If your have any questions, feel free to ask on the "issues" page on github.

Additionally, there can be an general.md file in any directory to 
describe what in this directory exists and how to work with them.

How to format these .md files? [updated version]

Every .md files starts with an header as the following:

-------------------

**\<your file name>.py - Documentation - Last updated on \<update date formatted dd/mm/yyyy> by \<your nickname>**

--------------

\<general info about the file>

Structure:

<an list of entries, splitted up by \n\n>
    
    class <classname> extends <super classes> followed by general infomation about the class and an list of sub-entries
    
    function <function name> <parametername: valuetype> -> <return type> followed by general information
        parameters may be in [] when optional
    
    attribute <name>: <data type> followed by information what it does 
    
    functions and attributes can have "static " prefix to mark them as static 