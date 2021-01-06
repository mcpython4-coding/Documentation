***BlockFactory.py - documentation - last updated on 29.7.2020 by uuk***
___

    class BlockFactory
        
        factory for creating on an simple way block classes
        examples:
            BlockFactory().set_name("test:block").set_hardness(1).set_blast_resistance(1).finish()
            BlockFactory().set_name("test:log").set_hardness(1).set_blast_resistance(1).set_log().finish()
            BlockFactory().set_name("test:slab").set_hardness(1).set_blast_resistance(1).set_slab().finish()
            BlockFactory().set_name("some:complex_block").set_hardness(1).set_blast_resistance(1).set_default_model_state("your=default,model=state").set_all_side_solid(False).finish()
        Most functions will return the BlockFactory-object called on to allow above syntax.
        .set_hardness and .set_blast_resistance should be set on ALL blocks created as they will be NOT optional in the future.
        The .finish() method will return the BlockItemFactory-instance for the block. Modifying it before the
            "stage:block:factory:finish"-phase will lead into changes in the base block. This can also lead into exceptions
            in this phase as their the data is read in and the classes are generated.
        for an long lists of examples, see Blocks.py; Be aware that it is using the template system described below.
        ---------------------------------
        Modifying existing BlockFactories
        ---------------------------------
        As mentioned above, using the instance and modifying it is not the ideal way of doing. You can go the "normal"
            route and replace the block-class in the registry. You can do this also over the BlockFactory route, but be
            aware that you have to register after the desired block and hope for the best. You can also, if you want to
            use BlockFactory-instances, use the on_class_create-event in the constructor of the BlockFactory-class and
            recycle your generated class afterwards.
        You can also call the finish()-method with immediate=True leading into an immediate class generation (may take
            some time).
        ---------------
        Template-system
        ---------------
        You are able to create BlockFactory templates (pre-configured BlockFactory objects from which you can create
            multiple blocks starting with the same foundation).
        You can store your config with .set_template() on an BlockFactory-object. It will store the active status
            for later usage. When you call .finish(), the block will be created and the system will reset to the state
            of your .set_template() call. You can manually reset it by calling .set_to_template() and you can delete
            the template by calling .reset_template(). You can disable the reset to the template on finish-call if you
            pass reset_to_template=False to it.
        If you are creating an block in multiple colors with the configuration, templates should be used as they reduce
            are better internally.
        Templates can be extracted/inserted as the .template-attribute.
        Template-attribute changes will NOT affect active build block, you must call set_to_template() first or finish your
            block
        Example:
            your_template = BlockFactory().[some calls].set_template()
            your_template.set_name("test:block").finish()  # will create an block called "test:block" with pre-configured parameters
            your_template.set_name("test:slab").set_slab().finish()  # will create an slab
            your_template.set_name("test:block2").finish()   # This is now NOT an slab beside it be based on the same base
        ---------------------
        Extending the Factory
        ---------------------
        Currently, the only way is to create an sub-class of BlockFactory and re-send it into the variable holding the
            class. It is planned to re-write the foundation of the system (and leaving most of the surface) and porting
            things to an really simple-extendable system. This will take some while and has not the highest priority
            (As it is an API-only improvement). If you miss any setter for an Block-class API attribute, create an
            issue for it and we will try to implement it (and it fit the general look of the API's)


        function __init__(self, on_class_create=None)
            
            will create an new BlockFactory-instance
            :param on_class_create: optional: an function taking the generated class and optional returning an new one to
                replace


            variable self.on_class_create

            variable self.set_name_finises_previous

            variable self.name

            variable self.modname

            variable self.breakable

            variable self.modelstates

            variable self.solid_faces

            variable self.no_collision

            variable self.create_callback

            variable self.delete_callback

            variable self.randomupdate_callback

            variable self.update_callback

            variable self.interaction_callback

            variable self.hardness

            variable self.minmum_toollevel

            variable self.blast_resistance

            variable self.besttools

            variable self.speed_multiplier

            variable self.block_item_generator_state

            variable self.face_name

            variable self.solid

            variable self.conducts_redstone

            variable self.can_mobs_spawn_on

            variable self.random_ticks_enabled

            variable self.customsolidsidefunction

            variable self.custommodelstatefunction

            variable self.customitemstackmodifcationfunction

            variable self.customblockitemmodificationfunction

            variable self.islog

            variable self.baseclass

            variable self.template

        function __call__(self, name: str = None)

        function copy(self)
            
            will copy the BlockFactory-object with all its content (including its template-link)
            :return: an copy of this


            variable obj.interaction_callback

            variable obj.customsolidsidefunction

            variable obj.custommodelstatefunction

            variable obj.customitemstackmodifcationfunction

            variable obj.customblockitemmodificationfunction

            variable obj.islog

            variable obj.baseclass

            variable obj.template

        function set_template(self, set_name_finises_previous=False)
            
            sets the current status as "template". This status will be set to on every .finish() call, but will not affect
            the new generated entry.


        function set_to_template(self)
            
            will reset the current object to the status right after the .set_template() call


            variable self.interaction_callback

            variable self.customsolidsidefunction

            variable self.custommodelstatefunction

            variable self.customitemstackmodifcationfunction

            variable self.customblockitemmodificationfunction

            variable self.random_ticks_enabled

            variable self.islog

            variable self.baseclass

        function reset_template(self)
            
            will delete the template-status


        function finish(self, register=True, reset_to_template=True, immediate=False)
            
            will finish up the process of configuration and register the finish_up-call for the future event
            :param register: unused
            :param reset_to_template: if the system should be reset to the configured template (if arrival) after finishing
                up
            :param immediate: if class generation should go on immediately or not
            :return: the BlockFactory instance. When the template exists, it will be an copy of the active without the
                template instance


        function finish_up(self)
            
            will finish up the system
            todo: clean up this mess!!!


                variable self.hardness

                variable self.blast_resistance

            class Baseclass extends object

                class Baseclass extends Baseclass,  cls

            variable master

            class ConstructedBlock extends Baseclass

                variable CUSTOM_WALING_SPEED_MULTIPLIER

                variable NAME

                variable BLOCK_ITEM_GENERATOR_STATE

                variable BREAKABLE

                variable BLAST_RESISTANCE

                variable SOLID

                variable CONDUCTS_REDSTONE_POWER

                variable CAN_MOBS_SPAWN_ON

                variable ENABLE_RANDOM_TICKS

                variable NO_COLLISION

                static
                function get_all_model_states()

                    variable states
                        make the entries unique!

                function __init__(self, *args, **kwargs)

                function on_remove(self)

                variable HARDNESS

                variable MINIMUM_TOOL_LEVEL

                variable BEST_TOOLS_TO_BREAK

                function set_model_state(self, state)

                function get_model_state(self)

                class ConstructedBlock extends ConstructedBlock

                    function __init__(self, *args, **kwargs)

                        variable self.face_solid

                class ConstructedBlock extends ConstructedBlock

                    function on_random_update(self): master.randomupdate_callback(self)
                            
                            if master.update_callback:
                            class ConstructedBlock(ConstructedBlock):

                class ConstructedBlock extends ConstructedBlock

                    function on_block_update(self)

                class ConstructedBlock extends ConstructedBlock

                    function on_player_interact(self, player, itemstack, button, modifiers, exact_hit) -> bool

                class ConstructedBlock extends ConstructedBlock

                    function on_request_item_for_block(self, itemstack)

                class ConstructedBlock extends ConstructedBlock

                    static
                    function modify_block_item(cls, itemconstructor)

                class ConstructedBlock extends ConstructedBlock

                    variable MODEL_FACE_NAME

                variable r

        function set_global_mod_name(self, name: str)
            
            will set the mod-prefix for the future (only very useful in template systems)
            :param name: the mod-prefix


        function set_solid_flag(self, state: bool)
            
            will set the SOLID-flag of the class
            :param state: the value to set to


        function set_conducts_redstone_power_flag(self, state: bool)
            
            will set the CAN_CONDUCT_REDSTONE-flag of the class
            :param state: the value to set to


        function set_can_mobs_spawn_on_flag(self, state: bool)
            
            will set the CAN_MOBS_SPAWN_ON-flag of the class
            :param state: the state to set to


        function set_name(self, name: str)
            
            will set the name of the block, when mod-prefix was set, the prefix is added in front with an ":" in between,
            but only if <name> has no ":" representing an "<mod-prefix>:<block name>".
            :param name: The name of the block


        function set_create_callback(self, function)
            
            will set an callback for the block creation in __init__-function of final class
            :param function: the function to invoke on creation. It is called together with the block instance


        function set_delete_callback(self, function)
            
            will set an callback for the deletion of the block
            :param function: the function to invoke on deletion. It is called together with the block instance


        @deprecation.deprecated("dev1-2", "a1.3.0")
        function setBrakeAbleFlag(self, state: bool)

        function set_break_able_flag(self, state: bool)
            
            will set the BREAKABLE-flag of the class
            :param state: the state to use


        function set_random_update_callback(self, function)
            
            will set the callback for random updates
            :param function: the function to invoke on random update together with the block instance


        function set_update_callback(self, function)
            
            will set the callback for an block update
            :param function: the function to invoke on an block update together with the block instance


        function set_custom_solid_side_function(self, function)
            
            will set the callback for the solid side system
            :param function: the function to invoke


        function set_solid_side_table_entry(self, side, state: bool)
            
            will set one entry in the solid face table
            :param side: the side to set
            :param state: the state to set to


        function set_custom_model_state_function(self, function)
            
            will set the model state getter callback for the class
            :param function: the function to invoke when needed


        function set_default_model_state(self, state)
            
            Will set the default model state of the block
            :param state: the state as an dict or an string-representation like in the block-state files
            :return:


            function get_state(*_): return state
                    
                    self.set_custom_model_state_function(get_state)
                    return self
                    
                    def set_all_model_state_info(self, modelstates: list):

        function set_all_model_state_info(self, modelstates: list)
            
            will set the list of all possible block states of the block
            :param modelstates: the model states, as an list of dicts
            todo: implement stringifier support


        function set_interaction_callback(self, function)
            
            sets the callback for the interaction event
            :param function: the function to invoke on
                (signature: block instance, player, itemstack, button, modifiers, exact_hit)


        function setFallable(self)
            
            will make the block affected by gravity


        function set_all_side_solid(self, state: bool)
            
            sets all side status of solid
            :param state: the status


        function set_log(self)
            
            makes the block an log-like block; Will need the needed block-state variation


        function set_slab(self)
            
            makes the block an slab-like block; Will need the needed block-state variation


        function set_hardness(self, value: float)
            
            will set the hardness of the block
            :param value: the value of the hardness


        function setStrenght(self, hardness: float, blast_resistance=None)
            
            will set hardness and blasz resistance at ones
            :param hardness: value for hardness
            :param blast_resistance: value for blast resistance, if None, hardness is used


        function enable_random_ticks(self)

        function set_minimum_tool_level(self, value: int)
            
            will set the minimum needed tool level for breaking the block
            :param value: the value representing an tool level


        function set_assigned_tools(self, tools)
            
            will set the tools good in breaking the block
            :param tools: an list of tools or only one tool


        function set_custom_itemstack_modification_function(self, function)
            
            will set the callback to modify the itemstack generated when the block is broken
            :param function: the function to invoke


        function set_custom_block_item_modification(self, function)
            
            will set the callback for the modification call for the ItemFactory-object generated by BlockItemFactory
            :param function: the function to invoke on callback


        function set_speed_multiplier(self, factor: float)
            
            sets the factor applied to the player movement speed when the player is ontop of the block
            :param factor: the factor to use


        function set_block_item_generator_state(self, state: dict)
            
            sets the state of the block to use when the BlockItemGenerator makes the image for the item
            :param state: the state as an dict
            todo: make this also accept an string


        function set_horizontal_orientable(self, face_name="facing")
            
            will set the block to horizontal orientable mode
            :param face_name: the name for the internal block-state reference for the orientation


        function set_blast_resistance(self, resistance: float)
            
            will set the resistance against explosions (internally not used, but part of the Block-API
            :param resistance: the resistance of the block


        function set_no_collision(self, value: bool = True)