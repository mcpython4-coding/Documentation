***Blocks.py - documentation - last updated on 16.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    Missing:
    air
    attached_melon_stem
    attached_pumpkin_stem


    variable DEFERRED_PIPE: DeferredRegistry

    function plant(name: str)

    function large_plant(name: str)

    function wood(name: str, normal=True)

    function stone_like(
            name: str,
            existing_full=True,
            existing_slab=True,
            existing_wall=True,
            existing_stairs=True,
            existing_fence=False,
            existing_button=False,
            existing_pressure_plate=False,
            texture=None,
            consumer=lambda _, __: None,
            ):

        variable fname

        variable instance

            variable obj

            variable obj

            variable obj

            variable obj

            variable obj

    function colored(name: str)