#ifndef CUSTOM_WIDGET_H
#define CUSTOM_WIDGET_H

#include <QWidget>
#include "editor_export.h"
#include <QEvent>
#include <QObject>

namespace KEditorExample {
class KEditorViewP;

class EDITOR_EXPORT KEditorView: public QWidget
{
    Q_OBJECT
public:
    KEditorView();
    ~KEditorView();

protected:
    // For keyboard presses event handling
    bool event(QEvent* e);

private:
    KEditorViewP* d;

};


}; // namespace KEditorExample


#endif
