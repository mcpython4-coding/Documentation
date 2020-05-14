***ItemFactory.py - documentation - last updated on 14.5.2020 by uuk***
___

    class ItemFactory

        variable TASKS

        static function process(cls)

        function __init__(self)

            variable self.name

            variable self.itemfile

            variable self.used_itemfiles

            variable self.has_block

            variable self.blockname

            variable self.stacksize

            variable self.creation_callback

            variable self.interaction_callback

            variable self.customfromitemfunction

            variable self.hungerregen
                food related stuff

            variable self.eat_callback

            variable self.baseclass

            variable self.tool_level

            variable self.tool_type

            variable self.tool_speed_multi

            variable self.tool_speed_callback

            variable self.armor_points

            variable self.fuel_level

        function finish(self, register=True, task_list=False)

        function _finish(self, register)

            variable master

            class baseclass extends object

                variable self.itemfile

                variable self.blockname

                class baseclass extends baseclass,  cls

            class ConstructedItem extends baseclass

                static function get_used_texture_files(cls)

                variable NAME

                variable HAS_BLOCK

                function get_block(self) -> str

                static function get_default_item_image_location() -> str

                function get_active_image_location(self)

                function __init__(self)

                variable STACK_SIZE

                function on_player_interact(self, player, block, button, modifiers) -> bool

                function on_set_from_item(self, block)

                class ConstructedItem extends ConstructedItem

                    function on_eat(self)
                        
                        called when the player eats the item
                        :return: if the item was eaten or not


                        variable G.world.get_active_player().hunger

                    variable HUNGER_ADDITION

                class ConstructedItem extends ConstructedItem

                    variable TOOL_LEVEL

                    variable TOOL_TYPE

                    function get_speed_multiplyer(self, itemstack)

                class ConstructedItem extends ConstructedItem

                    variable DEFENSE_POINTS

                class ConstructedItem extends ConstructedItem

                    variable FUEL

        function setBaseClass(self, baseclass)

            variable self.baseclass

        function setBaseClassByName(self, baseclassname: str)

        function setName(self, name: str)

            variable self.name

        function setDefaultItemFile(self, itemfile: str)

            variable self.itemfile

        function setHasBlockFlag(self, hasblock: bool)

            variable self.has_block

        function setBlockName(self, blockname: str)

            variable self.blockname

        function setUsedItemTextures(self, itemtextures: list)

            variable self.used_itemfiles

                variable self.itemfile

        function setMaxStackSize(self, stacksize: int)

            variable self.stacksize

        function setCreationCallback(self, function)

            variable self.creation_callback

        function setInteractionCallback(self, function)

            variable self.interaction_callback

        function setFoodValue(self, value: int)

            variable self.hungerregen

        function setEatCallback(self, function)

            variable self.eat_callback

        function setToolLevel(self, level: int)

            variable self.tool_level

        function setToolType(self, tooltype: list)

            variable self.tool_type

        function setToolBrakeMutli(self, multi: float)

            variable self.tool_speed_multi

        function setToolBrakeMultiCallback(self, function)

            variable self.tool_speed_callback

        function setArmorPoints(self, points: int)

            variable self.armor_points

        function setCustomFromItemFunction(self, function)

            variable self.customfromitemfunction

        function setFuelLevel(self, level)

            variable self.fuel_level