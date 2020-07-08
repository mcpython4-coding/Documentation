***IDataSerializer.py - documentation - last updated on 11.6.2020 by uuk***
___

    class InvalidSaveException extends Exception

    class MissingSaveException extends Exception

    class IDataSerializer extends mcpython.event.Registry.IRegistryContent

        variable TYPE

        variable PART - which part it can serialize

        static
        function load(cls, savefile, **kwargs)

        static
        function save(cls, data, savefile, **kwargs)

        static
        function apply_part_fixer(cls, savefile, fixer)

    variable dataserializerregistry

    function load()