***Builder.py - documentation - last updated on 16.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class CommandExecutionTracker
        
        Helper code for decoding a command
        It is "tracking" were in the command we are, what values we have etc.
        It is part of the two major stages of decoding, being the node selection system and on the other side being
            the actual parsing into values


        static
        function from_string(cls, string: str) -> "CommandExecutionTracker"
            
            Splits up the command into parts
            :param string: the string
            todo: do not split when in " or ' or brackets


        function __init__(self, content: typing.List[str] = None)
            
            Creates a new tracker
            Use from_string() when working with strings
            :param content: optional, a list of strings as bases


            variable self.content

            variable self.collected_values

            variable self.current_index

            variable self.index_pool

            variable self.parsing_errors

        function collect(self, value)
            
            Adds a value to the parsed value list
            :param value: the value


        function rollback(self)
            
            Rolls back this tracker to the latest saved point; the saved point is deleted


        function get(self, offset: int = 0) -> str
            
            Gets the current part
            :param offset: how many parts to go ahead of current pointer
            :return: the part


        function get_multi(self, count: int, offset: int = 0) -> typing.List[str]
            
            Similar to get(), but will return the next <count> entries
            :param count: the amount of entries to get
            :param offset: the offset from current pointer
            :return: the parts, as a list


        function increase(self, count: int)
            
            Increases the local pointer by <count>


        function save(self)
            
            Saves the current state for later rollback()-s


        function has(self, count: int) -> bool
            
            Checks if there are at least <count> parts pending
            Use this before calling get() or get_multi()


    class ICommandElementIdentifier extends ABC
        
        An abstract entry in the parsing tree
        Defines validation & parsing of entries


        function is_valid(self, node: "CommandNode", tracker: CommandExecutionTracker) -> bool
            
            Checks if the data at the current tracker pointer is a valid entry here
            :param node: the current node
            :param tracker: the tracker
            :return: if valid or not


        function parse(self, node: "CommandNode", tracker: CommandExecutionTracker)
            
            Parses the tracker data
            Does not need to do checks, is_valid() must be called beforehand
            WARNING: if is_valid() return True, the tracker will be saved, and than this method is directly
                invoked, before checking following nodes
            WARNING: do NOT forget to increase tracker pointer by calling increase()


    class DefinedString extends ICommandElementIdentifier
        
        Class for a set of defines strings without quotation marks
        Used internally also as the main node of a command
        todo: add a node only containing defined strings -> faster parsing by dict lookup


        function __init__(self, *strings: str)

            variable self.strings

        function is_valid(self, node: "CommandNode", tracker: CommandExecutionTracker) -> bool

        function parse(self, node: "CommandNode", tracker: CommandExecutionTracker)

        function __eq__(self, other)

    class Int extends ICommandElementIdentifier
        
        Helper for integers, with auto-parsing and validation


        function __init__(
                self,
                only_positive=False,
                only_negative=False,
                include_zero=True,
                value_range=None,
                ):
            
            :param only_positive: only positive integers allowed
            :param only_negative: only negative integers allowed
            :param include_zero: zero allowed
            :param value_range: a range of (min, max) for the integer, or None for open range


            variable self.value_range

            variable self.include_zero

            variable self.only_negative

            variable self.only_positive

        function is_valid(self, node: "CommandNode", tracker: CommandExecutionTracker) -> bool

            variable v

                variable v

        function parse(self, node: "CommandNode", tracker: CommandExecutionTracker)

    class IntPosition extends ICommandElementIdentifier
        
        A position, in int terms
        todo: allow local references


        function is_valid(self, node: "CommandNode", tracker: CommandExecutionTracker) -> bool

        function parse(self, node: "CommandNode", tracker: CommandExecutionTracker)

        function __eq__(self, other)

    class Position extends ICommandElementIdentifier
        
        A position, in float terms
        todo: allow local references, and selectors


        function is_valid(self, node: "CommandNode", tracker: CommandExecutionTracker) -> bool

        function parse(self, node: "CommandNode", tracker: CommandExecutionTracker)

        function __eq__(self, other)

    class RegistryContent extends ICommandElementIdentifier
        
        Registry entry getter
        registry name given, will return the entry of the registry by calling get() on it


        function __init__(self, registry: str)

            variable self.inner_registry

        function is_valid(self, node: "CommandNode", tracker: CommandExecutionTracker) -> bool

        function parse(self, node: "CommandNode", tracker: CommandExecutionTracker)

        function __eq__(self, other)

    class Block extends ICommandElementIdentifier
        
        Special entry for a block, for adding meta information


        variable BLOCK_REGISTRY

        function is_valid(self, node: "CommandNode", tracker: CommandExecutionTracker) -> bool

            variable element

            variable name

        function parse(self, node: "CommandNode", tracker: CommandExecutionTracker)

        function __eq__(self, other)

    class Item extends ICommandElementIdentifier
        
        Special entry for an item, for adding meta information


        variable ITEM_REGISTRY

        function is_valid(self, node: "CommandNode", tracker: CommandExecutionTracker) -> bool

            variable element

            variable name

        function parse(self, node: "CommandNode", tracker: CommandExecutionTracker)

        function __eq__(self, other)

    class Selector extends ICommandElementIdentifier
        
        A selector, to select entities in the world


        variable SELECTORS

        function __init__(self, max_entities=-1)

            variable self.max_entities

        function is_valid(self, node: "CommandNode", tracker: CommandExecutionTracker) -> bool

        function parse(self, node: "CommandNode", tracker: CommandExecutionTracker)

            variable meta

            variable f
                todo: check limit

        function __eq__(self, other)

    class AnyString extends ICommandElementIdentifier

        variable INSTANCE: typing.Optional["AnyString"]

        function __init__(self)

            variable self.opened

        function is_valid(self, node: "CommandNode", tracker: CommandExecutionTracker) -> bool

        function parse(self, node: "CommandNode", tracker: CommandExecutionTracker)

        function open(self)

    variable AnyString.INSTANCE

    class CommandNode
        
        A node in the tree of a command


        function __init__(
                self,
                inner_identifier: ICommandElementIdentifier,
                execute_on_client=False,
                valid_on_dedicated=True,
                valid_on_integrated=True,
                ):

            variable self.inner_identifier

            variable self.execute_on_client

            variable self.valid_on_dedicated

            variable self.valid_on_integrated

            variable self.following_nodes: typing.List["CommandNode"]

            variable self.on_execution_callbacks

            variable self.name

            variable self.info_text

            variable self.exception_handlers

        function than(self, node: "CommandNode")
            
            Adds a internal node into the system
            :param node: the node to add


        function on_execution(self, func: typing.Callable)

        function of_name(self, name: str)

        function info(self, text: str)

        function with_handle(
                self, error: typing.Type[Exception], message_formatter: typing.Callable
                ):

        function get_executing_node(
                self, tracker: CommandExecutionTracker
                ) -> typing.Optional["CommandNode"]:
            
            Parsing method for parsing a CommandExecutionTracker
            :param tracker: the tracker
            :return: when arrival, the end CommandNode for execution


                variable aft

        function get_similar_node(self, node: "CommandNode") -> typing.Optional["CommandNode"]
            
            Helper method for getting a similar node down the tree
            Similar nodes have the same inner identifier. The rest is currently ignored
            WARNING: currently, recursive trees may crash
            :param node: the node to compare to
            :return: the node or None


                variable track
                    todo: check for circular calls

        function run(self, env, data)

    class Command extends CommandNode
        
        The "base"-Node. It contains a little bit more meta-information, otherwise it is simply a normal CommandNode
        <name> is without the / in front


        function __init__(
                self,
                name: str,
                execute_on_client=False,
                valid_on_dedicated=True,
                valid_on_integrated=True,
                ):

            variable self.name

            variable self.additional_names

        function alias(self, name: str)