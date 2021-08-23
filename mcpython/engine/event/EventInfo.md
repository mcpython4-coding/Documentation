***EventInfo.py - documentation - last updated on 23.8.2021 by uuk***
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
        
        Base class for every event info declared here


        function equals(self, *args)

    class KeyPressEventInfo extends IEventInfo
        
        info for key press


        function __init__(self, symbol: int, modifier=None)

                variable modifier

        function equals(self, symbol, modifiers)

    class MousePressEventInfo extends IEventInfo
        
        Info for mouse press


        function __init__(self, mouse: int, modifier=None, area=None)

                variable modifier

        function equals(self, x, y, button, modifiers)