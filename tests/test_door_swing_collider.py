import pytest
import gameplay.door_swing_collider as mod

CASES = [
    ("collider_by_angle", (1,)),
    ("server_authoritative_open", (1,)),
    ("collider_on_model_swap", (1,)),
    ("single_axis_write", (1,)),
    ("remove_on_unload", (1,)),
    ("event_by_time", (1,)),
    ("open", (1,)),
    ("push", (1,)),
    ("load", (1,)),
    ("unload", (1,)),
    ("validate_door", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
