***IRecipe.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class IRecipe extends mcpython.common.event.Registry.IRegistryContent,  ABC
        
        Base class for recipes
        Data is matched by TYPE, than decoded by from_data() ['file' is for error messages]
        Later run the loading pipe, bake() is called
        After all that, prepare() is called. This should create the needed lookups for the crafting systems
        [e.g. maps from input -> output, ...]


        variable TYPE

        variable RECIPE_TYPE_NAMES

        variable RECIPE_VIEW

        static
        function from_data(cls, data: dict, file: str)

        function __init__(self)

            variable self.name

        function get_inputs(self) -> typing.Iterable[ItemStack]

        function get_outputs(self) -> typing.Iterable[ItemStack]

        function bake(self)

        function prepare(self)