***ItemFactory.py - documentation - last updated on 2.5.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable ItemFactoryInstance

    function set_food_value(factory, value: int)

    function set_default_item_file(factory, file)

    function set_eat_callback(instance, callback)

    function set_durability(instance, value)

    function set_tool_type(instance, *value)

    function set_armor_points(instance, points: int)

    function build_class(
            cls: typing.Type[mcpython.common.item.AbstractItem.AbstractItem],
            instance: FactoryBuilder.IFactory,
            ):

        variable configs: dict

        variable name

            variable name

            variable configs["default_item_file"]

        class ModifiedClass extends cls

            variable NAME

            variable STACK_SIZE

            variable HUNGER_ADDITION

            variable HAS_BLOCK

                variable FUEL

            static
            function get_used_texture_files(
                    cls,
                    ):

            static
            function get_default_item_image_location() -> str

            function get_active_image_location(self)

            function get_tooltip_provider(self)

                function on_eat(self)

                variable DURABILITY

                variable TOOL_TYPE

                variable TOOL_LEVEL

                function get_speed_multiplyer(self, itemstack)

                variable DEFENSE_POINTS

            function on_set_from_item(self, block)

    variable ItemFactory