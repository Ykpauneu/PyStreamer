from . import (
    create_dynamic_map_icon,
    destroy_dynamic_map_icon,
    is_valid_dynamic_map_icon,
)


class DynamicMapIcon:
    def __init__(self, id) -> None:
        self.id = id

    @classmethod
    def create(
        x: float,
        y: float,
        z: float,
        type: int,
        color: int,
        world_id: int = -1,
        interior_id: int = -1,
        player_id: int = -1,
        stream_distance: float = 200.0,
        style: int = 0,
        area_id: int = -1,
        priority: int = 0,
    ):
        return cls(
            create_dynamic_map_icon(
                x,
                y,
                z,
                type,
                color,
                world_id,
                interior_id,
                player_id,
                stream_distance,
                style,
                area_id,
                priority,
            )
        )

    def destroy(self):
        return destroy_dynamic_map_icon(self.id)

    def is_valid(self):
        return is_valid_dynamic_map_icon(self.id)
