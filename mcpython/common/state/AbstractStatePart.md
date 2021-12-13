***AbstractStatePart.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractStatePart extends ABC

        variable NAME: typing.Optional[str]

        function __init__(self)

            variable self.parts: typing.List["AbstractStatePart"]

            variable self.master

            variable self.underlying_batch

            variable self.state_renderer

            variable self.eventbus

            variable self.state_renderer_init

        function init_rendering(self)

            variable self.underlying_batch

            variable self.eventbus

            variable self.state_renderer

                variable self.state_renderer.assigned_state

                variable self.state_renderer.batch

        function create_state_renderer(self) -> typing.Any

        function get_sub_parts(self) -> typing.List["AbstractStatePart"]

        function bind_to_eventbus(self)