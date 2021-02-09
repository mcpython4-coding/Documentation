***IDataSerializer.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class InvalidSaveException extends Exception

    class MissingSaveException extends Exception

    class IDataSerializer extends mcpython.common.event.Registry.IRegistryContent
        
        Serializer class for any stuff saved in the game files.
        Used for accessing the data and loading it into an way that the game can understand it.


        variable TYPE

        variable PART - which part it can serialize

        static
        function load(cls, save_file, **kwargs)
            
            Loads stuff into the game
            :param save_file: the SaveFile object to use
            :param kwargs: the configuration


        static
        function save(cls, data, save_file, **kwargs)
            
            Saves data into the storage file
            :param data: the data to save
            :param save_file: the SaveFile object to save
            :param kwargs: the configuration


        static
        function apply_part_fixer(cls, save_file, fixer)
            
            Handler function for applying PartFixer instances into the given system
            :param save_file: the SaveFile used
            :param fixer: the fixer instance


    variable data_serializer_registry

    @shared.mod_loader("minecraft", "stage:serializer:parts")
    function load()