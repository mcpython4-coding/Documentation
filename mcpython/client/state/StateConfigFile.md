***StateConfigFile.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class IStateConfigEntry extends mcpython.common.event.Registry.IRegistryContent
        
        base class for every entry in an config file


        variable TYPE

        static
        function deserialize(
                cls,
                state_instance,
                data: dict,
                existing: typing.Union[None, mcpython.client.state.StatePart.StatePart],
                ) -> mcpython.client.state.StatePart.StatePart:

    variable entry_registry

    @shared.registry @onlyInClient() class UIButtonDefaultStateConfigEntry extends IStateConfigEntry

        variable NAME

        static
        function deserialize(
                cls,
                state_instance,
                data: dict,
                existing: typing.Union[None, mcpython.client.state.StatePart.StatePart],
                ) -> mcpython.client.state.StatePart.StatePart:

            variable size

            variable text

            variable position

            variable anchor_window

            variable anchor_button

            variable enabled

            variable has_hov

            variable on_press

                variable on_press

                variable existing.bboxsize

                variable existing.text

                variable existing.position

                variable existing.anchor_element

                variable existing.anchor_window

                variable existing.enabled

                variable existing.has_hovering_state

                variable existing.on_press

    @shared.registry @onlyInClient() class UILableStateConfigEntry extends IStateConfigEntry

        variable NAME

        static
        function deserialize(
                cls,
                state_instance,
                data: dict,
                existing: typing.Union[None, mcpython.client.state.StatePart.StatePart],
                ) -> mcpython.client.state.StatePart.StatePart:

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

    @shared.registry @onlyInClient() class UIProgressBarConfigEntry extends IStateConfigEntry

        variable NAME

        static
        function deserialize(
                cls, state_instance, data: dict, existing
                ) -> mcpython.client.state.StatePart.StatePart:

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

    @shared.registry @onlyInClient() class ConfigBackground extends IStateConfigEntry

        variable NAME

        static
        function deserialize(
                cls,
                state_instance,
                data: dict,
                existing: typing.Union[None, mcpython.client.state.StatePart.StatePart],
                ) -> mcpython.client.state.StatePart.StatePart:

    variable configs

    @onlyInClient()
    function get_config(file: str)

    @onlyInClient() class StateConfigFile
        
        Class for deserialize an config file for an state into an state


        function __init__(self, file: str)
            
            Constructs an new deserializer for an file


            variable self.file

            variable self.data

            variable self.injected_objects

        function inject(
                self,
                state_instance: typing.Union[
                mcpython.client.state.State.State, mcpython.client.state.StatePart.StatePart
                ],
                ):
            
            will make the given state an state of the kind specified by this file
            :param state_instance: the state to inject the data into
            WARNING: will override ALL existing data from state parts and their config


                variable state_instance.IS_MOUSE_EXCLUSIVE

                    variable d

                    variable prev

                    variable part

                    variable state_instance.part_dict[name]

                        variable part.master

        function reload(self)
            
            Will reload the context and parse into the previous injected states
            Called by the system on data reload
            Will internally re-call the inject()-function on every state


        function __del__(self)