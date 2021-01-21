***FurnaceCraftingHelper.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    @shared.crafting_handler class FurnaceRecipe extends mcpython.common.container.crafting.IRecipe.IRecipe
        
        Interface for decoding an furnace-like recipe


        variable RECIPE_NAMES
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

        function register(self)