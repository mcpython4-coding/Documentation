This file is about porting mods.

Java Edition [post-excluding 1.12.2]

    Copy all assets folder [assets, data]
    Create an mod.json file and fill with information
    Package name can stay, but can also changed to an more pythonic name
    No proxies!
    Eventhandler completly changed -> event subscription see respectifly
    
    Mod instance version match!
    
    Check API changes between mc java and mcpython and your dependencies in java
    and python -> change code repectivly.
    
    Difference in names and packages of things -> check them
    
Java Edition [pre-including 1.12.2, post-excluding 1.7.10]

    Copy all assets folders [assets]
    move recipe files and loot tables to data-folded
    Rename blocks to block and items to item in the texture-dir and change
    references in item-model files and block-model files
    
    Port oredict entries to tags
    
    Rest see above
    
Java Edition [pre-1.7.10 including]

    No information, please follow mc-forge port notes to later versions and follow
    than above
    
Bedrock Edition

    No information, may come soon
    
raspberry pi edition - interface
    
    No socket interface provided, please use API directly. See default modding
    for more information, API interface may come soon.    