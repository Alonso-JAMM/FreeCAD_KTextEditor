 
set(KEDITOR_SRCS
    KEditor.cpp
)

include_directories(
    ${Qt5Core_INCLUDE_DIRS}
    ${Qt5Widgets_INCLUDE_DIRS}
)



add_library(keditor SHARED ${KEDITOR_SRCS})

target_link_libraries(keditor KF5::TextEditor)

set_property(TARGET keditor PROPERTY PREFIX "")
