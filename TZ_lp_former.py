import tkinter
from tkinter import *
from tkinter import ttk
from docx import Document
import requests
from bs4 import BeautifulSoup
import xmlschema
import re
import zipfile
import os
from tkinter import messagebox
from docx.enum.section import WD_ORIENT
from docx.shared import Mm
icon = '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'
xsd_sheme = '''<?xml version="1.0" encoding="UTF-8"?>
<!-- ESKLP_interchangeability data types, version 21.5, create date 28.02.2020  -->
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns="http://service.rosminzdrav.ru/ESKLP_interchangeability" xmlns:xsd="undefined" targetNamespace="http://service.rosminzdrav.ru/ESKLP_interchangeability">
	<xs:element name="ESKLP_interchangeability">
		<xs:annotation>
			<xs:documentation>Структура групп взаимозаменяемых лекарственных препаратов ЕСКЛП</xs:documentation>
		</xs:annotation>
		<xs:complexType>
			<xs:sequence>
				<xs:element ref="group_list">
					<xs:annotation>
						<xs:documentation>Список групп взаимозаменяемых ЛП</xs:documentation>
					</xs:annotation>
				</xs:element>
			</xs:sequence>
			<xs:attribute name="UUID" type="uuidType" use="required">
				<xs:annotation>
					<xs:documentation>Уникальный идентификатор выгрузки</xs:documentation>
				</xs:annotation>
			</xs:attribute>
			<xs:attribute name="date_create" type="xs:dateTime" use="required">
				<xs:annotation>
					<xs:documentation>Дата-время создания выгрузки</xs:documentation>
				</xs:annotation>
			</xs:attribute>
			<xs:attribute name="schemaVersion" type="SmallNameType" use="required">
				<xs:annotation>
					<xs:documentation>Номер версии схемы, которой соответствуют данные</xs:documentation>
				</xs:annotation>
			</xs:attribute>
			<xs:attribute name="fullEsklpUUID" type="uuidType" use="required">
				<xs:annotation>
					<xs:documentation>Ссылка на полную выгрузку ЕСКЛП, на данных которой составлена выгрузка по взаимозаменяемости</xs:documentation>
				</xs:annotation>
			</xs:attribute>
			<xs:attribute name="incrementEsklpUUID" type="uuidType" use="optional">
				<xs:annotation>
					<xs:documentation>Ссылка на инкрементальную выгрузку, на данных которой составлена выгрузка по взаимозаменяемости</xs:documentation>
				</xs:annotation>
			</xs:attribute>
		</xs:complexType>
	</xs:element>
	<xs:element name="group">
		<xs:annotation>
			<xs:documentation>Группа взаимозаменяемости</xs:documentation>
		</xs:annotation>
		<xs:complexType>
			<xs:sequence>
				<xs:element name="group_price_list" minOccurs="0">
					<xs:annotation>
						<xs:documentation>Референтные цены на группу (обязательная для групп первого уровня)</xs:documentation>
					</xs:annotation>
					<xs:complexType>
						<xs:sequence>
							<xs:element name="group_price" maxOccurs="unbounded">
								<xs:annotation>
									<xs:documentation>Референтная цена на группу</xs:documentation>
								</xs:annotation>
								<xs:complexType>
									<xs:sequence>
										<xs:element name="value">
											<xs:annotation>
												<xs:documentation>Значение референтной цены (рублей) за единицу измерения группы </xs:documentation>
											</xs:annotation>
											<xs:simpleType>
												<xs:restriction base="xs:decimal">
													<xs:totalDigits value="20"/>
													<xs:fractionDigits value="10"/>
												</xs:restriction>
											</xs:simpleType>
										</xs:element>
										<xs:element name="usage_min" minOccurs="0">
											<xs:annotation>
												<xs:documentation>Минимальное количество закупаемых единиц ЛП в ЕИ группы, для которых применима данная цена</xs:documentation>
											</xs:annotation>
											<xs:simpleType>
												<xs:restriction base="xs:decimal">
													<xs:totalDigits value="30"/>
													<xs:fractionDigits value="10"/>
												</xs:restriction>
											</xs:simpleType>
										</xs:element>
										<xs:element name="usage_max" minOccurs="0">
											<xs:annotation>
												<xs:documentation>Максимальное количество закупаемых единиц ЛП в ЕИ группы, для которых применима данная цена</xs:documentation>
											</xs:annotation>
											<xs:simpleType>
												<xs:restriction base="xs:decimal">
													<xs:totalDigits value="30"/>
													<xs:fractionDigits value="10"/>
												</xs:restriction>
											</xs:simpleType>
										</xs:element>
										<xs:element name="price_type" type="xs:int">
											<xs:annotation>
												<xs:documentation>Тип цены</xs:documentation>
											</xs:annotation>
										</xs:element>
										<xs:element name="date_create" type="xs:dateTime">
											<xs:annotation>
												<xs:documentation>Дата расчета цены</xs:documentation>
											</xs:annotation>
										</xs:element>
										<xs:element name="date_start" type="xs:dateTime">
											<xs:annotation>
												<xs:documentation>Дата начала действия цены</xs:documentation>
											</xs:annotation>
										</xs:element>
										<xs:element name="date_end" type="xs:dateTime" minOccurs="0">
											<xs:annotation>
												<xs:documentation>Дата окончания действия цены</xs:documentation>
											</xs:annotation>
										</xs:element>
									</xs:sequence>
								</xs:complexType>
							</xs:element>
						</xs:sequence>
					</xs:complexType>
				</xs:element>
				<xs:element name="unit" form="qualified" minOccurs="0">
					<xs:annotation>
						<xs:documentation>Единица измерения группы (обязательна для групп первого уровня)</xs:documentation>
					</xs:annotation>
					<xs:complexType>
						<xs:sequence>
							<xs:element name="name" type="BigNameType">
								<xs:annotation>
									<xs:documentation>Название единицы измерения группы</xs:documentation>
								</xs:annotation>
							</xs:element>
							<xs:element name="okei_code" form="qualified">
								<xs:annotation>
									<xs:documentation>Код ОКЕИ. При отсутствии возможности сопоставить значение с ОКЕИ передается 876</xs:documentation>
								</xs:annotation>
								<xs:simpleType>
									<xs:restriction base="xs:string">
										<xs:pattern value="\d{3,4}"/>
									</xs:restriction>
								</xs:simpleType>
							</xs:element>
							<xs:element name="okei_name" type="BigNameType" form="qualified">
								<xs:annotation>
									<xs:documentation>Название единицы ОКЕИ. При отсутствии возможности сопоставить значение с ОКЕИ передается "Условная единица"</xs:documentation>
								</xs:annotation>
							</xs:element>
						</xs:sequence>
					</xs:complexType>
				</xs:element>
				<xs:element name="element_list" minOccurs="0">
					<xs:annotation>
						<xs:documentation>Список элементов </xs:documentation>
					</xs:annotation>
					<xs:complexType>
						<xs:sequence>
							<xs:element name="element" maxOccurs="unbounded">
								<xs:complexType>
									<xs:attribute name="ID" type="xs:int" use="required">
										<xs:annotation>
											<xs:documentation>Идентификатор</xs:documentation>
										</xs:annotation>
									</xs:attribute>
									<xs:attribute name="date_create" type="xs:dateTime" use="required">
										<xs:annotation>
											<xs:documentation>Дата-время создания</xs:documentation>
										</xs:annotation>
									</xs:attribute>
									<xs:attribute name="date_change" type="xs:dateTime" use="required">
										<xs:annotation>
											<xs:documentation>Дата-время изменения</xs:documentation>
										</xs:annotation>
									</xs:attribute>
									<xs:attribute name="date_end" type="xs:dateTime" use="optional">
										<xs:annotation>
											<xs:documentation>Дата-время окончания действия записи</xs:documentation>
										</xs:annotation>
									</xs:attribute>
									<xs:attribute name="is_active" type="xs:boolean" use="required">
										<xs:annotation>
											<xs:documentation>Признак активности элемента</xs:documentation>
										</xs:annotation>
									</xs:attribute>
									<xs:attribute name="rate_value" type="xs:decimal" use="required">
										<xs:annotation>
											<xs:documentation>Коэффициент приведения </xs:documentation>
										</xs:annotation>
									</xs:attribute>
									<xs:attribute name="pack_requirement" type="HugeNameType" use="optional">
										<xs:annotation>
											<xs:documentation>Требование к содержимому упаковки ЛП</xs:documentation>
										</xs:annotation>
									</xs:attribute>
									<xs:attribute name="SMNN_UUID" type="uuidType" use="optional">
										<xs:annotation>
											<xs:documentation>Уникальный системный идентификатор записи СМНН</xs:documentation>
										</xs:annotation>
									</xs:attribute>
								</xs:complexType>
							</xs:element>
						</xs:sequence>
					</xs:complexType>
				</xs:element>
				<xs:element ref="group_list" minOccurs="0">
					<xs:annotation>
						<xs:documentation>Cписок дочерних групп взаимозаменяемости</xs:documentation>
					</xs:annotation>
				</xs:element>
			</xs:sequence>
			<xs:attribute name="name" type="HugeNameType" use="required">
				<xs:annotation>
					<xs:documentation>Наименование</xs:documentation>
				</xs:annotation>
			</xs:attribute>
			<xs:attribute name="ID" type="xs:int" use="required">
				<xs:annotation>
					<xs:documentation>Идентификатор</xs:documentation>
				</xs:annotation>
			</xs:attribute>
			<xs:attribute name="version" type="xs:int" use="optional">
				<xs:annotation>
					<xs:documentation>Версия головной группы (заполняется для групп первого уровня)</xs:documentation>
				</xs:annotation>
			</xs:attribute>
			<xs:attribute name="ancestor_ID" type="xs:int" use="optional">
				<xs:annotation>
					<xs:documentation>Ссылка на предшествующую версию головной группы (заполняется для групп первого уровня)</xs:documentation>
				</xs:annotation>
			</xs:attribute>
			<xs:attribute name="date_create" type="xs:dateTime" use="required">
				<xs:annotation>
					<xs:documentation>Дата-время создания</xs:documentation>
				</xs:annotation>
			</xs:attribute>
			<xs:attribute name="date_change" type="xs:dateTime" use="required">
				<xs:annotation>
					<xs:documentation>Дата-время изменения</xs:documentation>
				</xs:annotation>
			</xs:attribute>
			<xs:attribute name="date_end" type="xs:dateTime" use="optional">
				<xs:annotation>
					<xs:documentation>Дата-время окончания действия записи</xs:documentation>
				</xs:annotation>
			</xs:attribute>
			<xs:attribute name="level" type="xs:int" use="required">
				<xs:annotation>
					<xs:documentation>Уровень группы</xs:documentation>
				</xs:annotation>
			</xs:attribute>
			<xs:attribute name="is_active" type="xs:boolean" use="required">
				<xs:annotation>
					<xs:documentation>Признак активности группы</xs:documentation>
				</xs:annotation>
			</xs:attribute>
			<xs:attribute name="hash" type="hashType" use="required">
				<xs:annotation>
					<xs:documentation>Контрольная сумма версии записи группы</xs:documentation>
				</xs:annotation>
			</xs:attribute>
		</xs:complexType>
	</xs:element>
	<xs:element name="group_list">
		<xs:annotation>
			<xs:documentation>Список групп взаимозаменяемости</xs:documentation>
		</xs:annotation>
		<xs:complexType>
			<xs:sequence>
				<xs:element ref="group" maxOccurs="unbounded">
					<xs:annotation>
						<xs:documentation>Группа взаимозаменяемых ЛП</xs:documentation>
					</xs:annotation>
				</xs:element>
			</xs:sequence>
		</xs:complexType>
	</xs:element>
	<xs:simpleType name="uuidType">
		<xs:annotation>
			<xs:documentation>Уникальный идентификатор</xs:documentation>
		</xs:annotation>
		<xs:restriction base="xs:string">
			<xs:pattern value="[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="hashType">
		<xs:annotation>
			<xs:documentation>Хэш-сумма</xs:documentation>
		</xs:annotation>
		<xs:restriction base="xs:string">
			<xs:pattern value="[A-F0-9]{32}"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="HugeNameType">
		<xs:annotation>
			<xs:documentation>Текстовое поле размерности до 2000 символов</xs:documentation>
		</xs:annotation>
		<xs:restriction base="xs:string">
			<xs:maxLength value="2000"/>
			<xs:minLength value="1"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="BigNameType">
		<xs:annotation>
			<xs:documentation>Большое текстовое поле</xs:documentation>
		</xs:annotation>
		<xs:restriction base="xs:string">
			<xs:minLength value="1"/>
			<xs:maxLength value="500"/>
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="SmallNameType">
		<xs:annotation>
			<xs:documentation>Малое текстовое поле</xs:documentation>
		</xs:annotation>
		<xs:restriction base="xs:string">
			<xs:minLength value="1"/>
			<xs:maxLength value="50"/>
		</xs:restriction>
	</xs:simpleType>
</xs:schema>
'''

pk = open('scheme', 'w')
pk.write(xsd_sheme)
pk.close()

pk = open('scheme', 'r')
xsd_sheme2 = pk.read()
pk.close()


if os.path.exists(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'interchange.zip')):
    pass
else:
    r = requests.get('https://esklp.egisz.rosminzdrav.ru/fs/public/api/esklp')
    id_of_json = r.json()['results'][1].get('fileId')
    headers = {'Content-Type': 'text/xml; charset=UTF-8'}
    params={'exportType': 'fullActive'}
    s = requests.get(f'https://esklp.egisz.rosminzdrav.ru/fs/public/api/esklp/download/{id_of_json}', headers=headers)
    f = open('interchange.zip', 'wb+')
    f.write(s.content)
    f.close()

z = zipfile.ZipFile('interchange.zip', 'r')
file_name_zip = z.namelist()[0]
with z.open(file_name_zip) as myfile:
    xml_file = myfile.read().decode('UTF-8', 'strict')
    z.close()
# path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'interchange.zip')
# os.remove(path)


xs = xmlschema.XMLSchema(xsd_sheme)
dicto = xs.to_dict(xml_file)
dicto = dicto['ns2:group_list']['ns2:group']
dicto = list({i['@name'] for i in dicto})

inf_to_fill = []

#
def my_callback(var, indx, mode):
    try:
        total_pack.set(first_pack.get() * second_pack.get() * third_pack.get())
    except:
        pass

def get_meds_by_name():
    [tree.delete(i) for i in tree.get_children()]
    try:
        search = txt.get()
        if search == '':
            search = 'нифедипин'

        payloads_ = {f'searchString': search, 'morphology': 'on', 'recordsPerPage': '_100', 'sortBy': 'ITEM_NAME',
                     'search-filter': 'Наименованию+позиции', 'active': 'on', 'activeESCKLP': 'on', 'terminated': 'on',
                     'active': 'on', 'clGroupHiddenId': '0', 'ktruCharselectedTemplateItem': '0',
                     'showLotsInfoHidden': 'false'}

        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'
                                 ' AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/51.0.2704.103 Safari/537.36'}
        response = requests.get(f"https://zakupki.gov.ru/epz/ktru/search/results.html",
                                params=payloads_, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')


        response = soup.find_all(class_='search-registry-entry-block box-shadow-search-input')
        # print(response)
        all_info_of = []
        for i, alle in enumerate(response):
            try:
                medicine = alle.find(class_="d-flex registry-entry__header-mid__h4 align-items-center w-space-inherit "
                                            "text-break hyphenate").get_text().replace('  ', '').replace('\n', '')
                KTRU = alle.find(target="_blank").get_text().replace('  ', '').replace('\n', '')
                mesure = alle.find(class_='registry-entry__body-title').get_text().replace('Единица измерения: ',
                                                                                           '').replace('  ', '')

                all_info = alle.find_all(class_="lots-wrap-content__body__val")
                form = all_info[0].get_text().replace('  ', '')
                dose = all_info[1].get_text().replace('  ', '')
                is_GNVL = all_info[2].get_text().replace('  ', '')
                is_NSPV = all_info[3].get_text().replace('  ', '')
                all_info_of.append([KTRU, medicine, form, dose, mesure, is_GNVL, is_NSPV])
            except:
                continue
        [tree.insert('', 'end', values=row) for row in all_info_of]
    except:
        messagebox.showerror('Ошибка', 'Ничего не найдено')

def selected_row_medcine():
    KTRU = tree.set(tree.selection(), '#1')
    medicine = tree.set(tree.selection(), '#2').replace('\u200b', '')
    form = tree.set(tree.selection(), '#3')
    dose = tree.set(tree.selection(), '#4')
    mesure = tree.set(tree.selection(), '#5')
    is_GNVL = tree.set(tree.selection(), '#6')
    is_NSPV = tree.set(tree.selection(), '#7')
    try:
        quantity_of = float(quantity_main.get())
        pat = r'\d+\.*\d*'
        all_quantities = re.findall(pat,dose)
        total_q = str(quantity_of)+'\\'
        iteros = 1
        for c in all_quantities:
            c = float(c)
            c = c * quantity_of
            if iteros == 1:
                total_q = total_q + str(c)
            else:
                total_q = total_q + '+' + str(c)
            iteros += 1
        total_q = total_q.replace('.0', '')
        total_q


    except:
        messagebox.showerror('Ошибка', 'Введите количество в еденицах измерения')

    expr = re.compile(rf'{medicine}.*{form}.*{dose}', re.I)
        # with open('your_file.txt', 'w') as f:
    #     for item in dicto:
    #         f.write("%s\n" % item)

    newlist = list(filter(expr.match, dicto))
    if not newlist:
        interact = "Нет"
    else:
        interact = "Да"

    try:
        inf_to_fill.append([KTRU, medicine, form, dose, mesure, is_GNVL, is_NSPV, interact, total_q])
        quantity_main.delete(0, 'end')
    except:
        pass


def form_docx():
    document = Document()
    section = document.sections[-1]
    # for section in sections:
        # change orientation to landscape
        # section.orientation = WD_ORIENT.LANDSCAPE
    # section.orientation = WD_ORIENT.LANDSCAPE
    # print(section.page_height, section.page_width)
    new_width, new_height = section.page_height, section.page_width
    section.orientation = WD_ORIENT.LANDSCAPE
    section.page_width = Mm(297)
    section.page_height = Mm(210)

    table = document.add_table(rows=1, cols=10, style='Table Grid')
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = '№ п/п'
    hdr_cells[1].text = 'Наименование объекта закупки (МНН)'
    hdr_cells[2].text = 'Лек. форма'
    hdr_cells[3].text = 'ОКПД / КТРУ'
    hdr_cells[4].text = 'Ед. изм.'
    hdr_cells[5].text = 'Доз-ка'
    hdr_cells[6].text = 'Кол-во'
    hdr_cells[7].text = 'Лекарственный препарат включен в перечень жизненно необходимых и важнейших лекарственных препаратов'
    hdr_cells[8].text = 'Наличие в лекарственном препарате наркотических средств, психотропных веществ и их прекурсоров'
    hdr_cells[9].text = 'Возможность взаимозаменяемости лекарственных препаратов'
    iterat=1
    for KTRU, medicine, form, dose, mesure, is_GNVL, is_NSPV, interakt, total_q in inf_to_fill:
        row_cells = table.add_row().cells
        row_cells[0].text = str(iterat)
        row_cells[1].text = str(medicine)
        row_cells[2].text = form
        row_cells[3].text = KTRU
        row_cells[4].text = mesure
        row_cells[5].text = dose
        row_cells[6].text = total_q
        row_cells[7].text = is_GNVL
        row_cells[8].text = is_NSPV
        row_cells[9].text = interakt
        iterat +=1

    # sections = document.sections
    # for section in sections:
    #     # section.orientation = WD_ORIENT.PORTRAIT
    #     print(section.orientation)

    document.save('ТЗ.docx')
    window.quit()



window = Tk()
window.geometry('930x480+500+200')
window.title("Сформировать ТЗ для ЛП")
window.resizable(width=False, height=False)

first_pack = DoubleVar()
first_pack.set(1)
second_pack = DoubleVar()
second_pack.set(1)
third_pack = DoubleVar()
third_pack.set(1)
total_pack = DoubleVar()
total_pack.set(1)

first_pack.trace_add('write', my_callback)
second_pack.trace_add('write', my_callback)
third_pack.trace_add('write', my_callback)

frame_main = tkinter.Frame(window)
frame_main.grid(sticky='news')

lbl = Label(frame_main, text="Введите наименование препарата", font=("Arial Bold", 14))
lbl.grid(row=0, column=0)

txt = Entry(frame_main, width=30, borderwidth=5)
txt.focus()
txt.grid(row=0, column=1)

lbl2 = Label(frame_main, text="Введите количество в первичной упаковке", font=("Arial Bold", 14))
lbl2.grid(row=1, column=0)

quantity1 = Entry(frame_main, width=30, borderwidth=5, textvariable=first_pack)
quantity1.grid(row=1, column=1)

lbl12 = Label(frame_main, text="Введите количество во вторичной упаковке", font=("Arial Bold", 14))
lbl12.grid(row=2, column=0)

quantity2 = Entry(frame_main, width=30, borderwidth=5, textvariable=second_pack)
quantity2.grid(row=2, column=1)

lbl12 = Label(frame_main, text="Введите количество в транспортной упаковке", font=("Arial Bold", 14))
lbl12.grid(row=3, column=0)

quantity3 = Entry(frame_main, width=30, borderwidth=5, textvariable=third_pack)
quantity3.grid(row=3, column=1)

lbl12 = Label(frame_main, text="Итого в еденицах измерения", font=("Arial Bold", 14))
lbl12.grid(row=4, column=0)

quantity_main = Entry(frame_main, width=30, borderwidth=5, textvariable=total_pack)
quantity_main.grid(row=4, column=1)

btn_search = Button(frame_main, text='Поиск', bd = 3, bg='yellow', padx=138, command=get_meds_by_name)
btn_search.grid(row=0, column=3)

btn_search = Button(frame_main, text='Добавить', bd = 3, bg='green', padx=130, command=selected_row_medcine)
btn_search.grid(row=1, column=3)

btn_search = Button(frame_main, text='Сформировать', bd = 3, bg='gray', padx=114, command=form_docx)
btn_search.grid(row=2, column=3)

frame_canvas = tkinter.Frame(frame_main)
frame_canvas.grid(row=5, column=0, sticky='nw', columnspan=4)
# frame_canvas.grid_rowconfigure(0, weight=1)
# frame_canvas.grid_columnconfigure(0, weight=1)
# frame_canvas.grid_propagate(False)


tree = ttk.Treeview(frame_canvas, columns=('KTRU', 'medicine', 'form', 'dose', 'measure', 'is_GNVL', 'is_NSPV' ), height=15, show='headings')

tree.column('KTRU', width=220)  # , stretch="no"
tree.column('medicine', width=150)  # , stretch="no"
tree.column('form', width=270)
tree.column('dose', width=100)
tree.column('measure', width=70)
tree.column('is_GNVL', width=50)
tree.column('is_NSPV', width=50)

tree.heading('KTRU', text='КТРУ')
tree.heading('medicine', text='Препарат')
tree.heading('form', text='Форма')
tree.heading('dose', text='Дозировка')
tree.heading('measure', text='Ед. Изм')
tree.heading('is_GNVL', text='ЖНВЛП')
tree.heading('is_NSPV', text='НСПВ')

# tree.grid(row=5, column=0, columnspan=4) #fill=tkinter.Y)

# Add a canvas in that frame
tree.grid(row=1, column=1, sticky="news")

scroll = tkinter.Scrollbar(frame_canvas, command=tree.yview, orient="vertical")
scroll.grid(row=1, column=2, sticky='ns')
# scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
tree.configure(yscrollcommand=scroll.set)

# btn_copy_org = Button(window, text='Копировать организацию в буфер', command=copy_org, bd=5)
# btn_copy_org.pack(side=tkinter.LEFT) #side=tkinter.LEFT

# btn_copy_mail = Button(window, text='Копировать почту в буфер', command=copy_mail, bd=5)
# btn_copy_mail.pack(side=tkinter.LEFT) #side=tkinter.LEFT
#
window.iconphoto(True, tkinter.PhotoImage(data=icon))
window.mainloop()