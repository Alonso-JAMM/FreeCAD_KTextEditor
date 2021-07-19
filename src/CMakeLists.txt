 
set(KEDITOR_SRCS
    KEditorView.cpp
)

include_directories(
    ${Qt5Core_INCLUDE_DIRS}
    ${Qt5Widgets_INCLUDE_DIRS}
)



add_library(libkeditor SHARED ${KEDITOR_SRCS})

target_link_libraries(libkeditor KF5::TextEditor)

set_property(TARGET libkeditor PROPERTY PREFIX "")
