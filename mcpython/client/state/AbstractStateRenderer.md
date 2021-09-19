***AbstractStateRenderer.py - documentation - last updated on 19.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractStateRenderer extends ABC
        
        Base class for state renderers


        variable ASSIGNED_DRAW_STAGE

        function __init__(self)

            variable self.batch: typing.Optional[pyglet.graphics.Batch]

            variable self.assigned_state

        function init(self)

        function on_activate(self)

        function on_deactivate(self)

        function draw(self)

        function resize(self, width: int, height: int)