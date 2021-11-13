***InventoryRecipeView.py - documentation - last updated on 13.11.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class InventorySingleRecipeView extends  mcpython.client.gui.ContainerRenderer.ContainerRenderer 
        
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

    class InventoryMultiRecipeView extends mcpython.client.gui.ContainerRenderer.ContainerRenderer
        
        Inventory class for multi inventory recipe view
        todo: add custom name attribute setter from renderer if needed


        function __init__(self)

            variable self.page

            variable self.recipes_per_page

        function add_recipe_renderer(
                self,
                renderer: mcpython.client.rendering.gui.RecipeViewRenderer.AbstractRecipeViewRenderer,
                ):

        function on_activate(self)

        function draw(self, hovering_slot=None)

            variable width

            variable height

            variable self.bg_image_size

        function get_interaction_slots(self)

        function tick(self, dt: float)