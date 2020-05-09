***logger.py - documentation - last updated on 9.5.2020 by uuk***
___

    variable FUNNY_STRINGS: typing.List[str]
        list of funny strings in the crash logs
        adapted from mc version 1.15.2, decompiled with mc-forge located under net.minecraft.crash.CrashReport
        added some extra entries


    variable log_file: str - where the log is


    variable inter_home: str - where python lives

    function println(*msg, sep=" ", end="\n", write_into_console=True, write_into_log_file=True)
        
        prints an line into the console, same as print(), but with some extra cool stuff
        :param msg: the message(s) to print
        :param sep: how to separate them
        :param end: what to print on the end
        :param write_into_console: if it should be printed into the console
        :param write_into_log_file: if it should be printed into the log file
        

    function write_exception(*info)
        
        writes the last exception into the log & console together with the stack (formatted so it seems like it was never
            cached)
        :param info: the info about the exception
        

    function add_funny_line()
        
        will add an funny line into the console
        
