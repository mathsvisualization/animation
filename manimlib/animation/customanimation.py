from __future__ import annotations

from manimlib.animation.transform import Restore
from manimlib.mobject.geometry import Circle
from manimlib.constants import YELLOW

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from manimlib.typing import Vect3

DEFAULT_CLACK_ANIMATION_RUNTIME = 2.0

class ClackAnimation(Restore):
    def __init__(
        self,
        point: Vect3,
        run_time: float = DEFAULT_CLACK_ANIMATION_RUNTIME,
        **kwargs
    ):
        circles = Circle(radius=0.25).replicate(3)
        circles.move_to(point)
        circles.set_stroke(YELLOW, 0, 0)
        circles.save_state()
        circles.scale(0.1)
        circles.set_stroke(YELLOW, 2, 1)

        super().__init__(circles, lag_ratio=0.1, run_time=run_time, **kwargs)