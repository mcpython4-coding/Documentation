***FurnaceCrafting.py - documentation - last updated on 20.7.2020 by uuk***
___

    @G.craftinghandler class FurnaceRecipe extends mcpython.gui.crafting.IRecipeType.IRecipe
        
        Interface for decoding an furnace-like recipe


        variable RECIPE_NAMES
            The list of type descriptors to decode

        static
        function get_recipe_names(cls) -> list: return cls.RECIPE_NAMES
                
                @classmethod
                def from_data(cls, data: dict) -> "FurnaceRecipe":

        static
        function from_data(cls, data: dict) -> "FurnaceRecipe"
            
            Loader function for an furnace crafting recipe
            :param data: the data to load
            :return: the recipe instance created


        function __init__(self, t, i, o, xp, time)

            variable self.input

            variable self.output

            variable self.xp

            variable self.time

            variable self.type

        function register(self)

    variable FurnesRecipe - todo: remove in a1.4.0