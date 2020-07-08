***logger.py - documentation - last updated on 14.6.2020 by uuk***
___

    variable FUNNY_STRINGS
        adapted from mc version 1.15.2, decompiled with mc-forge located under net.minecraft.crash.CrashReport
        added some extra entries

    variable log_file

    variable inter_home

    variable ESCAPE

    function escape(string: str) -> str
        
        will escape the string correctly
        :param string: the string to escape
        :return: the escaped string


    function println(*msg, sep=" ", end="\n", write_into_console=True, write_into_log_file=True)
        
        will print an line into the console with formatting
        :param msg: the msg to log
        :param sep: how to separate the elements
        :param end: how the message ends
        :param write_into_console: if the data should be written into the console
        :param write_into_log_file: if the data should be written into the log file


    function _transform_any_str_list(data) -> list

    function write_into_container(*container_areas, style=("+", "-", "|"), header=None, outer_line_distance=2,
            empty_lines_before_separate=1):
        
        will print the given data into an container-like structure
        :param container_areas: an list of container areas. Every area must be str or list. Areas are separated by
            horizontal lines from each other.
        :param style: the style to print with
        :param header: the header line of the table, may be str or list
        :param outer_line_distance: the distance from the vertical line to the string, in spaces
        :param empty_lines_before_separate: the new lines between text and an horizontal line


    function write_exception(*info)
        
        write the current exception into console and log
        :param info: the info to use

    
    machine: {}
    processor: {}
    python version: {}, implementation: {}


    function add_funny_line()