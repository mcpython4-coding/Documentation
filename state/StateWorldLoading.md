***StateWorldLoading.py - documentation - last updated on 14.5.2020 by uuk***
___

    class StateWorldLoading extends State.State

        variable NAME

        function __init__(self)

            variable self.status_table

            variable self.world_size

            variable self.finished_chunks

        function get_parts(self) -> list

        function on_update(self, dt)

                variable c

                variable self.status_table[chunk]

            variable self.parts[1].text

        function on_activate(self)

            variable G.worldgenerationhandler.enable_generation

                    variable c
                    
                    G.worldgenerationhandler.task_handler.schedule_invoke(
                        c, lambda: G.world.savefile.read("minecraft:chunk", dimension=G.world.active_dimension,
                                                        chunk=(cx, cz), immediate=False))


            variable G.worldgenerationhandler.enable_generation

        function on_deactivate(self)

            variable player

        function bind_to_eventbus(self)

        function on_key_press(self, symbol, modifiers)

        function on_draw_2d_post(self)

                variable self.parts[1].text

                variable self.parts[1].text

                variable status

                    variable factor

                    variable color

                    variable color

                    variable color

    variable worldloading

    function create()

        variable worldloading