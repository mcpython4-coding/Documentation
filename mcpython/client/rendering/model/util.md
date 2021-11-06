***util.py - documentation - last updated on 14.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable UV_ORDER

    variable SIDE_ORDER

    variable UV_INDICES
        representative for the order of uv insertion

    function get_model_choice(data, instance)

    function decode_entry(data: typing.Dict[str, typing.Any])

    function calculate_default_layout_uvs(
            texture_size: typing.Tuple[int, int],
            box_size: typing.Tuple[int, int, int],
            offset: typing.Tuple[int, int],
            ):
        
        Util method for calculating uv's
        Cache result whenever possible!
        WARNING: currently may not work correctly
        :param texture_size: the size of the texture, a simple factor for the result
        :param box_size: the sizes of the box
        :param offset: an offset of the texture origin
        :return: the uv's, to pass to e.g. box models
