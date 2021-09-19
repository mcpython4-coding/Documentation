***RenderingLayerManager.py - documentation - last updated on 19.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable __all__

    class RenderingLayer

        function __init__(self, rendering_manager: "RenderingLayerManager", name: str)

            variable self.manager

            variable self.name

            variable self.event_name

            variable self.enabled

            variable self.rendering_mode

            variable self.invoke_after

            variable self.invoke_before

            variable self.draw_subscribers

        function activate(self)

        function deactivate(self)

        function renderAfter(self, layer: typing.Union[str, "RenderingLayer"])

        function renderBefore(self, layer: typing.Union[str, "RenderingLayer"])

        function setRenderingMode(self, mode: str)

        function getRenderingEvent(self) -> str

        function registerEventSub(self, sub: typing.Callable)

        function isEnvEqual(self, other: "RenderingLayer") -> bool

        function setupEnv(self)

        function draw(self)

        function resetEnv(self)

    class RenderingLayerManager

        function __init__(self)

            variable self.ordered_layers: typing.List[RenderingLayer]

            variable self.schedule_resort

        function register_rendering_stage(self, name: str)

        function create_rendering_event(self, name: str)

        function draw(self)

            variable prev_layer

                variable prev_layer

        function sort_layers(self)

            variable layers

            variable graph

            variable self.ordered_layers

    variable manager

    variable REAL_BACKGROUND

    variable NORMAL_WORLD

    variable INTER_BACKGROUND

    variable MIDDLE_GROUND

    variable FOREGROUND