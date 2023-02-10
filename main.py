from bs4 import BeautifulSoup
from pprint import pprint

import requests
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem

from UI_files.MainWindow import Ui_MainWindow
from UI_files.FilesContentDialogue import Ui_Dialog

def api_request(customerregion=66, perpage=1, productsearch=None):
    payloads_ = {f'customerregion': customerregion, 'perpage': perpage,
                 'currentstage': 'EC', 'sort': '-signDate', 'fz': 44}
    response = requests.get(f"http://openapi.clearspending.ru/restapi/v3/contracts/search/?productsearch={productsearch}",
                            params=payloads_)
    l = list(response.json()['contracts']['data'])

    return l

def contact_info(print_form):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
        response = requests.get(print_form, headers=headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        parsed = soup.find(string='Телефон (электронная почта)').parent.parent.parent
        phone_mail = parsed.select('tr:nth-child(4) > td:nth-child(12)')[0]
        adress = parsed.select('tr:nth-child(4) > td:nth-child(5)')[0]

        return [phone_mail.next, phone_mail.next.next.next.text.split()[-1], adress.getText()]
    except: return ['-','-','-']

class FilesContentDialogue(QtWidgets.QDialog):
    def __init__(self):
        super(FilesContentDialogue, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def fill_table(self, files_list):
        tw = self.ui.tableWidget
        if not files_list:
            tw.setRowCount(0)
        else:
            for number, item in enumerate(files_list):
                tw.setRowCount(number+1)

                tw.setItem(number, 0, QTableWidgetItem(item['docDescription']))
                tw.setItem(number, 1, QTableWidgetItem(item['url']))

    def fill_table_with_products(self, products_list):
        tw = self.ui.tableWidget
        if not products_list:
            tw.setRowCount(0)
        else:
            for number, item in enumerate(products_list):
                tw.setRowCount(number+1)

                tw.setItem(number, 0, QTableWidgetItem(item['name']))
                tw.setItem(number, 1, QTableWidgetItem(str(item['price'])))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_search_clicked)
        self.ui.pushButton_3.clicked.connect(self.on_files_to_download_clicked)
        self.ui.pushButton_2.clicked.connect(self.on_products_in_contract_clicked)
        self.ui.tableWidget.setColumnHidden(6, True)
        self.ui.comboBox.addItems(['66','77',''])

    def fill_table(self, dealers_list):
        tw = self.ui.tableWidget
        if not dealers_list:
            tw.setRowCount(0)
        else:
            for number, item in enumerate(dealers_list):
                tw.setRowCount(number+1)
                cont_inf = contact_info(item.get('printFormUrl', '-'))

                tw.setItem(number, 0, QTableWidgetItem(item['suppliers'][0].get('organizationName', '-')))
                tw.setItem(number, 1, QTableWidgetItem(cont_inf[0]))
                tw.setItem(number, 2, QTableWidgetItem(cont_inf[1]))
                tw.setItem(number, 3, QTableWidgetItem(cont_inf[2]))
                tw.setItem(number, 4, QTableWidgetItem(item['suppliers'][0].get('inn', '-')))
                tw.setItem(number, 5, QTableWidgetItem(item.get('printFormUrl', '-')))
                tw.setItem(number, 6, QTableWidgetItem(str(number)))

    def on_search_clicked(self):
        self.finded_dealers_info_list = api_request(productsearch=self.ui.lineEdit.text(),
                                                    perpage=self.ui.spinBox.value(),
                                                    customerregion=self.ui.comboBox.currentText())
        self.fill_table(self.finded_dealers_info_list)

    def on_files_to_download_clicked(self):
        chosen_item = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 6).text()
        # print(self.finded_dealers_info_list[chosen_item])
        fcd.fill_table(self.finded_dealers_info_list[int(chosen_item)]['scan'])

        fcd.show()

    def on_products_in_contract_clicked(self):
        chosen_item = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 6).text()
        fcd.fill_table_with_products(self.finded_dealers_info_list[int(chosen_item)]['products'])

        fcd.show()

app = QApplication(sys.argv)
ex = MainWindow()
fcd = FilesContentDialogue()
ex.show()
sys.exit(app.exec_())