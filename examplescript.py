from mousemover import MouseMover

mover = MouseMover()

mover.move_to(1000, 200, 2)

mover.rel_move(300, 500, 3)

mover.set_mouse_position(1920/2, 1080/2)

my_position = mover.get_mouse_position()