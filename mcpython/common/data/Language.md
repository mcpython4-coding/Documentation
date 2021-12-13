***Language.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable ACTIVE_LANGUAGE - the active language
        change this for having another language, you have to include the needed lang files yourself :/

    function get(key: str, formatting=None)
        
        Get the translated name for a given key and applies a formatting when needed
        :param key: the key to get
        :param formatting: an list of formatting to use
        :return:


    function translate(s: str)
        
        Translates a special string to a translated one, sections in *#...#* are put into get()
        :param s: an string defining it
        :return: the formatted string


    class Language
        
        Base class for language data
        Handles all translations of the language set

            
            will load a file into the system
            :param file: the file to load, as ResourceLocate-able
            :param name: the name of the language to use or None for generation from file name


                    variable data
            
            will load an file from the old format into the system
            :param file: the file to load
            :param name: the name to load under, or None if to read from the file name


            variable name

                variable LANGUAGES[name]

            variable language

                variable lines

                variable language.table[pre]
            
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

    function load()