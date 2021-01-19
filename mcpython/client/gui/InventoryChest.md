***InventoryChest.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class InventoryChest extends mcpython.client.gui.Inventory.Inventory
        
        inventory class for chest


        variable TEXTURE

        variable TEXTURE_SIZE

        static
        function update_texture(cls)

        static
        function get_config_file() -> str or None

        function on_activate(self)

        function on_deactivate(self)

        function create_slots(self) -> list

        function draw(self, hovering_slot=None)

        function get_interaction_slots(self)

        function on_key_press(self, symbol, modifiers)

        function update_shift_container(self)