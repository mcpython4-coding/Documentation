***StateBlockItemGenerator.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class StateBlockItemGenerator extends State.State

        variable SETUP_TIME

        variable CLEANUP_TIME

        variable NAME

        function __init__(self)

            variable self.blockindex

            variable self.tasks: typing.List[str]

            variable self.table

            variable self.last_image

            variable self.tries

            variable self.failed_counter

        function get_parts(self) -> list

        function on_draw_2d_pre(self)

        function bind_to_eventbus(self)

        function on_resize(self, w, h)

        function activate(self)

            variable item_registry

                variable world.hide_faces_to_not_generated_chunks

                variable shared.tick_handler.enable_random_ticks

            variable self.tasks

                        variable self.table

                variable items

            variable shared.model_handler.hide_blockstate_errors

            variable self.parts[1].progress_max

            variable self.parts[1].progress

            variable window
                setup the window

            variable player
                setup the player view, todo: make configurable by block

            variable player.position

            variable player.rotation

            variable self.blockindex

                variable instance

                variable self.blockindex

            variable mcpython.common.event.TickHandler.handler.enable_tick_skipping

        function deactivate(self)

            variable window
                only here for making resizing possible again

            variable mcpython.common.event.TickHandler.handler.enable_tick_skipping

            variable shared.world.hide_faces_to_not_generated_chunks

            variable item_registry

        function close(self)

        function add_new_screen(self, *args)

            variable dimension

            variable block

                variable instance

            variable self.parts[1].progress

            variable self.parts[1].text

        function take_image(self, *args)

            variable blockname

            variable file

            variable image: PIL.Image.Image

            variable image

            variable self.last_image

        function _error_counter(self, image, blockname)

        function generate_item(self, blockname, file)

            variable model

            variable mcpython.client.rendering.model.ItemModel.handler.models[blockname]

            variable self.tries

            variable self.SETUP_TIME

            variable self.CLEANUP_TIME

    variable block_item_generator

    @onlyInClient()
    function create()