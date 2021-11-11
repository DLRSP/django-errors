import os
import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    os.environ["CUSTOM_COMPILE_COMMAND"] = "requirements/compile.py"
    # os.environ.pop("PIP_REQUIRE_VIRTUALENV")

    common_args = [
        "-m",
        "piptools",
        "compile",
        "--generate-hashes",
        "--allow-unsafe",
    ] + sys.argv[1:]

    subprocess.run(
        [
            "python36",
            "-m",
            "pip",
            "install",
            "pip",
            "--upgrade",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python36",
            "-m",
            "pip",
            "install",
            "pip-tools",
            "--upgrade",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python36",
            *common_args,
            "-P",
            "Django>=2.2,<2.3",
            "-o",
            "py36-django22.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python36",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-o",
            "py36-django32.txt",
        ],
        check=True,
        capture_output=True,
    )

    # subprocess.run(["python37", "-m", "pip", "install", "pip", "--upgrade", ],
    #                check=True,
    #                capture_output=True,
    #                )
    # subprocess.run(["python37", "-m", "pip", "install", "pip-tools", "--upgrade", ],
    #                check=True,
    #                capture_output=True,
    #                )
    # subprocess.run(
    #     [
    #         "python37",
    #         *common_args,
    #         "-P",
    #         "Django>=2.2,<2.3",
    #         "-o",
    #         "py37-django22.txt",
    #     ],
    #     check=True,
    #     capture_output=True,
    # )
    # subprocess.run(
    #     [
    #         "python37",
    #         *common_args,
    #         "-P",
    #         "Django>=3.2a1,<3.3",
    #         "-o",
    #         "py37-django32.txt",
    #     ],
    #     check=True,
    #     capture_output=True,
    # )

    subprocess.run(
        [
            "python38",
            "-m",
            "pip",
            "install",
            "pip",
            "--upgrade",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python38",
            "-m",
            "pip",
            "install",
            "pip-tools",
            "--upgrade",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python38",
            *common_args,
            "-P",
            "Django>=2.2,<2.3",
            "-o",
            "py38-django22.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python38",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-o",
            "py38-django32.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python38",
            *common_args,
            "-P",
            "Django>=4.0a1,<4.1",
            "-o",
            "py38-django40.txt",
        ],
        check=True,
        capture_output=True,
    )

    # subprocess.run(["python39", "-m", "pip", "install", "pip", "--upgrade", ],
    #                check=True,
    #                capture_output=True,
    #                )
    # subprocess.run(["python39", "-m", "pip", "install", "pip-tools", "--upgrade", ],
    #                check=True,
    #                capture_output=True,
    #                )
    # subprocess.run(
    #     [
    #         "python39",
    #         *common_args,
    #         "-P",
    #         "Django>=2.2,<2.3",
    #         "-o",
    #         "py39-django22.txt",
    #     ],
    #     check=True,
    #     capture_output=True,
    # )
    # subprocess.run(
    #     [
    #         "python39",
    #         *common_args,
    #         "-P",
    #         "Django>=3.2a1,<3.3",
    #         "-o",
    #         "py39-django32.txt",
    #     ],
    #     check=True,
    #     capture_output=True,
    # )
    # subprocess.run(
    #     [
    #         "python39",
    #         *common_args,
    #         "-P",
    #         "Django>=4.0a1,<4.1",
    #         "-o",
    #         "py39-django40.txt",
    #     ],
    #     check=True,
    #     capture_output=True,
    # )

    # subprocess.run(["python310", "-m", "pip", "install", "pip", "--upgrade", ],
    #                check=True,
    #                capture_output=True,
    #                )
    # subprocess.run(["python310", "-m", "pip", "install", "pip-tools", "--upgrade", ],
    #                check=True,
    #                capture_output=True,
    #                )
    # subprocess.run(
    #     [
    #         "python310",
    #         *common_args,
    #         "-P",
    #         "Django>=3.2a1,<3.3",
    #         "-o",
    #         "py310-django32.txt",
    #     ],
    #     check=True,
    #     capture_output=True,
    # )
    # subprocess.run(
    #     [
    #         "python310",
    #         *common_args,
    #         "-P",
    #         "Django>=4.0a1,<4.1",
    #         "-o",
    #         "py310-django40.txt",
    #     ],
    #     check=True,
    #     capture_output=True,
    # )
