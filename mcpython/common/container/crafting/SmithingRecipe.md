***SmithingRecipe.py - documentation - last updated on 18.11.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.crafting_handler class SmithingRecipe extends mcpython.common.container.crafting.IRecipe.IRecipe

        variable RECIPE_TYPE_NAMES
            todo: implement
            The list of type descriptors to decode

        variable CRAFTING_SUPPORT

        static
        function from_data(cls, data: dict, file: str) -> "SmithingRecipe"

        function __init__(self)