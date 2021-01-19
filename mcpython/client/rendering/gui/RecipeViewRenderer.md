***RecipeViewRenderer.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class NotEnoughItemsException extends Exception

    class AbstractRecipeViewRenderer extends ABC

        function prepare_for_recipe(
                self, recipe: mcpython.common.container.crafting.IRecipeType.IRecipe
                ):

        function draw(self, position: typing.Tuple[int, int], hovering_slot=None)

        function add_to_batch(
                self, position: typing.Tuple[int, int], batch: pyglet.graphics.Batch
                ):

        function get_rendering_size(self) -> typing.Tuple[int, int]

        function copy_into(self, helper, *itemstacks, creative=False)

        function get_slots(self)

        function tick(self, dt: float)