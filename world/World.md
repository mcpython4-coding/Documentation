***World.py - documentation - last updated on 14.5.2020 by uuk***
___

    class World
        function __init__(self, filename=None)

            variable self.players - when in an network, stores an reference to all other players


            variable self.active_player
                self.add_player("unknown", add_inventories=False)

        function add_player(self, name, add_inventories=True)
        function get_active_player(self)
        function reset_config(self)
        function get_active_dimension(self) -> world.Dimension.Dimension
        function add_dimension(self, id, name, config={}) -> world.Dimension.Dimension
        function join_dimension(self, id, save_current=True)
        function hit_test(self, position, vector, max_distance=8)
            
            intersected it is returned, along with the block previously in the line
            of sight. If no block is found, return None, None.
    
            Parameters
            ----------
            position : tuple of len 3
                The (x, y, z) position to check visibility from.
            vector : tuple of len 3
                The line of sight vector.
            max_distance : int
                How many blocks away to search for a hit.
    
            


            variable m


            variable previous


                variable key


                variable blocki


                    variable previous

        function show_sector(self, sector, immediate=False)
            
            drawn to the canvas.
    
            

        function hide_sector(self, sector, immediate=False)
            
            removed from the canvas.
    
            

        function change_sectors(self, before, after, immediate=False, generate_chunks=True, load_immediate=False)
            
            contiguous x, y sub-region of world. Sectors are used to speed up
            world rendering.
    
            


            variable before_set


            variable after_set


            variable pad


            variable show


            variable hide


                        variable chunk

        function process_queue(self)
        function process_tasks(self, timer=0.2)
        function process_entire_queue(self)
            
            todo: remove
    
            

        function cleanup(self, remove_dims=False, filename=None, add_player=False)
        function setup_by_filename(self, filename: str)