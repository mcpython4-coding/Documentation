***ConfigFile.py - documentation - last updated on 19.5.2020 by uuk***
___

    class InvalidMapperData extends Exception

    class StringParsingPool

        function __init__(self, text: str)

            variable self.data

        function pop_line(self) -> str

        function pop_lines(self, count: int) -> list

        function get_line(self) -> str

    function toDataMapper(value)

    class IDataMapper

        function __init__(self, default_value)

            variable self.value

        function read(self)

        function write(self, value)

        function serialize(self) -> str

        function deserialize(self, d: StringParsingPool)

        function integrate(self, other)

    class ICustomDataMapper extends IDataMapper,  ABC
        
        For modders which would like to add their own config data types.
        Will need to add to the MAPPERS list


        static function valid_value_to_parse(cls, data) -> bool

        static function parse(cls, data) -> IDataMapper

    class DictDataMapper extends IDataMapper

        function __init__(self)

        function add_entry(self, key: str, default_mapper=None, description=None)

        function __getitem__(self, item)

        function __setitem__(self, key, value)

        function __contains__(self, item)

        function read(self) -> dict

        function write(self, value: dict)

        function serialize(self) -> str

        static function deserialize(cls, d: StringParsingPool)

        function integrate(self, other)

    class ListDataMapper extends IDataMapper

        function __init__(self, default=[])

        function __getitem__(self, item)

        function __setitem__(self, key, value)

        function __contains__(self, item)

        function append(self, item)

        function add(self, items: list)

        function read(self)

        function write(self, value)

        function serialize(self) -> str

        static function deserialize(cls, d: StringParsingPool)

    class IntDataMapper extends IDataMapper

        function __init__(self, value=0)

        function read(self)

        function write(self, value)

        function serialize(self) -> str

        static function deserialize(cls, d: StringParsingPool)

        function integrate(self, other)

    class FloatDataMapper extends IDataMapper

        function __init__(self, value=0.)

        function read(self)

        function write(self, value)

        function serialize(self) -> str

        static function deserialize(cls, d: StringParsingPool)

    class StringDataMapper extends IDataMapper

        function __init__(self, value="")

        function read(self)

        function write(self, value)

        function serialize(self) -> str

        static function deserialize(cls, d: StringParsingPool)

    class BooleanDataMapper extends IDataMapper

        function __init__(self, value=False)

        function read(self)

        function write(self, value)

        function serialize(self) -> str

        static function deserialize(cls, d: StringParsingPool)

    variable MAPPERS

    function stringToMapper(d: str) -> IDataMapper

    function bufferToMapper(d: StringParsingPool) -> IDataMapper

    class ConfigFile
        
        class representation of an config file. Process of config reading MUST be started by mod


        function __init__(self, file_name: str, assigned_mod: str)

            variable self.file_name

            variable self.assigned_mod

            variable self.main_tag

            variable self.file

        function add_entry(self, key: str, default_mapper=None, description=None)

        function __getitem__(self, item)

        function __setitem__(self, key, value)

        function __contains__(self, item)

        function build(self)

        function read(self)

        function write(self)

    @G.modloader("minecraft", "stage:mod:config:define") function load()