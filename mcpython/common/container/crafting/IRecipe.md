***IRecipe.py - documentation - last updated on 20.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class IRecipe extends mcpython.common.event.api.IRegistryContent,  ABC
        
        Base class for recipes
        Data is matched by TYPE, than decoded by from_data() ['file' is for error messages]
        Later run the loading pipe, bake() is called
        After all that, prepare() is called. This should create the needed lookups for the crafting systems
        [e.g. maps from input -> output, ...]


        variable __slots__

        variable TYPE

        variable RECIPE_TYPE_NAMES

        variable RECIPE_VIEW

        variable CRAFTING_SUPPORT
            item names supporting crafting operations of this recipe

        static
        function from_data(cls, data: dict, file: str)

        function __init__(self)

            variable self.name

        function get_inputs(self) -> typing.Iterable[ItemStack]

        function get_outputs(self) -> typing.Iterable[ItemStack]