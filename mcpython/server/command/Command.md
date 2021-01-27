***Command.py - documentation - last updated on 27.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class CommandArgumentType extends enum.Enum
        
        An enum for command entries


        variable DEFINED_STRING
            A defined string like the string "as", without "

        variable INT
            An int. May be negative; cannot be NaN or inf
            todo: add a non-negative variant
            todo: add variant with NaN and inf

        variable STRING
            A string in "" or '', not mixed. May have spaces in it, determined by the " or ' s

        variable FLOAT
            A float number, can be negative; must be parse-able by float(), cannot contain spaces
            Represents a java double
            todo: add a non-negative variant

        variable BLOCK_NAME
            A name for a block. Can start with or without mod namespace; must be lookup-able in the block registry
            todo: add variant with forced namespace

        variable ITEM_NAME
            A name for an item. Can start with or without mod namespace; must be lookup-able in the item registry
            todo: add variant with forced namespace

        variable DIMENSION_NAME
            A name of a dimension in the active world

        variable SELECTOR
            A entity selector; defined by its own registry

        variable POSITION
            A position. May be selector; Selector must point to exactly one entity
            todo: add variant only for whole blocks

        variable SELECT_DEFINED_STRING
            A selection of different strings out of an list

        variable OPEN_END_UNDEFINED_STRING
            A variable list of strings

        variable STRING_WITHOUT_QUOTES
            A variable string without the "", without spaces

        variable BOOLEAN
            A boolean value

        function add_node(self, subcommand)

        function set_mode(self, parse_mode: "CommandArgumentMode")

    class CommandArgumentMode extends enum.Enum
        
        An enum for how ParseType-entries are handled
        todo: merge as optional: bool = False into node creation


        variable USER_NEED_ENTER - user must enter this entry

        variable OPTIONAL - user can enter this, but all sub-elements are than invalid

    class Node
        
        Class for an part of a command (a "Node"). Contains one parse-able entry, one ParseMode and a list of sub-commands
        todo: add variant without entry only linking a subset of nodes


        function __init__(
                self,
                entry_type: CommandArgumentType,
                *args,
                mode=CommandArgumentMode.USER_NEED_ENTER,
                on_node_iterated: typing.Callable[
                [typing.Any, typing.List, typing.List], None
                ] = None,
                on_node_executed: typing.Callable[
                [typing.Any, typing.List, typing.List], None
                ] = None,
                **kwargs
                ):
            
            Creates a new Node instance, representing
            :param entry_type: the type to use
            :param args: arguments to use for check & parsing
            :param mode: the mode to use
            :param kwargs: optional arguments for check & parsing
            :param on_node_executed: run when this node is the last one on the stack; signature: (info, values, node stack)
            :param on_node_iterated: run when this node is used during command parsing; signature: (info, values, node stack)
            todo: add attribute if it can be the last on the stack or not
            todo: add permission config entry
            todo: add "optional" parameter


            variable self.type

            variable self.mode

            variable self.nodes: typing.List["Node"]

            variable self.args

            variable self.kwargs

            variable self.on_node_executed

            variable self.on_node_iterated

        function add_node(self, node: typing.Union["Node", CommandArgumentType])
            
            Add a new sub-Node to this Node
            :param node: the Node to add
            :return: the current Node


        function get_node_ends(self) -> typing.Iterable["Node"]

    class CommandSyntaxHolder
        
        A build system for commands
        Inspired by minecraft's brigadier (https://github.com/Mojang/brigadier)


        function __init__(self, command: typing.Type["Command"])
            
            Creates a new CommandSyntaxHolder instance
            :param command: the command base class to use


            variable self.main_entry

            variable self.nodes

        function add_node(self, node: typing.Union[Node, CommandArgumentType])
            
            add a new Node to this
            :param node: the Node to add or a ParseType
            :return: the object invoked on (the self)


    class Command extends mcpython.common.event.Registry.IRegistryContent
        
        Base class for every command


        variable TYPE - the type definition for the registry

        static
        function insert_command_syntax_holder(command_syntax_holder: CommandSyntaxHolder)
            
            Takes a CommandSyntaxHolder and fills it with life
            :param command_syntax_holder: the syntax holder to use


        static
        function parse(values: list, modes: list, info)
            
            Parses the command
            :param values: the values parsed over parse bridge
            :param modes: the modes used (a list of decisions)
            :param info: a ParsingCommandInfo for parsing this command
            todo: remove


        static
        function get_help() -> list
            
            :return: help pages for this command. a "<command build>: <description>"-list
            todo: make translate-able
