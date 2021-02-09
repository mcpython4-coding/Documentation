***RenderingGroups.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class CollectionGroup extends pyglet.graphics.Group
        
        Group of groups


        function __init__(self, *sub_groups)

            variable self.sub_groups

        function set_state(self)

        function unset_state(self)

    @onlyInClient() class MatrixStackGroup extends pyglet.graphics.Group
        
        Group for holding an custom MatrixStack-instance


        function __init__(self, stack: mcpython.client.rendering.MatrixStack.MatrixStack)

            variable self.stack

        function set_state(self)

        function unset_state(self)

    @onlyInClient() class ScissorGroup extends pyglet.graphics.Group
        
        Code by: pyglet
        url: https://github.com/pyglet/pyglet/blob/pyglet-1.5-maintenance/examples/opengl/opengl_scissor.py
        A Custom Group that defines a "Scissor" area.
        If a Sprite/Label is in this Group, any parts of it that
        fall outside of the specified area will not be drawn.
        NOTE: You should use the same exact group instance
        for every object that will use the group, equal groups
        will still be kept seperate.
        :Parameters:
            `x` : int
                The X coordinate of the Scissor area.
            `x` : int
                The X coordinate of the Scissor area.
            `width` : int
                The width of the Scissor area.
            `height` : int
                The height of the Scissor area.


        function __init__(self, x, y, width, height, parent=None)

        @property
        function area(self)

        @area.setter
        function area(self, area)

        function set_state(self)

        function unset_state(self)