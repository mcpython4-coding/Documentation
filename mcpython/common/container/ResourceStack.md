***ResourceStack.py - documentation - last updated on 19.5.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractResourceStack extends ABC
        
        Abstract class for stack like objects


        static
        function create_empty(cls)

        function copy(self) -> "AbstractResourceStack"

        function copy_from(self, other: "AbstractResourceStack")

        function clean(self)

        function is_empty(self) -> bool

        function contains_same_resource(self, other: "AbstractResourceStack") -> bool

        function has_more_than(self, other: "AbstractResourceStack") -> bool

        function get_difference(self, other: "AbstractResourceStack") -> "AbstractResourceStack"

    class ItemStack extends AbstractResourceStack
        
        Default implementation for item stacks


        static
        function create_empty(cls)
            
            Get an empty itemstack


        function __init__(self, item_name_or_instance=None, amount=1, warn_if_unarrival=True)

                    variable self.item

                    variable self.item

                variable self.item

            variable self.amount

        function copy(self) -> "ItemStack"
            
            Copies the itemstack
            :return: copy of this itemstack


        function copy_from(self, other: "ItemStack")

        function clean(self)
            
            "Clean" the itemstack so that there is no data inside


        function __eq__(self, other)

        function is_empty(self) -> bool

        function get_item_name(self) -> typing.Optional[str]

        function set_amount(self, amount: int) -> "ItemStack"

        function add_amount(self, amount: int, check_overflow=True) -> "ItemStack"

        function __str__(self) -> str

        function __repr__(self)

        function contains_same_resource(self, other: "AbstractResourceStack") -> bool

        function has_more_than(self, other: "AbstractResourceStack") -> bool

        function get_difference(self, other: "AbstractResourceStack") -> "AbstractResourceStack"

    class LazyClassLoadItemstack extends ItemStack

        function __init__(self, item_name: str, amount=1)

            variable self.lazy_amount

            variable self.lazy_item_name

        function lookup(self)

        function __repr__(self)

    class FluidStack extends AbstractResourceStack

        static
        function create_empty(cls)

        function __init__(self, fluid: typing.Optional[str], amount: float = 0)

            variable self.fluid

            variable self.amount

        function copy(self) -> "AbstractResourceStack"

        function copy_from(self, other: "FluidStack")

        function clean(self)

        function is_empty(self) -> bool

        function contains_same_resource(self, other: "AbstractResourceStack") -> bool

        function has_more_than(self, other: "AbstractResourceStack") -> bool

        function get_difference(self, other: "AbstractResourceStack") -> "AbstractResourceStack"