# Wishing-Happy-Birthday-using-Python-Program
Wish a programming style and send this code to your coder friend also your other friends and give him/her a surprise on his/her Birthday !

from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText(" H  A  P  P  Y ", font='big'),
            int(screen.height / 3 - 5)),
        Cycle(
            screen,
            FigletText(" B  I  R  T  H  D  A  Y ", font='big'),
            int(screen.height / 2 - 1)),
        Cycle(
            screen,
            FigletText(" V  I  S  H  A  L ", font='big'),
            int(screen.height / 2 + 8)),
        Stars(screen, 300)
    ]
    screen.play([Scene(effects, 500)])


Screen.wrapper(demo)
