***EventInfo.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class IEventInfo
        
        base class for every event info


        function equals(self, *args)

    class KeyPressEventInfo extends IEventInfo
        
        info for key press


        function __init__(self, symbol: int, modifier=None)

                variable modifier

        function equals(self, symbol, modifiers)

    class MousePressEventInfo extends IEventInfo
        
        info for mouse press


        function __init__(self, mouse: int, modifier=None, area=None)

                variable modifier

        function equals(self, x, y, button, modifiers)

    class CallbackHelper

        function __init__(
                self,
                function,
                args=None,
                kwargs=None,
                extra_arg_filter=None,
                enable_extra_args=True,
                ):
            
            creates an new object
            :param function: the function to call
            :param args: the args given
            :param kwargs: the kwargs given
            :param extra_arg_filter: an function(args, kwargs) -> args, kwargs which filters them
            :param enable_extra_args: weither args given by __call__ should be included


                variable kwargs

                variable args

            variable self.function

            variable self.args

            variable self.kwargs

            variable self.filter

            variable self.enable_extra_args

        function __call__(self, *args, **kwargs)