***logger.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable FUNNY_STRINGS
        adapted from mc version 1.15.2, decompiled with mc-forge located under net.minecraft.crash.CrashReport
        added some extra entries

    variable log_file_path

    variable execute_able_source

    variable ESCAPE

    function escape(string: str) -> str
        
        Helper function for escaping the string via above dict
        :param string: the string to escape
        :return: the escaped string


    function println(*msg, sep=" ", end="\n", console=True, log_file=True)
        
        will print an line into the console with formatting
        :param msg: the msg to log
        :param sep: how to separate the elements
        :param end: how the message ends
        :param console: if the data should be written into the console
        :param log_file: if the data should be written into the log file


    function transform_any_str_list(data: typing.Any) -> typing.List[str]
        
        Helper function for transforming any type to an list of strings split by "\n"
        :param data: the data to transform
        :return: the transformed data


    function write_into_container(
            *container_areas,
            style=("+", "-", "|"),
            header=None,
            outer_line_distance=2,
            empty_lines_before_separate=1
            ):
        
        will print the given data into an container-like structure
        :param container_areas: an list of container areas. Every area must be str or list. Areas are separated by
            horizontal lines from each other.
        :param style: the style to print with
        :param header: the header line of the table, may be str or list
        :param outer_line_distance: the distance from the vertical line to the string, in spaces
        :param empty_lines_before_separate: the new lines between text and an horizontal line


        variable areas

        variable max_characters_in_line

        variable horizontal_line

        variable empty_line

    class TableBuilder

        function __init__(
                self,
                style=("+", "-", "|"),
                header=None,
                outer_line_distance=2,
                empty_lines_before_separate=1,
                print_if_empty=False,
                ):

            variable self.areas

            variable self.style

            variable self.header

            variable self.outer_line_distance

            variable self.empty_lines_before_separate

            variable self.print_if_empty

        function next_area(self)

        function println(self, text)

        function print_nothing(self) -> bool

        function finish(self)

    function print_exception(*info)
        
        write the current exception into console and log
        :param info: the info to use


    function print_stack(*info)
        
        Prints the current calling stack into the console.
        :param info: info to provide

    
    machine: {}
    processor: {}
    python version: {}, implementation: {}


    function add_funny_line()