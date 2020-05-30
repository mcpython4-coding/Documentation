***StateWorldLoading.py - documentation - last updated on 30.5.2020 by uuk***
___

    class StateWorldLoading extends State.State

        variable NAME

        function __init__(self)

            variable self.status_table

            variable self.world_size

            variable self.finished_chunks

        function get_parts(self) -> list

        function on_update(self, dt)

        function on_activate(self)
                    
                    G.worldgenerationhandler.task_handler.schedule_invoke(
                        c, lambda: G.world.savefile.read("minecraft:chunk", dimension=G.world.active_dimension,
                                                        chunk=(cx, cz), immediate=False))


        function on_deactivate(self)

        function bind_to_eventbus(self)

        function on_key_press(self, symbol, modifiers)

        function on_draw_2d_post(self)

                variable status

                    variable factor

                    variable color

                    variable color

                    variable color

    variable worldloading

    function create()