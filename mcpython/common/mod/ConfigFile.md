***ConfigFile.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class InvalidMapperData extends Exception

    @deprecation.deprecated() class StringParsingPool
        
        An system dedicated to handling an file context with the ability to pop and get lines.


        function __init__(self, text: str)

            variable self.data

        function pop_line(self) -> str

        function pop_lines(self, count: int) -> list

        function get_line(self) -> str

    @deprecation.deprecated()
    function toDataMapper(value)
        
        will 'map' the given value to an IDataMapper-object
        :param value: the value to map
        :return: an IDataMapper-instance
        WARNING: in case of non normal data mapper found, an StringDataMapper is used


            variable obj

            variable obj

    class IDataMapper
        
        base class for every serialize-able content in config files


        @deprecation.deprecated()
        function __init__(self, default_value)

            variable self.value

        @deprecation.deprecated()
        function read(self)
            
            will return an pythonic representation of the content


        @deprecation.deprecated()
        function write(self, value)
            
            will write to the internal buffer the data
            :param value: the value to write


        @deprecation.deprecated()
        function serialize(self) -> str
            
            will compress the mapper into an string-representation
            :return: the stringified version


        @deprecation.deprecated()
        function deserialize(self, d: StringParsingPool)
            
            will write certain data into the mapper
            :param d: the pool to read from


        @deprecation.deprecated()
        function integrate(self, other)
            
            will integrate the data from other into this
            :param other: the mapper to integrate


    class ICustomDataMapper extends IDataMapper,  ABC
        
        For modders which would like to add their own config data types
        Will need to add to the MAPPERS list to work with config system
        WARNING: lower priority than normal aata mappers beside string mapper. Overriding with this not possible


        @deprecation.deprecated()
        static
        function valid_value_to_parse(cls, data) -> bool

        @deprecation.deprecated()
        static
        function parse(cls, data) -> IDataMapper

    class DictDataMapper extends IDataMapper
        
        implementation of an mapper mapping dict-objects


        @deprecation.deprecated()
        function __init__(self)

        @deprecation.deprecated()
        function add_entry(self, key: str, default_mapper=None, description=None)

        @deprecation.deprecated()
        function __getitem__(self, item)

        @deprecation.deprecated()
        function __setitem__(self, key, value)

        @deprecation.deprecated()
        function __contains__(self, item)

        @deprecation.deprecated()
        function read(self) -> dict

        @deprecation.deprecated()
        function write(self, value: dict)

        @deprecation.deprecated()
        function serialize(self) -> str

        @deprecation.deprecated()
        static
        function deserialize(cls, d: StringParsingPool)

        @deprecation.deprecated()
        function integrate(self, other)

    class ListDataMapper extends IDataMapper

        @deprecation.deprecated()
        function __init__(self, default=[])

        @deprecation.deprecated()
        function __getitem__(self, item)

        @deprecation.deprecated()
        function __setitem__(self, key, value)

        @deprecation.deprecated()
        function __contains__(self, item)

        @deprecation.deprecated()
        function append(self, item)

        @deprecation.deprecated()
        function add(self, items: list)

        @deprecation.deprecated()
        function read(self)

        @deprecation.deprecated()
        function write(self, value)

        @deprecation.deprecated()
        function serialize(self) -> str

        @deprecation.deprecated()
        static
        function deserialize(cls, d: StringParsingPool)

    class IntDataMapper extends IDataMapper

        @deprecation.deprecated()
        function __init__(self, value=0)

        @deprecation.deprecated()
        function read(self)

        @deprecation.deprecated()
        function write(self, value)

        @deprecation.deprecated()
        function serialize(self) -> str

        @deprecation.deprecated()
        static
        function deserialize(cls, d: StringParsingPool)

        function integrate(self, other)

    class FloatDataMapper extends IDataMapper

        @deprecation.deprecated()
        function __init__(self, value=0.0)

        @deprecation.deprecated()
        function read(self)

        @deprecation.deprecated()
        function write(self, value)

        @deprecation.deprecated()
        function serialize(self) -> str

        @deprecation.deprecated()
        static
        function deserialize(cls, d: StringParsingPool)

    class StringDataMapper extends IDataMapper

        @deprecation.deprecated()
        function __init__(self, value="")

        @deprecation.deprecated()
        function read(self)

        @deprecation.deprecated()
        function write(self, value)

        @deprecation.deprecated()
        function serialize(self) -> str

        @deprecation.deprecated()
        static
        function deserialize(cls, d: StringParsingPool)

    class BooleanDataMapper extends IDataMapper

        @deprecation.deprecated()
        function __init__(self, value=False)

        @deprecation.deprecated()
        function read(self)

        @deprecation.deprecated()
        function write(self, value)

        @deprecation.deprecated()
        function serialize(self) -> str

        @deprecation.deprecated()
        static
        function deserialize(cls, d: StringParsingPool)

    variable MAPPERS

    @deprecation.deprecated()
    function stringToMapper(d: str) -> IDataMapper

    @deprecation.deprecated()
    function bufferToMapper(d: StringParsingPool) -> IDataMapper

    class ConfigFile
        
        class representation of an config file. Process of config reading MUST be started by mod


        @deprecation.deprecated()
        function __init__(self, file_name: str, assigned_mod: str)

            variable self.file_name

            variable self.assigned_mod

            variable self.main_tag

            variable self.file

        @deprecation.deprecated()
        function add_entry(self, key: str, default_mapper=None, description=None)

        @deprecation.deprecated()
        function __getitem__(self, item)

        @deprecation.deprecated()
        function __setitem__(self, key, value)

        @deprecation.deprecated()
        function __contains__(self, item)

                variable old_buffer

                    variable self.main_tag

        @deprecation.deprecated()
        function read(self)

        @deprecation.deprecated()
        function write(self)