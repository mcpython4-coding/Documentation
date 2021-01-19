***Inventory.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
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
                inventory: mcpython.client.gui.Inventory.Inventory,
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
                inventory: mcpython.client.gui.Inventory.Inventory,
                path: str,
                file=None,
                override=False,
                ):

                variable file

            variable data

                variable data

            variable idata

            variable data[path]