***Tag.py - documentation - last updated on 8.6.2020 by uuk***
___

    class Tag

        static
        function from_data(master, tagname: str, data: dict)

        function __init__(self, master, name: str, entries)

            variable self.entries

            variable self.master

            variable self.name

            variable self.load_tries

        function get_dependencies(self) -> list

        function build(self)