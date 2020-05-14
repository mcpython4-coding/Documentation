***GridRecipeInterface.py - documentation - last updated on 14.5.2020 by uuk***
___

    class GridRecipeInterface extends crafting.IRecipeInterface.IRecipeInterface

        variable NAME

            
            creates an new grid recipe interface
            recipe order: first in, first checked
            :param slot_input_map: an Slot[[ for input
            :param slot_output_map: an Slot for output
            :param maxsize: the max size for recipes. may be None for full grid size
            :param minsize: the min size for recipes. default is (1, 1)
            :param enabled: if recipes should be craftable
            :param enable_shaped_recipes: if shaped recipes should be enabled
            :param enable_shapeless_recipes: if shapeless recipes should be enabled
            

        function check_recipe_state(self)
        static function _minimize_slotmap(slotmap: dict) -> dict
        static function _check_shaped(recipe: crafting.GridRecipes.GridShaped, itemtable: dict) -> bool
        static function _check_shapeless(recipe: crafting.GridRecipes.GridShapeless, items: list) -> bool
        function update_output(self)
        function remove_input(self, count=1)
        function on_input_update(self, player=False)
        function on_output_update(self, player=False)
        function on_output_shift_click(self, slot, x, y, button, modifiers)