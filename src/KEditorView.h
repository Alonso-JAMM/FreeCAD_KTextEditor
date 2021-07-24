#ifndef CUSTOM_WIDGET_H
#define CUSTOM_WIDGET_H

#include <QWidget>
#include "editor_export.h"
#include <QEvent>
#include <QObject>
#include <QUrl>

namespace KEditor {
class KEditorViewP;

class KEDITORVIEW_EXPORT KEditorView: public QWidget
{
    Q_OBJECT
public:
    KEditorView();
    ~KEditorView();

    void openUrl(const QUrl &url);

    void confidDialog(QWidget* parent);

protected:
    // For keyboard presses event handling
    bool event(QEvent* e);

private:
    KEditorViewP* d;

};


}; // namespace KEditor


#endif
