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

