#include "KEditorView.h"
#include <QGridLayout>
#include <QKeyEvent>
#include <KTextEditor/Document>
#include <KTextEditor/Editor>
#include <KTextEditor/View>

namespace KEditor {
class KEditorViewP {
public:
    KTextEditor::Document *doc;
    KTextEditor::View *view;
};


KEditorView::KEditorView()
    : QWidget()
{
    d = new KEditorViewP;
    KTextEditor::Editor *editor = KTextEditor::Editor::instance();
    QGridLayout* layout = new QGridLayout(this);
    d->doc = editor->createDocument(this);
    d->view = d->doc->createView(this);
    layout->addWidget(d->view, 0, 0);
}


KEditorView::~KEditorView() {
    delete d->view;
    delete d->doc;
    delete d;
}

void KEditorView::openUrl(const QUrl &url)
{
    d->doc->openUrl(url);
}

bool KEditorView::event(QEvent* e)
{
    // HACK: when keys are pressed QEvent::ShortcutOverride is emitted. If we
    // accept all the key events except for the modifiers and other special keys,
    // then text will be added to the text field and shortcuts (like Ctrl+A or Ctrl+S)
    // will also be enabled.
    if (e->type() == QEvent::ShortcutOverride)
    {
        QKeyEvent *ke = static_cast<QKeyEvent *>(e);
        int key = ke->key();
        // no modifiers and other special keys
        if (!ke->modifiers() & (key != Qt::Key_Backspace) & (key != Qt::Key_Insert)
            & (key != Qt::Key_Delete) & (key != Qt::Key_Home) & (key != Qt::Key_End)
            & (key != Qt::Key_Left) & (key != Qt::Key_Up) & (key != Qt::Key_Right)
            & (key != Qt::Key_Down) & (key != Qt::Key_PageUp) & (key != Qt::Key_PageDown))
        {
            e->accept();
        }
    }

    return QWidget::event(e);

}

}
