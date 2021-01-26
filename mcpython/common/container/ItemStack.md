***ItemStack.py - documentation - last updated on 26.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class AbstractItemStack extends ABC
        
        Abstract class for item stack like objects


        static
        function create_empty(cls)

        function copy(self) -> "AbstractItemStack"

        function copy_from(self, other: "AbstractItemStack")

        function clean(self)

        function is_empty(self) -> bool

    class ItemStack extends AbstractItemStack
        
        Default implementation for item stacks


        static
        function create_empty(cls)
            
            Get an empty itemstack


        function __init__(self, item_name_or_instance=None, amount=1)

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