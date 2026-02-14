# eztk

A simplified Tkinter widget framework with a grid layout engine.

eztk wraps Tkinter's widget creation and grid placement into a compact API. It provides:

- **TkWidgetDef** — a unified wrapper for any Tkinter widget, tracking position, data, and parent/child relationships
- **EasyTk** — the root application class
- **Notebook** — a lightweight replacement for `ttk.Notebook`
- **Grid layout constants** — `NEXT_ROW`, `SAME_COL`, `EXTEND_ROW`, etc. for declarative widget placement

## Install

```bash
pip install eztk
```

Image features (thumbnails, OpenCV display) require additional dependencies:

```bash
pip install eztk[images]
```

## Quick start

```python
from eztk import eztk

app = eztk.EasyTk()
app.add_label(text="Hello, world!")
app.add_button("Click me", lambda: print("clicked"))
app.tkw.mainloop()
```
