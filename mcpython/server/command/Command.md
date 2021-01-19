***Command.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class ParseType extends enum.Enum
        
        An enum for command entrys


        variable DEFINIED_STRING - a definied string like "as"

        variable INT - an int. may be negative

        variable STRING - an string in "" or ''. not mixed. may have spaces in it

        variable FLOAT - an float number, can be negative

        variable BLOCKNAME - an name for an block. can start with or without mod prefix

        variable ITEMNAME - an name for an item. can start with or without mod prefix

        variable SELECTOR - an entity selector

        variable POSITION - an position. may be selector

        variable SELECT_DEFINITED_STRING - an selection of diffrent strings out of an list

        variable OPEN_END_UNDEFINITED_STRING - an variable list of strings

        variable STRING_WITHOUT_QUOTES - an varialbe string without the ""

        variable BOOLEAN - an boolean value

        function add_subcommand(self, subcommand)

        function set_mode(self, parsemode)

    class ParseMode extends enum.Enum
        
        An enum for how ParseType-entries are handled


        variable USER_NEED_ENTER - user must enter this entry

        variable OPTIONAL - user can enter this, but all sub-elements are than invalid

    class SubCommand
        
        class for an part of an command. contains one parse-able entry, one ParseMode and an list of sub-commands


        function __init__(self, type, *args, mode=ParseMode.USER_NEED_ENTER, **kwargs)
            
            creates an new subcommand
            :param type: the type to use
            :param args: arguments to use for check & parsing
            :param mode: the mode to use
            :param kwargs: optional arguments for check & parsing


            variable self.type

            variable self.mode

            variable self.sub_commands

            variable self.args

            variable self.kwargs

        function add_subcommand(self, subcommand)
            
            add an new SubCommand to this SubCommand
            :param subcommand: the SubCommand to add
            :return: itself


    class ParseBridge
        
        An build system for commands


        function __init__(self, command)
            
            creates an new ParseBridge
            :param command: the command base class to use


            variable self.main_entry

            variable self.sub_commands

        function add_subcommand(self, subcommand)
            
            add an new subcommand to this
            :param subcommand: the subcommand to add or an ParseType
            :return: the object invoked on (the self)


    class Command extends mcpython.common.event.Registry.IRegistryContent
        
        base class for every command


        variable TYPE - the type defintion for the registry

        static
        function insert_parse_bridge(parsebridge: ParseBridge)
            
            takes an ParseBridge and fills it with life
            :param parsebridge: the parsebridge to use


        static
        function parse(values: list, modes: list, info)
            
            parse the command
            :param values: the values parsed over parsebridge
            :param modes: the modes used (an list of decicions)
            :param info: an ParsingCommandInfo for parsing this command


        static
        function get_help() -> list
            
            :return: help pages for this command. a "<command build>: <description>"-list
            todo: make translated
