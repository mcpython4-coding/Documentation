How to create documentation files?

Every python file of the program has at the same level in the 
documentation an .md file named the same as the corresponding python 
file.

Additionally, there can be an general.md file in any directory to 
describe what in this directory exists and how to work with them.

How to format .md file for an python file?

short style guide guide:

every style definition is formatted with one tab. text to insert as
blank text, in "<>" descriptions on what to insert and in "\[\]" 
comments  

    ***<the name of the python file with path> - documentation***
    ___
    
    This file is used for <what it is used for> by <what uses this file>
    It contains <quick overview about what's in it>
    
    <some general words around content>
    
    <now follows an list of everything found in the file, following the following style>
    
    id is an version like structure like 1.1.1 1.1.2, 2.1, ...
    sub-version is for class-sub-structures or function descriptions,
    otherwise count on the level one up
    
    type is full path to attribute using <path without py>.<substructure>
    
    
    for functional script parts:
        <id> line <from>-<to>: <description>
        
    for attributes:
        <id> variable <name>: <type>: <description>   
    
    for functions:
        <id> def <function name>(*<parameter>: <type>) -> <returntype>:
        <description on what the function does, including:
        parameter work, raising (when known), affect on the game...>
        *<subpart>
     
    for classes:
        <id> class <class name>(*<supers>):
        <description on what the class is used for> 
        *<subpart>

How to format the general.md files?

    <the name of the directory> - general documentation
    This directory is used for <usage>
    It contains the following files:
    *<filename>: <very short overview>
    
    [optional]
    This directory was added by <who added it> on <when it was added>
    

How to mark something as deprecated?
use "WARNING: deprecated on \<date when deprecated\> by 
\<who deprecated it\>", add marker to code and add it to deprecated.txt

Changes to these file are always accepted. Please do not forget on
updating affected files.
     
    