***InventoryPlayerHotbar.py - documentation - last updated on 6.6.2020 by uuk***
___

    variable base: pyglet.image.AbstractImage

    function _get_tex_region(rx, ry, rex, rey)

    class TEXTURES

        variable hearts

        variable armor

        variable hunger

    class InventoryPlayerHotbar extends mcpython.gui.Inventory.Inventory
        
        main inventory for the hotbar


        function __init__(self)

            variable self.xp_level_lable

        function get_select_sprite(self)

        static
        function get_config_file()

        function is_blocking_interactions(self) -> bool

        function create_slots(self) -> list

        function on_activate(self)

        function on_deactivate(self)

        function draw(self, hoveringslot=None)

        function on_draw_over_image(self)

            variable selected_slot

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

        function is_closable_by_escape(self) -> bool: return False
                
                def is_always_open(self) -> bool: return True
                
                

        function is_always_open(self) -> bool: return True
                
                