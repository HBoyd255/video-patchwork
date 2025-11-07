import os
import time
import cv2
import numpy
from calculation import calculate_grid_size


feed_width = 190
feed_height = 100


for frame_count_i in range(1, 100):

    (column_count, row_count) = calculate_grid_size(frame_count_i)

    canvas_width = column_count * feed_width
    canvas_height = row_count * feed_height

    print(canvas_width)

    image = numpy.zeros((canvas_height, canvas_width, 3), dtype=numpy.uint8)

    for feed_i in range(frame_count_i):
        x = feed_i % column_count
        y = feed_i // column_count

        print(x, y)

        # print(x, y)

        pt1 = numpy.array((x * feed_width, y * feed_height))

        print(pt1)

        pt2 = pt1 + (feed_width, feed_height) - (1, 1)

        print(pt2)

        cv2.rectangle(image, pt1, pt2, (255, 255, 0), 1)
        cv2.putText(
            image,
            f"{feed_i}",
            (pt1 + (15, 30)),
            cv2.FONT_HERSHEY_TRIPLEX,
            1,
            (0, 0, 255),
            2,
        )

    print(f"({column_count},{row_count})")

    cv2.imshow("Patchwork Canvas", image)

    key = cv2.waitKey(1) & 0xFF

    # If esc is pressed, exit the program
    if key == 27:
        os._exit(0)

    time.sleep(0.2)
