***InventoryPlayerHotbar.py - documentation - last updated on 14.5.2020 by uuk***
___

    variable base: pyglet.image.AbstractImage

    function _get_tex_region(rx, ry, rex, rey)

    class TEXTURES

        variable hearts

        variable armor

        variable hunger

    class InventoryPlayerHotbar extends gui.Inventory.Inventory
        
        main inventory for the hotbar


        function __init__(self)

                variable self.selected_sprite

            variable self.lable

            variable self.last_index

            variable self.last_item

            variable self.time_since_last_change

            variable self.xp_level_lable

        function get_select_sprite(self)

            variable self.selected_sprite

        static function get_config_file()

        function is_blocking_interactions(self) -> bool

        function create_slots(self) -> list

        function on_activate(self)

        function on_deactivate(self)

        function draw(self, hoveringslot=None)

                variable self.bgsprite.position

        function on_draw_over_image(self)

            variable slot

            variable self.selected_sprite.position

            variable selected_slot

                variable self.time_since_last_change

                variable self.last_index

                variable self.last_item

                variable self.lable.text

                variable self.lable.x

                variable self.lable.y

        function draw_hearts(self, hx, hy)

            variable x

            variable y

            variable hearts

        function draw_hunger(self, hx, hy)

            variable x

            variable y

            variable hunger

        function draw_xp_level(self, hx, hy)

            variable x

            variable y

            variable active_progress

                variable self.lable.x

                variable self.lable.y

                variable self.lable.text

        function draw_armor(self, hx, hy)

            variable x

            variable y

            variable armor

        function is_closable_by_escape(self) -> bool

        function is_always_open(self) -> bool