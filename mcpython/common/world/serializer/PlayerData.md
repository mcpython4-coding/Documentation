***PlayerData.py - documentation - last updated on 16.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.registry class PlayerData extends mcpython.common.world.serializer.IDataSerializer.IDataSerializer

        variable PART

        static
        function load(cls, save_file, **_)

                    variable player

                    variable player

        static
        function load_player_data(cls, data, player, save_file)

            variable player.flying

                variable player.in_nether_portal_since

            variable player.should_leave_nether_portal_before_dim_change

        static
        function save(cls, data, save_file, **_)

                variable data[player.name]
                    todo: move to player custom save data