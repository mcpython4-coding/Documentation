***IDataSerializer.py - documentation - last updated on 13.11.2021 by uuk***
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

    class IDataSerializer extends mcpython.common.event.api.IRegistryContent
        
        Serializer class for any stuff saved in the game files.
        Used for accessing the data and loading it into an way that the game can understand it.


        variable TYPE

        variable PART - which part it can serialize
            
            Loads stuff into the game
            :param save_file: the SaveFile object to use

            
            Saves data into the storage file
            :param data: the data to save
            :param save_file: the SaveFile object to save


    variable data_serializer_registry

    @shared.mod_loader("minecraft", "stage:serializer:parts")
    function load()