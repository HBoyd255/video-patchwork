# Video Patchwork

This module combines the functionality of
[Flask](https://pypi.org/project/Flask/) and
[Open CV](https://pypi.org/project/opencv-python/) allowing multiple videos to
be served to separate Open CV windows, and stitched together into one video
stream via Flask.

## Background

A past project of mine,
[Project G.E.S.T.U.R.E.](https://hboyd.co.uk/projects/gesture/), ws was based
around capturing two Raspberry Pi Camera video feeds and processing them on a
headless Raspberry Pi. To debug and analyse the pipeline, I needed to be able to
steam multiple feeds. Although streaming multiple feeds with flask is
possible, managing each of the separate feeds on the other end can be difficult
to organise.
