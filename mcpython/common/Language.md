***Language.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    variable ACTIVE_LANGUAGE - the active language
        change this for having another language, you have to include the needed lang files yourself :/

    function get(key: str, formatting=None)
        
        get the translated name for an given key
        :param key: the key to get
        :param formatting: an list of formatting to use
        :return:


    function translate(s: str)
        
        translates an special string to an translated one
        :param s: an string defining it
        :return: the formatted string


    class Language
        
        base class for language data


        static
        function from_file(cls, file: str, name=None)
            
            will load an file into the system
            :param file: the file to load, as ResourceLocate-able
            :param name: the name of the language to use or None for generation from file name


        static
        function from_old_data(cls, file: str, name=None)
            
            will load an file from the old format into the system
            :param file: the file to load
            :param name: the name to load under, or None if to read from the file name


                variable LANGUAGES[name]

            variable language

                variable lines

                variable language.table[pre]

        static
        function from_data(cls, name: str, data: dict)
            
            will load data into the system
            :param name: the name to load under
            :param data: the data to load


                variable LANGUAGES[name].table

                variable LANGUAGES[name]

                variable LANGUAGES[name].table

        function __init__(self)

        function add_entry(self, key: str, value: str)

        function read_value(self, key: str)

    function from_directory(directory: str, modname: str)
        
        will create Language data for an directory
        :param directory: the directory name
        :param modname: the mod name


    function from_mod_name(modname: str)