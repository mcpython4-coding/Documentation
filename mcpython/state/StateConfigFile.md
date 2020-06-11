***StateConfigFile.py - documentation - last updated on 11.6.2020 by uuk***
___

    class IStateConfigEntry extends mcpython.event.Registry.IRegistryContent
        
        base class for every entry in an config file


        variable TYPE

    variable entry_registry

    @G.registry class UIButtonDefaultStateConfigEntry extends IStateConfigEntry

        variable NAME

        static
        function deserialize(cls, state_instance, data: dict,
                existing: typing.Union[
                None, mcpython.state.StatePart.StatePart]) -> mcpython.state.StatePart.StatePart:

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

    @G.registry class UILableStateConfigEntry extends IStateConfigEntry

        variable NAME

        static
        function deserialize(cls, state_instance, data: dict, existing: typing.Union[
                None, mcpython.state.StatePart.StatePart]) -> mcpython.state.StatePart.StatePart:

                variable existing.text

                variable existing.position

                variable existing.anchor_window

                variable existing.anchor_element

                variable existing.on_press

                variable existing.color

                variable existing.text_size

    @G.registry class UIProgressBarConfigEntry extends IStateConfigEntry

        variable NAME

        static
        function deserialize(cls, state_instance, data: dict, existing) -> mcpython.state.StatePart.StatePart

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

    @G.registry class ConfigBackground extends IStateConfigEntry

        variable NAME

        static
        function deserialize(cls, state_instance, data: dict,
                existing: typing.Union[None, mcpython.state.StatePart.StatePart]) -> \
                mcpython.state.StatePart.StatePart:
                import mcpython.state.StatePartConfigBackground
                if existing is not None and issubclass(type(existing),
                mcpython.state.StatePartConfigBackground.StatePartConfigBackground):

    variable configs

    function get_config(file: str)

    class StateConfigFile
        
        Class for deserialize an config file for an state into an state


        function __init__(self, file: str)
            
            Constructs an new deserializer for an file


            variable self.file

            variable self.data

            variable self.injected_objects

        function inject(self, state_instance: typing.Union[mcpython.state.State.State, mcpython.state.StatePart.StatePart])
            
            will make the given state an state of the kind specified by this file
            :param state_instance: the state to inject the data into
            WARNING: will override ALL existing data from state parts and their config


        function reload(self)
            
            Will reload the context and parse into the previous injected states
            Called by the system on data reload
            Will internally re-call the inject()-function on every state


        function __del__(self)