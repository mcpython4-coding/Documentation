***RecipeGenerator.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class ICraftingKeyEncoder extends ABC
        
        base class for an encoder for an crafting field


        static
        function valid(cls, data) -> bool

        static
        function encode(cls, data, generator)

    class ItemStackEncoder extends ICraftingKeyEncoder
        
        encodes an ItemStack-instance
        WARNING: in normal mode, ItemStacks can NOT be used as they are based on the item-registry which is not yet
            filled with data


        static
        function valid(cls, data) -> bool

        static
        function encode(cls, data: ItemStack, generator: DataGeneratorInstance)

    class TagEncoder extends ICraftingKeyEncoder
        
        encodes an string-tag like "#minecraft:logs"


        static
        function valid(cls, data) -> bool

        static
        function encode(cls, data: str, generator)

    class StringTypedItem extends ICraftingKeyEncoder
        
        encodes an raw item name


        static
        function valid(cls, data) -> bool

        static
        function encode(cls, data, generator)

    class MixedTypeList extends ICraftingKeyEncoder
        
        encodes an list of key encode-ables


        static
        function valid(cls, data) -> bool

        static
        function encode(cls, data: list, generator)

    variable CRAFTING_ENCODERS

    function encode_data(data, generator: DataGeneratorInstance)
        
        encodes data together with the configuration to use
        :param data: the data to encode
        :param generator: the config to use
        :return: encoded data for later dumping in data gen


    variable INDICATOR_LIST

    class ShapedRecipeGenerator extends IDataGenerator
        
        Generator for an shaped recipe


        function __init__(self, name: str)

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

        function dump(self, generator: "DataGeneratorInstance")

            variable pattern

            variable sx

            variable sy

                variable p

            variable table

                variable table[INDICATOR_LIST[i]]

            variable data

                variable data["group"]

        function get_default_location(self, generator: "DataGeneratorInstance", name: str)

    class ShapelessGenerator extends IDataGenerator

        function __init__(self, name: str, config)

            variable self.name

            variable self.inputs

            variable self.output

            variable self.group

        function setGroup(self, name: str)

        function setOutput(self, stack: typing.Union[typing.Tuple[int, str], str])

        function addInput(self, identifier, count=1)

        function addInputs(self, *identifiers)

        function dump(self, generator: "DataGeneratorInstance")

        function get_default_location(self, generator: "DataGeneratorInstance", name: str)

    class SmeltingGenerator extends IDataGenerator

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

        function dump(self, generator: "DataGeneratorInstance")

        function get_default_location(self, generator: "DataGeneratorInstance", name: str)