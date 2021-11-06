"""This module runs main script functionalities on a sample video.

------------

Exports
------------

    - :py:func:`sample.main` is main/entry function

-------------------------------

Related documentations/articles
-------------------------------

    - python style guide: https://www.python.org/dev/peps/pep-0008
    - python docstring conventions: https://www.python.org/dev/peps/pep-0257
    - documenting python devguide: https://devguide.python.org/documenting
    - reStructuredText docstring format: https://www.python.org/dev/peps/pep-0287
    - reStructuredText doc: https://docutils.sourceforge.io/rst.html
"""

from audio_video.main import video_to_mp3, mute_video


def main():
    """This is main/entry function.
    """
    samples_dir = "samples"
    sample_video_path = f"{samples_dir}/sample_video.mp4"

    video_to_mp3(
        video_path=sample_video_path,
        output_path=samples_dir,
        output_name="sample_audio",
    )

    mute_video(
        video_path=sample_video_path,
        output_path=samples_dir,
        output_name="sample_mute_video",
    )


if __name__ == "__main__":
    main()
