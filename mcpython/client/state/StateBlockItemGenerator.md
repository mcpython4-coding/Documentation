***StateBlockItemGenerator.py - documentation - last updated on 20.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
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

            variable item_registry

            variable window
                only here for making resizing possible again

            variable mcpython.common.event.TickHandler.handler.enable_tick_skipping

            variable shared.world.hide_faces_to_not_generated_chunks

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

    variable block_item_generator

    @onlyInClient()
    function create()