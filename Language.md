***Language.py - documentation - last updated on 26.5.2020 by uuk***
___

    variable LANGUAGES: dict - an dict representing the languages todo: remove

    variable ACTIVE_LANGUAGE
        change this for having another language, you have to include the needed lang files yourself to the resource system :/

    function get(key, formatting=None)
        
        get the translated name for an given key
        :param key: the key to get
        :param formatting: an list of formatting to use
        :return:


    function translate(s: str)
        
        translates an special string to an translated one
        :param s: an string defining it
        :return: the formatted string


    class Language
        
        Base class for Language-related stuff.
        Holds all translations for an given language


        static function from_file(cls, file: str, name=None)

        static function from_old_data(cls, file: str, name=None)

        static function from_data(cls, name: str, data: dict)

        function __init__(self)

            variable self.table

        function add_entry(self, key: str, value: str)

        function read_value(self, key: str)

    function from_directory(directory: str, modname: str)

    function from_mod_name(modname: str)