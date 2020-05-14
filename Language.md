***Language.py - documentation - last updated on 14.5.2020 by uuk***
___

    variable LANGUAGES

    variable ACTIVE_LANGUAGE
        change this for having another language, you have to include the needed lang files yourself :/

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

        static function from_file(cls, file: str, name=None)

        static function from_old_data(cls, file: str, name=None)

        static function from_data(cls, name: str, data: dict)

        function __init__(self)

            variable self.table

        function add_entry(self, key: str, value: str)

            variable self.table[key]

        function read_value(self, key: str)

    function from_directory(directory: str, modname: str)

        variable files

        variable m

    function from_mod_name(modname: str)