***config.py - documentation***
___

This file is used for configurating various parts of the game

WARNING: some of the content of this file is not for changing by the end
user, it can affect the game in an way that it is afterwards UNPLAYABLE.
Make sure you know what you are doing when using this!

1. variable int TICKS_PER_SEC: defaulted to 20, changing this will 
affect running speed of the game. 20 is also the speed of minecraft!
Used in window to set update schedule.

2. variable int/float WALKING_SPEED: how fast to walk, in blocks/sec

3. variable int/float SPRINTING_SPEED: how fast to sprint, in blocks/sec

4. variable int/float FLYING_SPEED: how fast to fly in gamemode 1, in 
blocks/sec

5. variable int/float FLYING_SPRINTING_SPEED: how fast to fly when 
sprinting in gamemode 1 in blocks/sec

6. variable int/float GAMEMODE_3_SPEED: how fast to fly in gamemode 3,
in blocks/sec

7. variable int/float GAMEMODE_3_SPRINTING_SPEED: how fast to fly when
sprinting in gamemode 3 in blocks/sec

8. variable dict<int: list<int/float>> SPEED_DICT: an dict from gamemode
to \[walking speed, sprinting speed\] or \[walking speed, sprinting 
speed, flying speed, fly-sprint-speed\] used to calculate traveled
distance in state.StatePartGame.StatePartGame._update, dynamically
generated from values 2 - 7.

9. int/float GRAVITY: the gravity in the game, in blocks/sec^2, used in 
state.StatePartGame.StatePartGame._update

10. int/float TERMINAL_VELOCITY: max downward speed, in blocks/sec, used
in state.StatePartGame.StatePartGame._update

11. float MAX_JUMP_HEIGHT: max height of the player to jump

12. float JUMP_SPEED: speed to the top on enter hit, in blocks/sec, used
in state.StatePartGame.StatePartGame._update, dynamically calculated
from 9 and 11

13. int/float PLAYER_HEIGHT: how tall is the player? Used in
util.math.get_max_y and in state.StatePartGame.StatePartGame._update

14. list<tuple<int/float, int/float, int/float>> FACES: dx, dy, dz for
all 6 sides of a cube, used by world.Chunk.Chunk.exposed & 
world.Chunk.Chunk.check_neighbors 

15. list<tuple<int/float, int/float, int/float>> ADVANCED_FACES: like
14, but also including edge-positions, used by 
rendering.window.Window.collide

16. list<util.enums.EnumSide> FACE_NAMES: names of faces in order of 
faces in (14), used by world.Chunk.Chunk.exposed

17. list<util.enums.EnumSide> REVERSED_FACE_NAMES: the opposite sides to
(16), used by nothing, but maybe useful

18. int RANDOM_TICK_SPEED: how much random ticks per 16x16x16 sector?
used by event.TickHandler.TickHandler.send_random_ticks. defaulted to 3,
which is also minecraft's value

19. int RANDOM_TICK_RANGE: how far away random ticks are send, in 
chunks. Defaulted to 0 due to performance issues. Used by 
event.TickHandler.TickHandler.send_random_ticks