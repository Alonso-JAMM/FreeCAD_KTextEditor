cmake_minimum_required(VERSION 3.10)

#set the project name
project(KEditorView)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 17)

find_package(Shiboken2 REQUIRED)
find_package(PySide2 REQUIRED)
find_package(Qt5Core REQUIRED)
find_package(Qt5Widgets REQUIRED)
find_package(KF5TextEditor REQUIRED)

set(CMAKE_AUTOMOC ON)

# used information from these sources:
# https://gitlab.kitware.com/cmake/community/-/wikis/doc/cmake/RPATH-handling
# https://code.qt.io/cgit/pyside/pyside-setup.git/tree/examples/samplebinding/CMakeLists.txt?h=5.15.2
# make it so that the binary file can find the shared library
# I think this makes it so that the binary looks for its current directory
set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH FALSE)
set(CMAKE_INSTALL_RPATH ${CMAKE_INSTALL_PREFIX})
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)


add_subdirectory(src)
add_subdirectory(python)

