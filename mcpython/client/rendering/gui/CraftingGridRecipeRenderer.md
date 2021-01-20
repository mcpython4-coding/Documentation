***CraftingGridRecipeRenderer.py - documentation - last updated on 20.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
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