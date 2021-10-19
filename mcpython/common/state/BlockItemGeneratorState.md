***BlockItemGeneratorState.py - documentation - last updated on 19.10.2021 by uuk***
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

    class BlockItemGenerator extends AbstractState.AbstractState

        variable SETUP_TIME

        variable CLEANUP_TIME

        variable NAME

        function __init__(self)

            variable self.status_bar

            variable self.memory_bar

            variable self.block_index: int
                The current block number

            variable self.tasks: typing.List[str]
                The block names

            variable self.table
                Temporary storage for the information in the json file for later runs

            variable self.draw_calls_since_last_take

        function create_state_parts(self) -> list

            variable self.status_bar
                We want a progress bar to inform te user

            variable self.memory_bar

        function on_draw_2d_pre(self)

        function bind_to_eventbus(self)

        function on_resize(self, w, h)

        function tick(self, _)

        function activate(self)

            variable world

            variable item_registry

            variable self.tasks
                Fetch the list of all blocks

            variable shared.model_handler.hide_blockstate_errors
                We want to hide this error messages
                todo: add command line option to disable

            variable self.status_bar.progress_max
                Update the progress bar

            variable self.status_bar.progress

            variable player
                Setup the player view, todo: make configurable by block model / state

            variable player.position

            variable player.rotation

            variable self.block_index
                Which block we are currently working on

                variable instance

                variable self.block_index

            variable TickHandler.handler.enable_tick_skipping
                We do not want to skip ticks, as this would be bad here...

        function prepare_window(self)

        function load_previous_data(self)

        function clean_world(self, world)

        function deactivate(self)

            variable shared.model_handler.hide_blockstate_errors
                We want to enable this again

            variable window
                only here for making resizing possible again

            variable TickHandler.handler.enable_tick_skipping

            variable shared.world.hide_faces_to_not_generated_chunks

            variable item_registry

        function bake_items(self)

        function close(self)

        function add_new_screen(self, *args)

            variable dimension

            variable block

                variable instance

            variable self.status_bar.progress

            variable self.status_bar.text

            variable self.draw_calls_since_last_take

        function take_image(self, *args)

            variable block_name

            variable file

            variable image: PIL.Image.Image

            variable image

        function generate_item(self, block_name: str, file: str)

            variable model

            variable ItemModel.handler.models[block_name]

            variable self.SETUP_TIME

            variable self.CLEANUP_TIME

    variable block_item_generator

    function create()