***Language.py - documentation***
___

This file is used for translating various texts with help of the 
language files of minecraft to translated once.

1. variable dict<str -> Language.Language> LANGUAGES: 
table name -> Language instance, used for translating strings

2. variable str ACTIVE_LANGUAGE: The name of the active language

3. def get(key: str, formatting=[]) -> str
    Translates an key to translated in active language. formatting are
    args that can be given to the function and are than 
    result.format(*formatting). If key is not found, key is returned as
    it is. 
    

4. def translate(s: str) -> str:
    former decode(s: str) -> str, deprecation since doc create.
    will translate the given string replacing every 
    "#\*\<translateable\>\*#" with the translated key. translateable 
    supports formatting by adding them with '|' after key

5. class Language(object):
    main class for Language system
    
    5.1 def from_file(cls, file: str, name=None)
    
    Will read file as Language file. Name is the language name. If name
    is None, name is extracted from filename. "file" is read through 
    ResouceLocator's read function with json system.
    WARNING: only new language format is supported at the moment,
    old format is planed but not implemented yet.
    
    5.2 def from_data(cls, name: str, data: dict)
    
    Will load the language data (new format!) into the system using name
    as language name. WARNING: if any to translate exists in system, 
    behaviour may be not what us wanted
    
    5.3 def \_\_init__(self)
    
    Creates an new Language-object with empty table
    
    5.4 def add_entry(self, key: str, value: str)
    
    Will add an new translated entry like replace(key, value) in every 
    string
    
    5.5 def read_value(self, key)
    
    Will access the key from the Language file. If not arrival, returns
    key.
    
6. def from_directory(directory, modname)
    
    will register all files in directory to the load stage
    for language files on event bus of modname.

7. def from_mod_name(modname: str)
    
    will call from_directory with default location 
    ("assets/\<modname\>/lang")

8. line 81: load minecraft files