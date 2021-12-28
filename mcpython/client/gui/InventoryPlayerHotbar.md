***InventoryPlayerHotbar.py - documentation - last updated on 28.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
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

            variable base: pyglet.image.AbstractImage

        function _get_tex_region(rx, ry, rex, rey)

        variable base1

        variable base2

        class Textures

            variable hearts

            variable armor

            variable hunger

            variable bar

            variable bar_size

            variable selection

            variable xp_bars

        variable TEXTURES

    class InventoryPlayerHotbar extends mcpython.client.gui.ContainerRenderer.ContainerRenderer
        
        main inventory for the hotbar


        variable INSTANCES: typing.List["InventoryPlayerHotbar"]

        static
        function create(cls, player)

        function __init__(self, player)

            variable self.player

            variable self.lable

            variable self.last_index

            variable self.last_item

            variable self.time_since_last_change

            variable self.xp_level_lable

        function free(self)

        static
        function get_config_file()

        function is_blocking_interactions(self) -> bool

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