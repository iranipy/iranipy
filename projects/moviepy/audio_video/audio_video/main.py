"""This module provides `moviepy` audio/video basic functionalities.

It's just a simple script to extract audio from video.

------------

Exports
------------

    - :py:func:`main.video_to_mp3` is a function which Extracts audio from video and save as mp3
    - :py:func:`main.mute_video` is a function which Removes audio from video

-------------------------------

Related documentations/articles
-------------------------------

    - moviepy: https://zulko.github.io/moviepy
    - python style guide: https://www.python.org/dev/peps/pep-0008
    - python docstring conventions: https://www.python.org/dev/peps/pep-0257
    - documenting python devguide: https://devguide.python.org/documenting
    - reStructuredText docstring format: https://www.python.org/dev/peps/pep-0287
    - reStructuredText doc: https://docutils.sourceforge.io/rst.html
"""

from moviepy.video.io.VideoFileClip import VideoFileClip


def video_to_mp3(video_path: str, output_path: str, output_name: str):
    """Extracts audio from video and save as mp3.

    :param video_path: path to video file
    :type video_path: str
    :param output_path: path, where the output should be saved in
    :type output_path: str
    :param output_name: output filename
    :type output_name: str
    """
    with VideoFileClip(video_path) as video:
        audio = video.audio
        audio.write_audiofile(f"{output_path}/{output_name}.mp3")


def mute_video(video_path: str, output_path: str, output_name: str):
    """Removes audio from video.

    :param video_path: path to video file
    :type video_path: str
    :param output_path: path, where the output should be saved in
    :type output_path: str
    :param output_name: output filename
    :type output_name: str
    """
    with VideoFileClip(video_path) as video:
        ext = video.filename.split(".")[-1]
        muted = video.without_audio()
        muted.write_videofile(
            f"{output_path}/{output_name}.{ext}",
            audio=False, codec="mpeg4"
        )
