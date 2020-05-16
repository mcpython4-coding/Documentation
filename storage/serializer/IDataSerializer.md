***IDataSerializer.py - documentation - last updated on 16.5.2020 by uuk***
___

    class InvalidSaveException extends Exception

    class MissingSaveException extends Exception

    class IDataSerializer extends event.Registry.IRegistryContent

        variable TYPE

        variable PART - which part it can serialize

        static function load(cls, savefile, **kwargs)

        static function save(cls, data, savefile, **kwargs)

    variable dataserializerregistry

    function load()