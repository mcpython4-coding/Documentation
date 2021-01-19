***ItemFactory.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class ItemFactory extends mcpython.common.factory.IFactoryModifier.IFactory

        variable FACTORY_MODIFIERS

        variable TASKS

        static
        function process(cls)

        function __init__(self, name=None)

            variable self.set_name_finises_previous

            variable self.name

            variable self.modname

            variable self.item_file

            variable self.used_item_files

            variable self.has_block

            variable self.blockname

            variable self.max_stack_size

            variable self.creation_callback

            variable self.interaction_callback

            variable self.custom_from_item_function

            variable self.hungerregen
                food related stuff

            variable self.eat_callback

            variable self.base_classes

            variable self.tool_level

            variable self.tool_type

            variable self.tool_speed_multi

            variable self.tool_speed_callback

            variable self.durability

            variable self.armor_points

            variable self.fuel_level

            variable self.template

            variable self.tooltip_renderer

            variable self.tooltip_extra

            variable self.tooltip_color

        function __call__(self, name: str = None)

        function setTemplate(self, set_name_finises_previous=False)
            
            sets the current status as "template". This status will be set to on every .finish() call, but will not affect
            the new generated entry.


        function setToTemplate(self)

        function resetTemplate(self)

        function finish(self, register=True, task_list=False)

            variable copied

        function copy(self)

        function finish_up(self, register=False)
            
            will finish up the creation
            :param register: if the result should be registered to the registry
            todo: clean up this mess!!!!!


            variable master

                variable self.name

            class BaseClass extends object

                variable self.item_file

                variable self.blockname

                class BaseClass extends BaseClass,  cls

            class ConstructedItem extends  BaseClass 

                static
                function get_used_texture_files(cls)

                variable NAME

                variable HAS_BLOCK

                variable ITEM_NAME_COLOR

                variable DURABILITY

                function get_block(self) -> str

                static
                function get_default_item_image_location() -> str

                function get_active_image_location(self)

                function __init__(self)

                variable STACK_SIZE

                function on_player_interact(self, player, block, button, modifiers) -> bool

                function on_set_from_item(self, block)

                class ConstructedItem extends  ConstructedItem 

                    function on_eat(self)
                        
                        called when the player eats the item
                        :return: if the item was eaten or not


                    variable HUNGER_ADDITION

                class ConstructedItem extends  ConstructedItem 

                    variable TOOL_LEVEL

                    variable TOOL_TYPE

                    function get_speed_multiplyer(self, itemstack)

                class ConstructedItem extends ConstructedItem

                    variable DEFENSE_POINTS

                class ConstructedItem extends ConstructedItem

                    variable FUEL

                class ConstructedItem extends ConstructedItem

                    static
                    function get_tooltip_provider(cls)

                class ConstructedItem extends ConstructedItem

                    static
                    function getAdditionalTooltipText(cls, *_) -> list

                    variable ConstructedItem

        function setBaseClass(
                self, baseclass
                ):  # overwrites all previous base classes and replace them with the new(s)
                self.base_classes = baseclass if type(baseclass) == list else [baseclass]
                return self
                
                def setBaseClassByName(self, baseclassname: str):

            variable self.base_classes

        function setBaseClassByName(self, baseclassname: str)

        function setGlobalModName(self, name: str)

        function setName(self, name: str)

        function setDefaultItemFile(self, itemfile: str)

        function setHasBlockFlag(self, hasblock: bool)

        function setBlockName(self, blockname: str)

        function setUsedItemTextures(self, textures: list)

        function setMaxStackSize(self, size: int)

        function setCreationCallback(self, function)

        function setInteractionCallback(self, function)

        function setFoodValue(self, value: int)

        function setEatCallback(self, function)

        function setToolLevel(self, level: int)

        function setToolType(
                self,
                tool_types: typing.List[mcpython.common.item.AbstractToolItem.AbstractToolItem],
                ):

            variable self.tool_type

        function setToolBrakeMulti(self, multi: float)

        function setToolBrakeMultiCallback(self, function)

        function set_durability(self, durability: int)

        function setArmorPoints(self, points: int)

        function set_damage_able(self, durability: int)

        function setCustomFromItemFunction(self, function)

        function setFuelLevel(self, level)

        function setToolTipRenderer(self, renderer)

        function setTooltipExtraLines(self, lines)

        function setToolTipItemNameColor(self, color_name: str)