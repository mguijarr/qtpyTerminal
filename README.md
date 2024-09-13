# qtpyTerminal
A Vt100 terminal widget for qtpy (PyQt, Pyside)

# About

qtpyTerminal is a QWidget derived from QPlainTextEdit, which can execute an interactive
command to run in the default shell (`SHELL` environment variable). The shell process
is forked, and input/output is redirected to the Qt widget. It is then possible to
interact with the program, as in a VT100 terminal thanks to the use of Pyte for
escape codes interpretation (see ).

# Installation

qtpyTerminal only requires pyte and qtpy - it should run seamlessly with different
Python Qt backends like PyQt or Pyside.

Clone the repository, and from the source directory:

`pip install .`

(to have it installed in the current Python environment).

# Example

```python
import sys
from qtpy import QtGui, QtWidgets
from qtpyTerminal import qtpyTerminal

# Create the Qt application and console.
app = QtWidgets.QApplication([])
mainwin = QtWidgets.QMainWindow()
mainwin.setWindowTitle("qtpyTerminal example")
container = QtWidgets.QWidget(mainwin)
container.setLayout(QtWidgets.QVBoxLayout())
mainwin.setCentralWidget(container)

console = qtpyTerminal(mainwin)

def exit():
  console.stop()
  app.quit()

start_button = QtWidgets.QPushButton("Start shell", container)
start_button.clicked.connect(console.start)
container.layout().addWidget(start_button)
container.layout().addWidget(console)
quit_button = QtWidgets.QPushButton("Quit", container)
quit_button.clicked.connect(exit)
container.layout().addWidget(quit_button)

# Show widget and launch Qt's event loop.
mainwin.show()
sys.exit(app.exec_())

```

By default the process started by the terminal is defined by the `SHELL` environment variable.
It is possible to call `.set_cmd()` to launch another command - for example `.set_cmd("python")`
will start an interactive session of the Python interpreter in the Terminal widget.

The widget size policy is `MinimumExpanding` on both directions. Vertical scrolling is handled.
Please note that horizontal scrolling is not implemented yet. So, it is better to define a fixed
number of columns. By default the terminal is 132 columns.

The number of columns or default number of rows can be defined with `.set_cols()` or `.set_rows()`.
It is also possible to give them directly as arguments of `qtpyTerminal` constructor.

By default, the widgets uses "text" color (`QPalette`) for the main foreground color, and "base"
color for the background. It can be changed by calling `set_fgcolor(QColor)` or `set_bgcolor(QColor)`
respectively.

# Contributing

Contributions are welcome. Please submit merge requests. 
