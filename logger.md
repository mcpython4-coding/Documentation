***logger.py - documentation - last updated on 8.6.2020 by uuk***
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


    function write_exception(*info)
        
        write the current exception into console and log
        :param info: the info to use

    
    machine: {}
    processor: {}
    python version: {}, implementation: {}


    function add_funny_line()