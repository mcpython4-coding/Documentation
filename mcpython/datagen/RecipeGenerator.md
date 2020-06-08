***RecipeGenerator.py - documentation - last updated on 8.6.2020 by uuk***
___

    class ICraftingKeyEncoder

        static
        function encode(cls, data): raise NotImplementedError()
                
                
                class ItemStackEncoder(ICraftingKeyEncoder):

    class ItemStackEncoder extends ICraftingKeyEncoder

        static
        function valid(cls, data) -> bool

        static
        function encode(cls, data: mcpython.gui.ItemStack.ItemStack)

    class TagEncoder extends ICraftingKeyEncoder

        static
        function valid(cls, data) -> bool

        static
        function encode(cls, data: str)

    class StringTypedItem extends ICraftingKeyEncoder

        static
        function valid(cls, data) -> bool

        static
        function encode(cls, data)

    class MixedTypeList extends ICraftingKeyEncoder

        static
        function valid(cls, data) -> bool

        static
        function encode(cls, data: list)

    variable CRAFTING_ENCODERS

    function encode_data(data)

    variable INDICATOR_LIST

    class ShapedRecipeGenerator extends mcpython.datagen.Configuration.IDataGenerator

        function __init__(self, name: str, config)

            variable self.grid

            variable self.types

            variable self.output

            variable self.group

            variable self.name

        function setGroup(self, name: str)

        function setEntry(self, x: int, y: int, data)
            
            will insert data into the grid
            :param x: the x position
            :param y: the y position
            :param data: the data to use, may be ItemStack, ItemStack-Tag-list, tag


        function setEntries(self, positions, data)

        function setOutput(self, stack: typing.Union[typing.Tuple[int, str], str])

        function generate(self)

            variable pattern

            variable sx

            variable sy

                variable p

            variable table

                variable table[INDICATOR_LIST[i]]

            variable data

                variable data["group"]

    class ShapelessGenerator extends mcpython.datagen.Configuration.IDataGenerator

        function __init__(self, name: str, config)

            variable self.name

            variable self.inputs

            variable self.output

            variable self.group

        function setGroup(self, name: str)

        function setOutput(self, stack: typing.Union[typing.Tuple[int, str], str])

        function addInput(self, identifier, count=1)

        function addInputs(self, *identifiers)

        function generate(self)

    class SmeltingGenerator extends mcpython.datagen.Configuration.IDataGenerator

        function __init__(self, name: str, config, mode="minecraft:smelting")

            variable self.name

            variable self.group

            variable self.output

            variable self.xp

            variable self.cooking_time

            variable self.inputs

            variable self.mode

        function setGroup(self, name: str)

        function add_ingredient(self, data)

        function add_ingredients(self, *data)

        function setOutput(self, stack: str)

        function setXp(self, xp: int)

        function setCookingTime(self, dt: int)

        function generate(self)