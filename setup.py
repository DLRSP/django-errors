import os
from distutils.cmd import Command
from distutils.command.build import build as _build

from setuptools.command.install_lib import install_lib as _install_lib

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


class CompileTranslations(Command):
    description = "compile message catalogs to MO files via django compilemessages"
    user_options = []  # type: list

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            from django.core.management import call_command
        except ModuleNotFoundError:
            return
        curdir = os.getcwd()
        os.chdir(
            os.path.realpath(
                os.path.join("src", os.path.basename(list(os.walk("src"))[1][0]))
            )
        )
        call_command("compilemessages")
        os.chdir(curdir)


class Build(_build):
    sub_commands = [] + _build.sub_commands
    if os.path.isdir(
        os.path.realpath(
            os.path.join("src", os.path.basename(list(os.walk("src"))[1][0]), "locale")
        )
    ):
        sub_commands = [("compile_translations", None)] + _build.sub_commands


class InstallLib(_install_lib):
    def run(self):
        _install_lib.run(self)


setup(
    cmdclass={
        "build": Build,
        "install_lib": InstallLib,
        "compile_translations": CompileTranslations,
    },
)
