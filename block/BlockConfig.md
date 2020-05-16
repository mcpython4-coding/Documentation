***BlockConfig.py - documentation - last updated on 16.5.2020 by uuk***
___

    classes will be removed in the future as they can be replaced by tags


    class BlockConfigEntry
        
        Entry class for BlockConfig


        function __init__(self, configname: str)
            
            creates am mew entry
            :param configname: the name of the config class


            variable self.name: str

            variable self.affects: list

        function add_data(self, data: list)
            
            adds data to the system
            :param data: an lsit of data to apply


        function contains(self, item)
            
            will check if the item is marked as affected
            :param item: the item to check


        function __contains__(self, item)

    variable ENTRYS - todo: remove in a1.2.0

    variable ENTRIES: dict - the entries

        variable name