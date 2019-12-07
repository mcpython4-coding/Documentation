***config.py - documentation***
___

This file is used for configurating various parts of the game

WARNING: some of the content of this file is not for changing by the end
user, it can affect the game in an way that it is afterwards UNPLAYABLE.
Make sure you know what you are doing when using this!

1. variable str MC_VERSION_BASE: the version of minecraft this version of the game is based on

2. variable str VERSION_TYPE: the type of the version, possible: "dev", "snapshot" and "release"

3. variable str VERSION_NAME: the name of the version

4. variable str FULL_VERSION_NAME: the full name of the version based on (1)-(3) 

5. variable int TICKS_PER_SEC: defaulted to 20, changing this will 
affect running speed of the game. 20 is also the speed of minecraft!
Used in window to set update schedule.

6. variable int/float WALKING_SPEED: how fast to walk, in blocks/sec

7. variable int/float SPRINTING_SPEED: how fast to sprint, in blocks/sec

8. variable int/float FLYING_SPEED: how fast to fly in gamemode 1, in 
blocks/sec

9. variable int/float FLYING_SPRINTING_SPEED: how fast to fly when 
sprinting in gamemode 1 in blocks/sec

10. variable int/float GAMEMODE_3_SPEED: how fast to fly in gamemode 3,
in blocks/sec

11. variable int/float GAMEMODE_3_SPRINTING_SPEED: how fast to fly when
sprinting in gamemode 3 in blocks/sec

12. variable dict<int: list<int/float>> SPEED_DICT: an dict from gamemode
to \[walking speed, sprinting speed\] or \[walking speed, sprinting 
speed, flying speed, fly-sprint-speed\] used to calculate traveled
distance in state.StatePartGame.StatePartGame._update, dynamically
generated from values (6) - (11).

13. int/float GRAVITY: the gravity in the game, in blocks/sec^2, used in 
state.StatePartGame.StatePartGame._update

14. int/float TERMINAL_VELOCITY: max downward speed, in blocks/sec, used
in state.StatePartGame.StatePartGame._update

15. float MAX_JUMP_HEIGHT: max height of the player to jump

16. float JUMP_SPEED: speed to the top on enter hit, in blocks/sec, used
in state.StatePartGame.StatePartGame._update, dynamically calculated
from (13) and (15)

17. int/float PLAYER_HEIGHT: how tall is the player? Used in
util.math.get_max_y and in state.StatePartGame.StatePartGame._update

18. list<tuple<int/float, int/float, int/float>> FACES: dx, dy, dz for
all 6 sides of a cube, used by world.Chunk.Chunk.exposed & 
world.Chunk.Chunk.check_neighbors 

19. list<tuple<int/float, int/float, int/float>> ADVANCED_FACES: like
18, but also including edge-positions, used by 
rendering.window.Window.collide

20. list<util.enums.EnumSide> FACE_NAMES: names of faces in order of 
faces in (18), used by world.Chunk.Chunk.exposed

21. list<util.enums.EnumSide> REVERSED_FACE_NAMES: the opposite sides to
(20), used by nothing, but maybe useful

22. int RANDOM_TICK_SPEED: how much random ticks per 16x16x16 sector?
used by event.TickHandler.TickHandler.send_random_ticks. defaulted to 3,
which is also minecraft's value

23. int RANDOM_TICK_RANGE: how far away random ticks are send, in 
chunks. Defaulted to 0 due to performance issues. Used by 
event.TickHandler.TickHandler.send_random_ticks