***StateBlockItemGenerator.py - documentation - last updated on 14.5.2020 by uuk***
___

    class StateBlockItemGenerator extends State.State

        variable SETUP_TIME

        variable CLEANUP_TIME

        variable NAME

        function __init__(self)

            variable self.blockindex

            variable self.tasks

            variable self.table

            variable self.last_image

            variable self.tries

            variable self.failed_counter

        function get_parts(self) -> list

            variable kwargs

        function on_draw_2d_pre(self)

            variable self.parts[2].position

            variable process

                variable self.parts[2].progress

            variable self.parts[2].text

        function bind_to_eventbus(self)

        function on_resize(self, w, h)

            variable self.parts[1].size

        function on_activate(self)

            variable G.world.hide_faces_to_ungenerated_chunks

            variable G.tickhandler.enable_random_ticks

            variable self.tasks

                        variable self.table

                variable items

            variable self.parts[1].progress_max

            variable self.parts[1].progress

            variable G.world.get_active_player().position

            variable G.world.get_active_player().rotation

            variable self.blockindex

                variable blockinstance

                variable self.blockindex

            variable event.TickHandler.handler.enable_tick_skipping
                event.TickHandler.handler.bind(self.take_image, SETUP_TIME)

        function on_deactivate(self)

            variable event.TickHandler.handler.enable_tick_skipping

            variable G.tickhandler.enable_random_ticks

            variable G.world.hide_faces_to_ungenerated_chunks

        function close(self)

            variable G.world.get_active_player().position

            variable G.world.get_active_player().rotation

            variable self.last_image

        function add_new_screen(self, *args)

                variable blockinstance

            variable self.parts[1].progress

            variable self.parts[1].text

        function take_image(self, *args)

            variable blockname

            variable file

            variable image: PIL.Image.Image

            variable image - todo: make dynamic based on window size

            variable self.last_image

        function _error_counter(self, image, blockname)

                variable self.last_image

                variable file

                variable file - use missing texture instead

        function generate_item(self, blockname, file)

            variable obj

            variable block

            variable self.tries

            variable self.SETUP_TIME

            variable self.CLEANUP_TIME

    variable blockitemgenerator

    function create()

        variable blockitemgenerator