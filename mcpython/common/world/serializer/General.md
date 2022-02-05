***General.py - documentation - last updated on 5.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.registry class General extends mcpython.common.world.serializer.IDataSerializer.IDataSerializer

        variable PART

            variable read_buffer: ReadBuffer

            variable save_file.version

            variable player_name

            variable mods

            variable chunks_to_generate

            variable shared.world.config

            variable dimensions

            variable current_dimension

            variable target_buffer