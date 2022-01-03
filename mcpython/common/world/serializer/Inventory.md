***Inventory.py - documentation - last updated on 3.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    improvements for the future:
    - make the whole serializer an network buffer and store at head an offset table


    @shared.registry class Inventory extends mcpython.common.world.serializer.IDataSerializer.IDataSerializer
        
        Inventory serializer class
        todo: add part fixers


        variable PART
            
            :param save_file: the save file instance
            :param inventory: The inventory to save
            :param path: the path to save under
            :param file: the file to save into


                variable file

            variable data: ReadBuffer

                variable data: bytes

            variable buffer

                variable file

            variable data: ReadBuffer

                variable table

                variable table

            variable buffer

            variable write