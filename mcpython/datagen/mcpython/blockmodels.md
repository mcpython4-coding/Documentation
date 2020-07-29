***blockmodels.py - documentation - last updated on 29.7.2020 by uuk***
___

    variable DEFAULT_OUTPUT - where to output data - in dev environment

    function generate_button_template(config)

    function generate_button_state(config, name)

    function generate_door_template(config)

    function generate_door_state(config, name)

    function generate_trapdoor_template(config)

    function generate_trapdoor(config, name)

    function generate_fence_template(config)

    function generate_fence_state(config, name)

    function generate_fence_gate_template(config)

    function generate_fence_gate_state(config, name)

    function generate_pressure_plate_state(config, name)

    function generate_stair_base(config)

    function generate_stairs_state(config, name)

    function generate_one_to_one(config, name)

    function generate_wall_template(config)

    function generate_log_template(config)

    @G.modloader("minecraft", "special:datagen:configure")
    function generate_recipes()
        
        generator for all non-combined-generated block models in minecraft


        variable config