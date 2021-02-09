***Inventory.py - documentation - last updated on 9.2.2021 by uuk***
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
    - add option to store under an special directory the data and output the binary data


    @shared.registry class Inventory extends mcpython.common.world.serializer.IDataSerializer.IDataSerializer
        
        Inventory serializer class
        todo: add part fixers


        variable PART

        static
        function load(
                cls,
                save_file,
                inventory: mcpython.client.gui.ContainerRenderer.ContainerRenderer,
                path: str,
                file=None,
                ):
            
            :param save_file: the save file instance
            :param inventory: The inventory to save
            :param path: the path to save under
            :param file: the file to save into


                variable file

            variable data

            variable data

            variable inventory.uuid

            variable status

        static
        function save(
                cls,
                data,
                save_file,
                inventory: mcpython.client.gui.ContainerRenderer.ContainerRenderer,
                path: str,
                file=None,
                override=False,
                ):

                variable file

            variable data

                variable data

            variable idata

            variable data[path]