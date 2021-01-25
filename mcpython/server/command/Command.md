***Command.py - documentation - last updated on 25.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class ParseType extends enum.Enum
        
        An enum for command entries


        variable DEFINED_STRING
            A defined string like the string "as", without "

        variable INT
            An int. May be negative; cannot be NaN or inf

        variable STRING
            A string in "" or '', not mixed. May have spaces in it

        variable FLOAT
            A float number, can be negative; must be parse-able by float(), cannot contain spaces
            Represents a java double

        variable BLOCK_NAME
            A name for a block. Can start with or without mod namespace; must be lookup-able in the block registry

        variable ITEM_NAME
            A name for an item. Can start with or without mod namespace; must be lookup-able in the item registry

        variable SELECTOR
            A entity selector; defined by its own registry

        variable POSITION
            A position. May be selector for position; Selector must be unique

        variable SELECT_DEFINED_STRING
            A selection of different strings out of an list

        variable OPEN_END_UNDEFINED_STRING
            A variable list of strings

        variable STRING_WITHOUT_QUOTES
            A variable string without the ""

        variable BOOLEAN
            A boolean value

        function add_subcommand(self, subcommand)

        function set_mode(self, parse_mode: "ParseMode")

    class ParseMode extends enum.Enum
        
        An enum for how ParseType-entries are handled


        variable USER_NEED_ENTER - user must enter this entry

        variable OPTIONAL - user can enter this, but all sub-elements are than invalid

    class SubCommand
        
        Class for an part of an command. contains one parse-able entry, one ParseMode and an list of sub-commands


        function __init__(self, entry_type: ParseType, *args, mode=ParseMode.USER_NEED_ENTER, **kwargs)
            
            Creates an new subcommand
            :param entry_type: the type to use
            :param args: arguments to use for check & parsing
            :param mode: the mode to use
            :param kwargs: optional arguments for check & parsing


            variable self.type

            variable self.mode

            variable self.sub_commands: typing.List["SubCommand"]

            variable self.args

            variable self.kwargs

        function add_subcommand(self, subcommand: typing.Union["SubCommand", ParseType])
            
            Add an new SubCommand to this SubCommand
            :param subcommand: the SubCommand to add
            :return: itself


    class ParseBridge
        
        A build system for commands
        Inspired by minecraft's brigadier (https://github.com/Mojang/brigadier)
        todo: every SubCommand should have an onParsingEndHere method executing the command instead of
            a single function giving the tree


        function __init__(self, command)
            
            creates an new ParseBridge
            :param command: the command base class to use


            variable self.main_entry

            variable self.sub_commands

        function add_subcommand(self, subcommand: typing.Union[SubCommand, ParseType])
            
            add an new subcommand to this
            :param subcommand: the subcommand to add or an ParseType
            :return: the object invoked on (the self)


    class Command extends mcpython.common.event.Registry.IRegistryContent
        
        Base class for every command


        variable TYPE - the type definition for the registry

        static
        function insert_parse_bridge(parse_bridge: ParseBridge)
            
            Takes an ParseBridge and fills it with life
            :param parse_bridge: the parse bridge to use


        static
        function parse(values: list, modes: list, info)
            
            Parses the command
            :param values: the values parsed over parse bridge
            :param modes: the modes used (a list of decisions)
            :param info: a ParsingCommandInfo for parsing this command


        static
        function get_help() -> list
            
            :return: help pages for this command. a "<command build>: <description>"-list
            todo: make translate-able
