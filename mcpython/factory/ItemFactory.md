***ItemFactory.py - documentation - last updated on 7.7.2020 by uuk***
___

    class ItemFactory

        variable TASKS

        static
        function process(cls)

        function __init__(self, name=None)

            variable self.set_name_finises_previous

            variable self.name

            variable self.modname

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

            variable self.template

        function __call__(self, name: str = None)

        function setTemplate(self, set_name_finises_previous=False)
            
            sets the current status as "template". This status will be set to on every .finish() call, but will not affect
            the new generated entry.


        function setToTemplate(self)

        function resetTemplate(self)

        function finish(self, register=True, task_list=False)

            variable copied

        function copy(self)

        @deprecation.deprecated("dev1-2", "a1.2.0")
        function _finish(self, register)

        function finish_up(self, register=False)
            
            will finish up the creation
            :param register: if the result should be registered to the registry
            todo: clean up this mess!!!!!


            variable master

                variable self.name

            class BaseClass extends object

                variable self.itemfile

                variable self.blockname

                class BaseClass extends BaseClass,  cls

            class ConstructedItem extends BaseClass

                variable NAME

                variable HAS_BLOCK

                static
                function get_default_item_image_location() -> str: return master.itemfile
                        
                        def get_active_image_location(self): return master.itemfile
                        
                        def __init__(self):

                function get_active_image_location(self): return master.itemfile
                        
                        def __init__(self):

                function __init__(self)

                variable STACK_SIZE

                function on_player_interact(self, player, block, button, modifiers) -> bool

                function on_set_from_item(self, block)

                class ConstructedItem extends ConstructedItem

                    function on_eat(self)
                        
                        called when the player eats the item
                        :return: if the item was eaten or not


                    variable HUNGER_ADDITION

                class ConstructedItem extends ConstructedItem

                    variable TOOL_LEVEL

                    variable TOOL_TYPE

                    function get_speed_multiplyer(self, itemstack)

                class ConstructedItem extends ConstructedItem

                    variable DEFENSE_POINTS

                class ConstructedItem extends ConstructedItem

                    variable FUEL

        function setBaseClass(self, baseclass):   # overwrites all previous base classes and replace them with the new(s)
                self.baseclass = baseclass if type(baseclass) == list else [baseclass]
                return self
                
                def setBaseClassByName(self, baseclassname: str):

        function setBaseClassByName(self, baseclassname: str)

        function setGlobalModName(self, name: str)

        function setName(self, name: str)

        function setDefaultItemFile(self, itemfile: str)

        function setHasBlockFlag(self, hasblock: bool)

        function setBlockName(self, blockname: str)

        function setUsedItemTextures(self, itemtextures: list)

        function setMaxStackSize(self, stacksize: int)

        function setCreationCallback(self, function)

        function setInteractionCallback(self, function)

        function setFoodValue(self, value: int)

        function setEatCallback(self, function)

        function setToolLevel(self, level: int)

        function setToolType(self, tooltype: list)

        function setToolBrakeMutli(self, multi: float)

        function setToolBrakeMultiCallback(self, function)

        function setArmorPoints(self, points: int)

        function setCustomFromItemFunction(self, function)

        function setFuelLevel(self, level)