***StateBlockItemGenerator.py - documentation - last updated on 16.5.2020 by uuk***
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

        function on_draw_2d_pre(self)

        function bind_to_eventbus(self)

        function on_resize(self, w, h)

        function on_activate(self)

        function on_deactivate(self)

        function close(self)

        function add_new_screen(self, *args)

        function take_image(self, *args)

        function _error_counter(self, image, blockname)

        function generate_item(self, blockname, file)

    variable blockitemgenerator

    function create()