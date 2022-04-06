from pystage.en import Stage

stage = Stage()
stage.add_backdrop("")
zombie = stage.add_a_sprite()

def doit(zombie):
    zombie.change_x_by(10)

zombie.when_program_starts(doit)

stage.play()