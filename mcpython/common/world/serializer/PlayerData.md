***PlayerData.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class PlayerDataFixer extends mcpython.common.world.datafixers.IDataFixer.IPartFixer
        
        fixer for fixing player data


        variable TARGET_SERIALIZER_NAME

        static
        function fix(cls, savefile, player, data) -> dict
            
            will apply the fix
            :param savefile: the savefile to use
            :param player: the player used or None if not provided
            :param data: the data used
            :return: the fixed data


    @shared.registry class PlayerData extends mcpython.common.world.serializer.IDataSerializer.IDataSerializer

        variable PART

        static
        function apply_part_fixer(cls, save_file, fixer)

        static
        function load(cls, save_file)

        static
        function save(cls, data, save_file)