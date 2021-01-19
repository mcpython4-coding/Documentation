***InventoryPlayerHotbar.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class _TEXTURES

        variable hearts

        variable armor

        variable hunger

        variable bar

        variable bar_size

        variable selection

        variable xp_bars

    variable TEXTURES

    function reload()

        function _get_tex_region(rx, ry, rex, rey)

        class Textures

            variable hearts

            variable armor

            variable hunger

            variable base

            variable bar

            variable bar_size

            variable selection

            variable base

            variable xp_bars

        variable TEXTURES

    class InventoryPlayerHotbar extends mcpython.client.gui.Inventory.Inventory
        
        main inventory for the hotbar


        function __init__(self, player)

            variable self.player

            variable self.lable

            variable self.last_index

            variable self.last_item

            variable self.time_since_last_change

            variable self.xp_level_lable

        static
        function get_config_file()

        function is_blocking_interactions(self) -> bool

        function create_slots(self) -> list

        function on_activate(self)

        function on_deactivate(self)

        function draw(self, hovering_slot=None)

                variable self.time_since_last_change

                variable self.last_index

                variable self.last_item

                variable self.lable.text

                variable self.lable.x

                variable self.lable.y

        function draw_hearts(self, hx, hy)

        function draw_hunger(self, hx, hy)

        function draw_xp_level(self, hx, hy)

        function draw_armor(self, hx, hy)

        function is_closable_by_escape(self) -> bool

        function is_always_open(self) -> bool