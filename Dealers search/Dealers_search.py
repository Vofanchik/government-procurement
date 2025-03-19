import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
from data import icon, regions

import pyperclip
import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint


def get_item_name():
    # try:

        region = regions[combo.get()]
        prodsearch = txt.get()
        payloads_ = {f'customerregion': region, 'perpage': {combo_1.get()}, 'currentstage': 'EC', 'sort': '-signDate'}
        response = requests.get(f"http://openapi.clearspending.ru/restapi/v3/contracts/search/?productsearch={prodsearch}",
                                params=payloads_)
        all_info = []
        names_of = []
        emails_of = []
        prods_of = []
        urls_of = []
        phone_of = []
        inn_of = []
        for contracts in response.json()['contracts']['data']:

            try:

                org_name = contracts['suppliers'][0]['organizationName']
                if org_name not in names_of:
                    names_of.append(org_name)
                else:
                    continue
            except:
                continue
            regnum = contracts['regNum']

            payload = {'contractReestrNumber': regnum}
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
            response_2 = requests.get('https://zakupki.gov.ru/epz/contract/printForm/view.html?', params=payload,
                                      headers=headers)
            response_2.encoding = 'utf-8'
            contract_url = contracts['contractUrl']
            soup = BeautifulSoup(response_2.text, 'html.parser')
            divphone = str(soup.find_all("div", class_="inextricable land")[0])
            phone_email = BeautifulSoup(divphone, 'html.parser')
            main_info = phone_email.tr.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.contents
            phone_email = main_info[-2].contents
            phone = phone_email[0]
            email = phone_email[-1]
            inn = main_info[11].contents
            urls_of.append(contract_url)
            emails_of.append(email)
            phone_of.append(phone)
            inn_of.append(inn)
            products_list = []
            for itera, products in enumerate(contracts['products']):
                products_list.append(products['name'])
                if itera == 0:
                    break
            prods_of.append(str(products_list).replace('[\'', '').replace('\']', ''))
        down_space = '_' * 10

        names_of_fin = [elem.replace('ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ', 'ООО').replace('Общество с ограниченной ответственностью', 'ООО').replace('ЗАКРЫТОЕ АКЦИОНЕРНОЕ ОБЩЕСТВО', 'ЗАО') for elem in names_of]

        all_info.append(list(zip(names_of_fin,emails_of,phone_of, prods_of, inn_of)))
        [tree.insert('', 'end', values=row) for row in all_info[0]]

    # except:
        # messagebox.showerror('Ошибка', 'Попробуйте другой запрос')


def copy_org():
    pyperclip.copy(selected_row_org())


def selected_row_org():
    return tree.set(tree.selection(), '#1')


def copy_mail():
    pyperclip.copy(selected_row_mail())

def selected_row_mail():
    return tree.set(tree.selection(), '#2')

def selected_row_inn():
    return tree.set(tree.selection(), '#5')

def form_adress():
    try:
        payloads_ = {'query': f'{selected_row_inn()}'}

        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'
                                 ' AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/51.0.2704.103 Safari/537.36',
                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   }
        response = requests.post(f"https://egrul.nalog.ru/",
                                 data=payloads_, headers=headers)
        id = response.json()['t']

        response = requests.get(f"https://egrul.nalog.ru/search-result/{id}",
                                headers=headers)

        adress = response.json()['rows'][0]['a']
        short_name = response.json()['rows'][0]['c']
        kpp = response.json()['rows'][0]['p']
        administrator = response.json()['rows'][0]['g']
        ogrn = response.json()['rows'][0]['o']
        all_info = f'Руководителю организации\n' \
                   f'{short_name}\n\n' \
                   f'{administrator}\n\n' \
                   f'{adress}\n\n' \
                   f'ОГРН:{ogrn}\nИНН:{selected_row_inn()}\nКПП:{kpp}\n\n' \
                   f'Эл. почта:{selected_row_mail()}'
        pyperclip.copy(all_info)
    except:
        messagebox.showerror('Ошибка', 'Возможно проблемма в ИП или не выбрана организация')


window = Tk()
window.geometry('620x540')
window.title("Поиск поставщиков")
window.resizable(width=False, height=False)


lbl = Label(window, text="Введите наименование товара", font=("Arial Bold", 14))
lbl.pack()

txt = Entry(window, width=100, borderwidth=5)
txt.focus()
txt.pack()

lbl2 = Label(window, text="Выберите регион поиска", font=("Arial Bold", 14))
lbl2.pack()

combo = Combobox(window)
combo['values'] = list(regions.keys())
combo.current(0)
combo.pack()

lbl3 = Label(window, text="Выберите количество запросов", font=("Arial Bold", 14))
lbl3.pack()

combo_1 = Combobox(window)
combo_1['values'] = ('1', '5', '10', '20')
combo_1.current(0)
combo_1.pack()

btn_search = Button(window, text='Поиск', command=get_item_name, bd = 3, bg='cyan', padx=230)
btn_search.pack()


tree = ttk.Treeview(columns=('organization', 'email', 'phone', 'items', 'inn'), height=15, show='headings')


tree.column('organization', width=200)  # , stretch="no"
tree.column('email', width=100)
tree.column('phone', width=100)
tree.column('items', width=100)
tree.column('inn', width=100)

tree.heading('organization', text='Организация')
tree.heading('email', text='Почта')
tree.heading('phone', text='Телефон')
tree.heading('items', text='Объект закупки')
tree.heading('inn', text='ИНН')

tree.pack()

btn_copy_org = Button(window, text='Копировать организацию в буфер', command=copy_org, bd=5)
btn_copy_org.pack(side=tkinter.LEFT) #side=tkinter.LEFT

btn_copy_mail = Button(window, text='Копировать почту в буфер', command=copy_mail, bd=5)
btn_copy_mail.pack(side=tkinter.LEFT) #side=tkinter.LEFT

btn_form_adress = Button(window, text='Сформировать адресата в буфер', command=form_adress, bd=5)
btn_form_adress.pack(side=tkinter.LEFT)

window.iconphoto(True, tkinter.PhotoImage(data=icon))
window.mainloop()