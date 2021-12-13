***AbstractState.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractState extends IRegistryContent,  ABC
        
        Base class for all states
        Handled by the StateHandler of the game
        activate() is invoked when the state is switched to, deactivate() when switching away
        bind_to_eventbus() is a helper function for registering functions to the internal event bus
        (It should be used as it is automatically bind when the state is active)
        create_state_parts() is the initializer for the "parts" attribute and can be used to return a list of StatePart's,
        bound also when needed


        variable IS_MOUSE_EXCLUSIVE
            Set this if the state is mouse-exclusive, so the mouse is hidden
            For more finer control, use the is_mouse_exclusive() getter method

        variable CONFIG_LOCATION: typing.Optional[str]
            Default location: data/{mod}/states/{name}.json

        static
        function is_mouse_exclusive(cls) -> bool:  # todo: make attribute
                return cls.IS_MOUSE_EXCLUSIVE
                
                def __init__(self):

        function __init__(self)

            variable self.part_dict
                Internal attribute used when loading serialized states, as they have named their StateParts internally

            variable self.eventbus
                Constructs the underlying parts array

            variable self.parts

                variable state_part.master
                    StateParts get an list of steps to get to them as an list

                variable state_part.eventbus

                variable self.underlying_batch

                variable self.state_renderer

                    variable self.state_renderer.assigned_state

                    variable self.state_renderer.batch

                variable self.state_renderer

                variable self.underlying_batch

        function create_state_renderer(self) -> typing.Any
            
            Optional creates a AbstractStateRenderer instance for this state
            Only invoked on client side
            May return None when no state renderer is needed (e.g. when all is handled somewhere in the parts)


        function create_state_parts(self) -> typing.List
            
            Creates the parts of the state (instances of AbstractStatePart)
            When not overwritten, defaults to no state parts
            Invoked somewhere during state construction; Not further defined by API
            WARNING: this might get invoked DURING the constructor of THIS class,
                so invoking super().__init__() will result into this being invoked. When writing to the same variables
                as below the line in the constructor, this will reset the values!


        function bind_to_eventbus(self)
            
            Helper method for binding to the internal EventBus
            Invoked somewhere during state construction; Not further defined by API
