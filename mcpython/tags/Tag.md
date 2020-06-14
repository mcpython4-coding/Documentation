***Tag.py - documentation - last updated on 14.6.2020 by uuk***
___

    class Tag
        
        class holding an single tag


        static
        function from_data(master, tagname: str, data: dict)
            
            will create an new tag from data
            :param master: the group to use
            :param tagname: the name of the tag
            :param data: the data to use
            :return the tag instance


        function __init__(self, master, name: str, entries: list)
            
            will create an new tag instance from an list of entries
            :param master: the tag group to use
            :param name: the name of the tag
            :param entries: the entries to use


            variable self.entries

            variable self.master

            variable self.name

            variable self.load_tries

        function get_dependencies(self) -> list
            
            will return an list of tags these tag links to
            :return the list


        function build(self)
            
            will build the tag
