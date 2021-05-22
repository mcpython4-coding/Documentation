***PlayerData.py - documentation - last updated on 22.5.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
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
        function load(cls, save_file, **_)

                    variable player.in_nether_portal_since

                variable player.should_leave_nether_portal_before_dim_change

        static
        function save(cls, data, save_file, **_)

                variable data[player.name]
                    todo: move to player custom save data