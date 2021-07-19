#ifndef BINDINGS_H
#define BINDINGS_H

// Make "signals:", "slots:" visible as access specifiers
#define QT_ANNOTATE_ACCESS_SPECIFIER(a) __attribute__((annotate(#a)))


#include <src/KEditorView.h>

#endif
