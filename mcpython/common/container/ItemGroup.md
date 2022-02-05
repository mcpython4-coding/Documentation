***ItemGroup.py - documentation - last updated on 5.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ItemGroup extends IBufferSerializeAble

        variable __slots__

        function __init__(self)

            variable self.entries: typing.List[ItemStack]

            variable self.has_lazy

            variable self.entries

        function add(self, entry: typing.Union[ItemStack, str])

                variable self.has_lazy

        function load_lazy(self)

            variable has

                        variable has

            variable self.has_lazy

        function sort_after_item_name(self)

        function view(self) -> typing.Iterator[ItemStack]

        function filter_for(self, pattern: re.Pattern) -> typing.Iterator[ItemStack]

        function filtered(self)

    class FilteredItemGroup extends ItemGroup

        variable __slots__

        function __init__(self)

            variable self.raw_filter: str

            variable self.filter: re.Pattern

        function view(self) -> typing.Iterator[ItemStack]

        function apply_raw_filter(self, filter_code: str)

        function apply_filter(self, filter_pattern: re.Pattern)