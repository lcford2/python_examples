import PyQt5.QtCore as core
import PyQt5.QtGui as gui
import PyQt5.QtWidgets as widgets
import sys
import os
import ctypes
import platform
from IPython import embed as II

from econ_ui import Ui_econ_ui
from econ_for_gui import gui_run, EconCalcs, effectivei


class MyMainScreen(widgets.QDialog):
    def __init__(self, parent=None):
        widgets.QDialog.__init__(self, parent)
        self.ui = Ui_econ_ui()
        self.ui.setupUi(self)
        self.ui.eff_rate_box.hide()
        self.ui.eff_calc_box.hide()
        self.ui.answer_label.setText("Answer equals ($):")

        self.input_info = {'know': '0', 'find': '0', 'amount': '0',
                           'periods': '0', 'rate_type': '0', 'effective': '0'}

        self.econ_calcs = EconCalcs(0, 0, 0, 0, 0)

        self.ui.find_combo.currentIndexChanged.connect(self.find_combo_change)
        self.ui.know_combo.currentIndexChanged.connect(self.know_combo_change)
        self.ui.know_combo.currentIndexChanged.connect(self.change_label)
        self.ui.know_combo.currentIndexChanged.connect(self.error_check)
        self.ui.find_combo.currentIndexChanged.connect(self.error_check)
        self.ui.amount_edit.cursorPositionChanged.connect(self.select_text)
        self.ui.period_edit.cursorPositionChanged.connect(self.select_text)
        self.ui.effective_radio.toggled.connect(self.rate_radio_change)
        self.ui.nominal_radio.toggled.connect(self.rate_radio_change)
        self.ui.nominal_rate_edit.textEdited.connect(self.effective_calc)
        self.ui.eff_period_edit.textEdited.connect(self.effective_calc)
        self.ui.buttonBox.accepted.connect(self.get_info)
        self.ui.output_info_box.setFontItalic(True)
        text_color = gui.QColor(255, 0, 0)
        self.ui.output_info_box.setTextColor(text_color)

    def know_combo_change(self):
        index = self.ui.know_combo.currentIndex()
        self.input_info['know'] = str(index)

    def error_check(self):
        know_index = self.ui.know_combo.currentIndex()
        find_index = self.ui.find_combo.currentIndex()
        if know_index == find_index:
            message = 'That is not a valid selection. The "Find" drop down box and "Know" drop down box cannot be the same. Please change one.'
            self.ui.output_info_box.append(message)
        else:
            self.ui.output_info_box.clear()
        if find_index == 4:
            if know_index in [0, 2]:
                self.ui.output_info_box.clear()
            if know_index in [1, 3]:
                message = 'That is not a valid capital costs calculation. Please select either "Annual Worth" or "Present Worth" from the "What do you know?" drop down box.'
                self.ui.output_info_box.append(message)

    def select_text(self):
        sender = self.sender()
        sender_name = sender.objectName()
        if sender_name == 'amount_edit':
            text = self.ui.amount_edit.text()
            if text == 'Enter a number':
                self.ui.amount_edit.selectAll()
        elif sender_name == 'period_edit':
            text = self.ui.period_edit.text()
            if text == 'Enter a number':
                self.ui.period_edit.selectAll()

    def change_label(self):
        label = self.ui.amount_label
        know_index = self.ui.know_combo.currentIndex()
        label_map = {"0": "Enter the present worth:",
                     "1": "Enter for future worth:",
                     "2": "Enter the annual worth:",
                     "3": "Enter the gradient amount:"}
        new_label = label_map.get(str(know_index), "Error")
        label.setText(new_label)

    def find_combo_change(self):
        index = self.ui.find_combo.currentIndex()
        self.input_info['find'] = str(index)

    def rate_radio_change(self):
        if self.ui.effective_radio.isChecked() == True:
            self.input_info['rate_type'] = 'effective'
            self.ui.eff_calc_box.hide()
            self.ui.eff_rate_box.show()
        elif self.ui.nominal_radio.isChecked() == True:
            self.input_info['rate_type'] = 'nominal'
            self.ui.eff_calc_box.show()
            self.ui.eff_rate_box.hide()

    def get_info(self):
        amount = self.ui.amount_edit.text()
        amount = amount.replace(',', '')
        periods = self.ui.period_edit.text()
        if self.input_info['rate_type'] == 'effective':
            self.input_info['effective'] = self.ui.rate_edit.text()
        elif self.input_info['rate_type'] == 'nominal':
            self.input_info['effective'] = self.ui.eff_rate_edit.text()
        self.input_info['amount'] = str(amount)
        self.input_info['periods'] = str(periods)
        self.calc_values()

    def effective_calc(self):
        m = self.ui.eff_period_edit.text()
        r = self.ui.nominal_rate_edit.text()
        effective_rate = '0'
        try:
            r = float(r)
            m = float(m)
            effective_rate = effectivei(r, m)
            self.ui.eff_rate_edit.setText(f"{effective_rate: .4f}")
        except:
            pass

    def calc_values(self):
        have = 0
        find = 0
        find_map = {"0": "P", "1": "F", "2": "A", "3": "G", "4": "C"}
        have_map = {"0": "P", "1": "F", "2": "A", "3": "G"}
        find = find_map[self.input_info["find"]]
        have = have_map[self.input_info["know"]]
        amount = float(self.input_info['amount'])
        if find == 'C':
            periods = 0
        else:
            periods = float(self.input_info['periods'])
        rate = float(self.input_info['effective'])
        self.econ_calcs.update_input(find, have, amount, periods, rate)
        result = self.econ_calcs.get_solution
        # result = gui_run(find, have, amount, periods, rate)
        self.ui.answer_edit.setText(f'{result:,.2f}')


if __name__ == "__main__":
    app = widgets.QApplication(sys.argv)
    screen_res = app.desktop().screenGeometry()
    mainscreen = MyMainScreen()
    # Icon made by "https://www.flaticon.com/authors/surang"
    app.setWindowIcon(gui.QIcon('cost.png'))
    mainscreen.show()
    app.exec_()
