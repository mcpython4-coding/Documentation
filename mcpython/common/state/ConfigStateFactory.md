***ConfigStateFactory.py - documentation - last updated on 28.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class IStateConfigEntry extends mcpython.common.event.api.IRegistryContent
        
        base class for every entry in an config file


        variable TYPE

        static
        function deserialize(
                cls,
                state_instance,
                data: dict,
                existing: typing.Union[
                None, mcpython.common.state.AbstractStatePart.AbstractStatePart
                ],
                ) -> mcpython.common.state.AbstractStatePart.AbstractStatePart:

    variable entry_registry

    @shared.registry class UIButtonDefaultStateConfigEntry extends IStateConfigEntry

        variable NAME

        static
        function deserialize(
                cls,
                state_instance,
                data: dict,
                existing: typing.Union[
                None, mcpython.common.state.AbstractStatePart.AbstractStatePart
                ],
                ) -> mcpython.common.state.AbstractStatePart.AbstractStatePart:

            variable size

            variable text

            variable position

            variable anchor_window

            variable anchor_button

            variable enabled

            variable has_hov

            variable on_press

                variable on_press

                variable existing.bounding_box_size

                variable existing.text

                variable existing.position

                variable existing.anchor_element

                variable existing.anchor_window

                variable existing.enabled

                variable existing.has_hovering_state

                variable existing.on_press

    @shared.registry class UILableStateConfigEntry extends IStateConfigEntry

        variable NAME

        static
        function deserialize(
                cls,
                state_instance,
                data: dict,
                existing: typing.Union[
                None, mcpython.common.state.AbstractStatePart.AbstractStatePart
                ],
                ) -> mcpython.common.state.AbstractStatePart.AbstractStatePart:

            variable text

            variable position

            variable anchor_window

            variable anchor_lable

            variable on_press

            variable color

            variable text_size

                variable existing.text

                variable existing.position

                variable existing.anchor_window

                variable existing.anchor_element

                variable existing.on_press

                variable existing.color

                variable existing.text_size

    @shared.registry class UIProgressBarConfigEntry extends IStateConfigEntry

        variable NAME

        static
        function deserialize(
                cls, state_instance, data: dict, existing
                ) -> mcpython.common.state.AbstractStatePart.AbstractStatePart:

            variable position

            variable size

            variable color

            variable item_count

            variable status

            variable text

            variable anchor_ele

            variable anchor_win

                variable existing.position

                variable existing.size

                variable existing.anchor_window

                variable existing.anchor_element

                variable existing.color

                variable existing.progress

                variable existing.progress_max

                variable existing.text

    @shared.registry class ConfigBackground extends IStateConfigEntry

        variable NAME

        static
        function deserialize(
                cls,
                state_instance,
                data: dict,
                existing: typing.Union[
                None, mcpython.common.state.AbstractStatePart.AbstractStatePart
                ],
                ) -> mcpython.common.state.AbstractStatePart.AbstractStatePart:

    variable configs

    function get_config(file: str)

    class StateConfigFile
        
        Class for deserialize a config file for a state into a state


        function __init__(self, file: str)
            
            Constructs n new deserializer for a file


            variable self.file

            variable self.data

            variable self.injected_objects

        function inject(
                self,
                state_instance: typing.Union[
                mcpython.common.state.AbstractState.AbstractState,
                mcpython.common.state.AbstractStatePart.AbstractStatePart,
                ],
                retry: bool = True,
                ):
            
            Will make the given state an state of the kind specified by this file
            :param state_instance: the state to inject the data into
            :param retry: internal flag if to schedule a reload if the data is not arrival
            WARNING: will override ALL existing data from state parts and their config


                variable state_instance.IS_MOUSE_EXCLUSIVE

                    variable d

                    variable prev

                    variable part

                    variable state_instance.part_dict[name]

                        variable part.master
            
            Will reload the context and parse into the previous injected states
            Called by the system on data reload
            Will internally re-call the inject()-function on every state


            variable self.data

        function __del__(self)