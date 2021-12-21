***StonecuttingRecipe.py - documentation - last updated on 20.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.crafting_handler class StoneCuttingRecipe extends mcpython.common.container.crafting.IRecipe.IRecipe

        variable __slots__

        variable RECIPE_TYPE_NAMES
            The list of type descriptors to decode

        variable CRAFTING_SUPPORT

        static
        function from_data(cls, data: dict, file: str) -> "StoneCuttingRecipe"

        function __init__(self, ingredient: str, result: str, count: int = 1)

            variable self.ingredient

            variable self.result

            variable self.count