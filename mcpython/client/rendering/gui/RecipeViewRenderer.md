***RecipeViewRenderer.py - documentation - last updated on 13.11.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class NotEnoughItemsException extends Exception

    class AbstractRecipeViewRenderer extends ABC
        
        Renderer system for displaying a recipe to the player in a JEI-like style


        function copy(self)

        function prepare_for_recipe(
                self, recipe: mcpython.common.container.crafting.IRecipe.IRecipe
                ):

        function draw(self, position: typing.Tuple[int, int], hovering_slot=None)

        function add_to_batch(
                self, position: typing.Tuple[int, int], batch: pyglet.graphics.Batch
                ):

        function get_rendering_size(self) -> typing.Tuple[int, int]

        function copy_into(self, helper, *itemstacks, creative=False)

        function get_slots(self)

        function tick(self, dt: float)