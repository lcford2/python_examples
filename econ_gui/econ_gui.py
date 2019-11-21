import PyQt5.QtCore as core
import PyQt5.QtGui as gui
import PyQt5.QtWidgets as widgets
import sys
import os
import ctypes

from econ_ui import Ui_econ_ui
from econ_for_gui import gui_run, effectivei

input_info = {'know': '0', 'find': '0', 'amount': '0',
              'periods': '0', 'rate_type': '0', 'effective': '0'}


class MyMainScreen(widgets.QDialog):
    def __init__(self, parent=None):
        widgets.QDialog.__init__(self, parent)
        self.ui = Ui_econ_ui()
        self.ui.setupUi(self)
        self.ui.eff_rate_box.hide()
        self.ui.eff_calc_box.hide()

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
        global input_info
        index = self.ui.know_combo.currentIndex()
        input_info['know'] = str(index)

    def error_check(self):
        global input_info
        know_index = self.ui.know_combo.currentIndex()
        find_index = self.ui.find_combo.currentIndex()
        if know_index == find_index:
            message = 'That is not a valid selection. The "Find" drop down box and "Know" drop down box cannot be the same. Please change one.'
            self.ui.output_info_box.append(message)
        else:
            self.ui.output_info_box.clear()
        if find_index == 4:
            if know_index == 0:
                self.ui.output_info_box.clear()
            if know_index == 1:
                #cur_mes = unicode(self.ui.output_info_box.text()).encode('utf_8')
                message = 'That is not a valid capital costs calculation. Please select either "Annual Worth" or "Present Worth" from the "What do you know?" drop down box.'
                self.ui.output_info_box.append(message)
            if know_index == 2:
                self.ui.output_info_box.clear()
            if know_index == 3:
                #cur_mes = unicode(self.ui.output_info_box.text()).encode('utf_8')
                message = 'That is not a valid capital costs calculation. Please select either "Annual Worth" or "Present Worth" from the "What do you know?" drop down box.'
                self.ui.output_info_box.append(message)

    def select_text(self):
        sender = self.sender()
        sender_name = sender.objectName()
        if sender_name == 'amount_edit':
            text = unicode(self.ui.amount_edit.text()).encode('utf_8')
            if text == 'Enter a number':
                self.ui.amount_edit.selectAll()
        elif sender_name == 'period_edit':
            text = unicode(self.ui.period_edit.text()).encode('utf_8')
            if text == 'Enter a number':
                self.ui.period_edit.selectAll()

    def change_label(self):
        label = self.ui.amount_label
        know_index = self.ui.know_combo.currentIndex()
        new_label = "Enter the present worth:"
        if str(know_index) == '0':
            new_label = "Enter the present worth:"
        elif str(know_index) == '1':
            new_label = "Enter the future worth:"
        elif str(know_index) == '2':
            new_label = "Enter the annual worth:"
        elif str(know_index) == '3':
            new_label = "Enter the gradient amount:"
        label.setText(new_label)

    def find_combo_change(self):
        global input_info
        index = self.ui.find_combo.currentIndex()
        input_info['find'] = str(index)

    def rate_radio_change(self):
        global input_info
        if self.ui.effective_radio.isChecked() == True:
            input_info['rate_type'] = 'effective'
            self.ui.eff_calc_box.hide()
            self.ui.eff_rate_box.show()
        elif self.ui.nominal_radio.isChecked() == True:
            input_info['rate_type'] = 'nominal'
            self.ui.eff_calc_box.show()
            self.ui.eff_rate_box.hide()

    def get_info(self):
        global input_info
        amount = unicode(self.ui.amount_edit.text()).encode('utf_8')
        amount = amount.replace(',', '')
        periods = unicode(self.ui.period_edit.text()).encode('utf_8')
        if input_info['rate_type'] == 'effective':
            input_info['effective'] = unicode(
                self.ui.rate_edit.text()).encode('utf_8')
        elif input_info['rate_type'] == 'nominal':
            input_info['effective'] = unicode(
                self.ui.eff_rate_edit.text()).encode('utf_8')
        input_info['amount'] = str(amount)
        input_info['periods'] = str(periods)
        self.calc_values()

    def effective_calc(self):
        m = unicode(self.ui.eff_period_edit.text()).encode('utf_8')
        r = unicode(self.ui.nominal_rate_edit.text()).encode('utf_8')
        effective_rate = '0'
        try:
            r = float(r)
            m = float(m)
            effective_rate = effectivei(r, m)
            self.ui.eff_rate_edit.setText(str(effective_rate))
        except:
            pass

    def calc_values(self):
        global input_info
        have = 0
        find = 0
        if input_info['find'] == '0':
            find = 'P'
        elif input_info['find'] == '1':
            find = 'F'
        elif input_info['find'] == '2':
            find = 'A'
        elif input_info['find'] == '3':
            find = 'G'
        elif input_info['find'] == '4':
            find = 'C'
        if input_info['know'] == '0':
            have = 'P'
        elif input_info['know'] == '1':
            have = 'F'
        elif input_info['know'] == '2':
            have = 'A'
        elif input_info['know'] == '3':
            have = 'G'
        amount = float(input_info['amount'])
        periods = float(input_info['periods'])
        rate = float(input_info['effective'])
        result = gui_run(find, have, amount, periods, rate)
        self.ui.answer_edit.setText('{:,}'.format(result))


if __name__ == "__main__":
    app = widgets.QApplication(sys.argv)
    screen_res = app.desktop().screenGeometry()
    mainscreen = MyMainScreen()
    app.setWindowIcon(gui.QIcon('slack.svg'))
    myappid = 'slack.svg'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    mainscreen.show()
    app.exec_()
