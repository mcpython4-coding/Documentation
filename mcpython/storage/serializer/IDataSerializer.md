***IDataSerializer.py - documentation - last updated on 26.7.2020 by uuk***
___

    class InvalidSaveException extends Exception

    class MissingSaveException extends Exception

    class IDataSerializer extends mcpython.event.Registry.IRegistryContent
        
        Serializer class for any stuff saved in the game files.
        Used for accessing the data and loading it into an way that the game can understand it.


        variable TYPE

        variable PART - which part it can serialize

        static
        function load(cls, savefile, **kwargs)
            
            Loads stuff into the game
            :param savefile: the SaveFile object to use
            :param kwargs: the configuration


        static
        function save(cls, data, savefile, **kwargs)
            
            Saves data into the storage file
            :param data: the data to save
            :param savefile: the SaveFile object to save
            :param kwargs: the configuration


        static
        function apply_part_fixer(cls, savefile, fixer)
            
            Handler function for applying PartFixer instances into the given system
            :param savefile: the SaveFile used
            :param fixer: the fixer instance


    variable dataserializerregistry

    @G.modloader("minecraft", "stage:serializer:parts")
    function load()