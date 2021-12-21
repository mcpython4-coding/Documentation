***FurnaceCraftingHelper.py - documentation - last updated on 20.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.crafting_handler class FurnaceRecipe extends mcpython.common.container.crafting.IRecipe.IRecipe
        
        Interface for decoding an furnace-like recipe


        variable CRAFTING_SUPPORT

        variable RECIPE_TYPE_NAMES
            The list of type descriptors to decode

        static
        function from_data(cls, data: dict, file: str) -> "FurnaceRecipe"
            
            Loader function for an furnace crafting recipe
            :param data: the data to load
            :param file: the file loaded from
            :return: the recipe instance created


        function __init__(self, t, i, o, xp, time)

            variable self.input

            variable self.output

            variable self.xp

            variable self.time

            variable self.type