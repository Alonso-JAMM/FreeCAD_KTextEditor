import os
import pathlib
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext


# https://stackoverflow.com/questions/42585210/extending-setuptools-extension-to-use-cmake-in-setup-py
class CMakeExtension(Extension):
    def __init__(self, name):
        # don't invoke the original build_ext for this special extension
        super().__init__(name, sources=[])


class build_ext(_build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_cmake(ext)
#         super().run()

    def build_cmake(self, ext):
        cwd = pathlib.Path().absolute()

        # make sure the dirs exists
        # TODO clean this part so that we build the shared libraries in the
        # correct directory and being able to install them in the correct
        # directory
        build_tmp = pathlib.Path(self.build_temp)
        build_tmp.mkdir(parents=True, exist_ok=True)
        extdir = pathlib.Path(self.get_ext_fullpath(ext.name))
        extdir.parent.mkdir(parents=True, exist_ok=True)

        output_directory = str(extdir.parent.absolute()) + "/" + ext.name

        cmake_args = [
            "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=" + output_directory,
            "-DCMAKE_BUILD_TYPE=Release"
        ]
        build_args = [
            "--config", "Release",
            "--", "-j6"
        ]

        os.chdir(str(build_tmp))
        self.spawn(["cmake", str(cwd)] + cmake_args)
        self.spawn(["cmake", "--build", "."] + build_args)

        os.chdir(str(cwd))


setup(
    name="KEditor",
    version="0.1.0",
    packages=[
        "KEditorView",
        "freecad",
        "freecad.KEditor",
    ],
    package_dir={
        "KEditorView": "src",
    },
    description="Embedded KTextEditor for FreeCAD",
    include_package_data=True,
    zip_safe=False,
    ext_modules=[CMakeExtension("KEditorView")],
    cmdclass={
        "build_ext": build_ext,
    }
)
