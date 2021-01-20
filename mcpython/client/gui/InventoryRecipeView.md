***InventoryRecipeView.py - documentation - last updated on 20.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class InventorySingleRecipeView extends mcpython.client.gui.Inventory.Inventory
        
        Inventory class for single inventory recipe view
        todo: add custom name attribute setter from renderer if needed


        function __init__(self)

        function set_renderer(
                self,
                renderer: mcpython.client.rendering.gui.RecipeViewRenderer.AbstractRecipeViewRenderer,
                ):

            variable self.renderer

        function on_activate(self)

        function draw(self, hovering_slot=None)

        function get_interaction_slots(self)

        function tick(self, dt: float)