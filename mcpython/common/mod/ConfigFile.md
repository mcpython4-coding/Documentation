***ConfigFile.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class InvalidMapperData extends Exception

    class StringParsingPool
        
        An system dedicated to handling an file context with the ability to pop and get lines.


        function __init__(self, text: str)

            variable self.data

        function pop_line(self) -> str

        function pop_lines(self, count: int) -> list

        function get_line(self) -> str

    function toDataMapper(value)
        
        will 'map' the given value to an IDataMapper-object
        :param value: the value to map
        :return: an IDataMapper-instance
        WARNING: in case of non normal data mapper found, an StringDataMapper is used


    class IDataMapper
        
        base class for every serialize-able content in config files


        function __init__(self, default_value)

            variable self.value

        function read(self)
            
            will return an pythonic representation of the content


        function write(self, value)
            
            will write to the internal buffer the data
            :param value: the value to write


        function serialize(self) -> str
            
            will compress the mapper into an string-representation
            :return: the stringified version


        function deserialize(self, d: StringParsingPool)
            
            will write certain data into the mapper
            :param d: the pool to read from


        function integrate(self, other)
            
            will integrate the data from other into this
            :param other: the mapper to integrate


    class ICustomDataMapper extends IDataMapper,  ABC
        
        For modders which would like to add their own config data types
        Will need to add to the MAPPERS list to work with config system
        WARNING: lower priority than normal aata mappers beside string mapper. Overriding with this not possible


        static
        function valid_value_to_parse(cls, data) -> bool

        static
        function parse(cls, data) -> IDataMapper

    class DictDataMapper extends IDataMapper
        
        implementation of an mapper mapping dict-objects


        function __init__(self)

        function add_entry(self, key: str, default_mapper=None, description=None)

        function __getitem__(self, item)

        function __setitem__(self, key, value)

        function __contains__(self, item)

        function read(self) -> dict

        function write(self, value: dict)

        function serialize(self) -> str

        static
        function deserialize(cls, d: StringParsingPool)

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

        static
        function deserialize(cls, d: StringParsingPool)

    class IntDataMapper extends IDataMapper

        function __init__(self, value=0)

        function read(self)

        function write(self, value)

        function serialize(self) -> str

        static
        function deserialize(cls, d: StringParsingPool)

        function integrate(self, other)

    class FloatDataMapper extends IDataMapper

        function __init__(self, value=0.0)

        function read(self)

        function write(self, value)

        function serialize(self) -> str

        static
        function deserialize(cls, d: StringParsingPool)

    class StringDataMapper extends IDataMapper

        function __init__(self, value="")

        function read(self)

        function write(self, value)

        function serialize(self) -> str

        static
        function deserialize(cls, d: StringParsingPool)

    class BooleanDataMapper extends IDataMapper

        function __init__(self, value=False)

        function read(self)

        function write(self, value)

        function serialize(self) -> str

        static
        function deserialize(cls, d: StringParsingPool)

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

    @shared.mod_loader("minecraft", "stage:mod:config:define")
    function load()