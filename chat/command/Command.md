***Command.py - documentation - last updated on 14.5.2020 by uuk***
___

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


        variable STRING_WITHOUT_QUOTES


        variable BOOLEAN


    class ParseMode extends enum.Enum
        
        An enum for how ParseType-entries are handled
        


        variable USER_NEED_ENTER - user must enter this


        variable OPTIONAL - user can enter this


    class SubCommand
        
        class for an part of an command. contains one parseable entry, one parsemode and an list of sub-commands
        

        function __init__(self, type, *args, mode=ParseMode.USER_NEED_ENTER, **kwargs)
            
            creates an new subcommand
            :param type: the type to use
            :param args: arguments to use for check & parsing
            :param mode: the mode to use
            :param kwargs: optional arguments for check & parsing
            

        function add_subcommand(self, subcommand)
            
            add an new subcommand to this
            :param subcommand: the subcommand to add
            :return: itself
            


    class ParseBridge
        
        An build system for commands
        

        function __init__(self, command)
            
            creates an new ParseBridge
            :param command: the command base class to use
            

        function add_subcommand(self, subcommand)
            
            add an new subcommand to this
            :param subcommand: the subcommand to add
            :return: itself
            


    class Command extends event.Registry.IRegistryContent

        variable TYPE

        static function insert_parse_bridge(parsebridge: ParseBridge)
            
            takes an ParseBridge and fills it with life
            :param parsebridge: the parsebridge to use
            

        static function parse(values: list, modes: list, info)
            
            parse the command
            :param values: the values parsed over parsebridge
            :param modes: the modes used (an list of decicions)
            :param info: an ParsingCommandInfo for parsing this command
            

        static function get_help() -> list
            
            :return: help pages for this command. a (commandprefix, info)-list
            todo: make translated
            
