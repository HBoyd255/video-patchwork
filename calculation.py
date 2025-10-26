
import math

def calculate_grid_size(video_feed_count: int) -> tuple[int, int]:

    column_count = math.ceil(math.sqrt(video_feed_count))
    row_count = math.ceil(video_feed_count / column_count)

    return (column_count, row_count)


