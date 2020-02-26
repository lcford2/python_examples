### Using PyQt5 to create a simple GUI for Engineering Economics Calculations

`PyQt5` is an easy to use API that provides access to the C++ Qt library. This allows users to write GUI logic in Python without having to lower-level implementation details. 

In this example, I created `econ_ui.ui` using Qt Designer, an application that allows users to easily setup how their GUI will look. `econ_ui.py` is the result of calling `pyuic`, a package that converts `.ui` files to `.py` files, on `econ_ui.ui`. `econ_gui.py` imports the ui Python file and then contains the logic for how users interact with the interface. `econ_for_gui.py` contains the engineering economic calculations that can be invoked from the interface. 

To install all the requisite packages, use `conda env create -f environment.yml`.

To run the GUI, use the command `python econ_gui.py` from within the environment created by the step above. 