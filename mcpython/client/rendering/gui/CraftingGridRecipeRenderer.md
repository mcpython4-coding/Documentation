***CraftingGridRecipeRenderer.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class CraftingTableLikeRecipeViewRenderer extends  RecipeViewRenderer.AbstractRecipeViewRenderer 

        variable TEXTURE: typing.Optional[pyglet.image.AbstractImage]

        static
        function update_texture(cls)

            variable size

            variable texture

            variable size

            variable texture

            variable cls.TEXTURE

            variable cls.TEXTURE_SIZE

        function __init__(self)

            variable self.recipe

            variable self.slots

            variable i

                    variable self.slots[i].position

            variable self.slots[-1].position

            variable self.mutation_iterator

            variable self.grid

            variable self.enable_shapeless_symbol

            variable self.remaining_state_time

        function prepare_for_recipe(
                self, recipe: mcpython.common.container.crafting.IRecipe.IRecipe
                ):

            variable self.recipe

                variable i

        function clear(self)

        function draw(self, position: typing.Tuple[int, int], hovering_slot=None)

        function add_to_batch(
                self, position: typing.Tuple[int, int], batch: pyglet.graphics.Batch
                ):

        function get_rendering_size(self) -> typing.Tuple[int, int]

        function get_slots(self)

        function tick(self, dt: float)