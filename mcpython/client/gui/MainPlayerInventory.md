***MainPlayerInventory.py - documentation - last updated on 20.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class MainPlayerInventory extends mcpython.client.gui.Inventory.Inventory
        
        inventory class for the main part of the inventory


        variable TEXTURE

        variable TEXTURE_SIZE

        static
        function update_texture(cls)

        static
        function get_config_file() -> str or None

        function __init__(self, hotbar)

            variable self.hotbar

            variable inputs

            variable self.recipe_interface

        function create_slots(self) -> list

        function armor_update(self, player=None)

        function draw(self, hovering_slot=None)

        function remove_items_from_crafting(self)

        function on_deactivate(self)

        function update_shift_container(self)