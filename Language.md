***Language.py - documentation - last updated on 9.5.2020 by uuk***
___

    This file is used for translating various texts with help of the
    language files of minecraft to translated once.
    

    variable LANGUAGES: dict - an list representing all loaded languages

    variable ACTIVE_LANGUAGE: str - an str representing the active language, only changeable on startup
        change this for having another language, you have to include the needed lang files yourself :/

    function get(key, formatting=None)

        
        get the translated name for an given key
        :param key: the key to get
        :param formatting: an list of formatting to use
        

    function translate(s: str)

        
        translates an special string to an translated one
        :param s: an string defining it
        :return: the formatted string
        

    class Language
        static function from_file(cls, file: str, name=None)

            
            loads an language file into the system
            :param file: the file to load
            :param name: the name to subscribe under, or None if to generate from file
            

        static function from_old_data(cls, file: str, name=None)

            
            loads an old pre-1.13 language file into the system
            :param file: the file to load
            :param name: the name to subscribe under, or None if to generate from file
            

        static function from_data(cls, name: str, data: dict)

            
            loads data direct into the system
            :param name: the name to register under
            :param data: the data to register
            

        function __init__(self)

        function add_entry(self, key: str, value: str)

            
            will insert an new entry into the language class
            :param key: the key to use
            :param value: the value to use
            :return:
            

        function read_value(self, key: str)

            
            reads an given key from the Language object
            :param key: the key
            :return: the translation
            

    function from_directory(directory: str, modname: str)

    function from_mod_name(modname: str)
