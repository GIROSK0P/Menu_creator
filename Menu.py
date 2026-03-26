import tkinter as tk
from tkinter import ttk
import sqlite3
from idlelib.tooltip import Hovertip
import json
import math
import subprocess

class Main(tk.Frame):
    
    
    def __init__(self,root_q,to_menu=None): 
        self.to_menu=to_menu      
        self.na_vkl=0
        self.r_vkl=0
        self.menu_cat_=0
        self.rg_to_menu_vkl=0
        
        super().__init__(root_q)
    
        self.init_main()
    
#####################################        
        
    def init_main(self):

        self.label = tk.Label(text='Авторизация', bg = 'White',font=['arial','18'])
        self.label.place(x=416,y=150)

        self.label_l = tk.Label(text='Логин', bg = 'White',font=['arial','13'])
        self.label_l.place(x=425,y=200)

        self.label_lh = tk.Label(text='Введите логин', bg = 'White',font=['arial','8'])
        self.label_lh.place(x=425,y=225)

        self.entry_l = ttk.Entry()
        self.entry_l.place(x = 425,y = 250)

        self.label_p = tk.Label(text='Пароль', bg = 'White', font=['arial','13'],)
        self.label_p.place(x=425,y=275)

        self.label_lp = tk.Label(text='Введите пароль', bg = 'White',font=['arial','8'])
        self.label_lp.place(x=425,y=300)

        self.entry_p = ttk.Entry(show='*')
        self.entry_p.place(x = 425,y = 325)

        self.btn_aut = tk.Button(text = 'Войти', bg ='White',font=['arial','8'],width=19,
                            bd = 3, command=self.lp_aut)
        self.btn_aut.place(x=425, y=360)

        self.label_help = tk.Label(text='Нет аккаунта? Создайте его, нажав кнопку ниже!',foreground="#696969", bg='White',font=['arial','8'])
        self.label_help.place(x=360,y=385)

        self.btn_reg = tk.Button(text = 'Зарегистрироваться', bg ='White',font=['arial','8'],width=19,
                            bd = 3, command=self.lp_reg)
        self.btn_reg.place(x=425, y=410)

    

#####################################        
                   
    def lp_aut(self):

        lp=str(self.entry_l.get())+str(self.entry_p.get())
        with open('password.json','r') as lvl: 
            self.login_password = json.load(lvl)
        
        
        if lp in self.login_password:

            self.to_menu = self.login_password[(str(self.entry_l.get())+str(self.entry_p.get()))]

            self.label_l.destroy()
            self.entry_l.destroy()
            self.label_p.destroy()
            self.entry_p.destroy()
            if self.na_vkl==1:
                self.label_na.destroy()
            if self.r_vkl==1:
                self.label_r.destroy()
            if self.rg_to_menu_vkl==1:
                self.btn_aut.destroy()
                self.label_help.destroy()
                self.btn_reg.destroy()
                self.label_lh.destroy()
                self.label_lp.destroy()
                self.label.destroy()
                self.label_m.destroy()
                self.label_mh.destroy()
                self.entry_m.destroy()
                self.btn_back.destroy()
                self.label_r.destroy()
                self.menu_btn.destroy()
            else:
                self.btn_aut.destroy()
                self.label_help.destroy()
                self.btn_reg.destroy()
                self.label_lh.destroy()
                self.label_lp.destroy()
                self.label.destroy()
            root.title("Категории меню")
            self.start_menu_aut()
        
        
        elif not(lp in self.login_password):

            self.label_na = tk.Label(text='Логин или пароль неправильный', bg='White',font=['arial','18'])
            self.label_na.place(x=310,y=440)
            self.na_vkl = 1

#####################################        
                        
    def lp_reg(self):

        root.title('Регистрация')
        
        self.btn_aut.destroy()
        self.label_help.destroy()
        self.btn_reg.destroy()
        self.label_lh.destroy()
        self.label_lp.destroy()
        self.label.destroy()
        if self.na_vkl==1:
            self.label_na.destroy()

        self.label = tk.Label(text='Регистрация', bg = 'White',font=['arial','18'])
        self.label.place(x=416,y=150)

        self.label_lh = tk.Label(text='Придумайте логин', bg = 'White',font=['arial','8'])
        self.label_lh.place(x=425,y=225)

        self.label_lp = tk.Label(text='Придумайте пароль', bg = 'White',font=['arial','8'])
        self.label_lp.place(x=425,y=300)

        self.label_m = tk.Label(text='Название меню', bg = 'White', font=['arial','13'])
        self.label_m.place(x=424,y=350)

        self.label_mh = tk.Label(text='Придумайте название меню', bg = 'White', font=['arial','8'])
        self.label_mh.place(x=424,y=375)

        self.entry_m = ttk.Entry()
        self.entry_m.place(x = 427,y = 400)

        self.btn_aut = tk.Button(text = 'Зарегестрироваться', bg ='White',font=['arial','10'],width=24,
                            bd = 3,command = self.reg)
        self.btn_aut.place(x=390, y=435)
        
        self.btn_back =tk.Button(text='Вернуться назад',bg ='White',font=['arial','10'],width=24,
                            bd = 3,command =self.back)   
        self.btn_back.place(x=390, y=480)

        self.rg_to_menu_vkl = 1

#####################################        
        
    def reg(self):

        with open('password.json','r') as lvl: 
            self.login_password = json.load(lvl)
        if ((str(self.entry_l.get())+str(self.entry_p.get())) in self.login_password.keys()) or ((str(self.entry_m.get())+'.db') in self.login_password.values()):
            self.label_r = tk.Label(text='Аккаунт с этими данными уже существует. Придумайте другой логин и пароль.', bg = 'White', font=['arial','14'],)
            self.label_r.place(x=150,y=510)
            self.r_vkl=1
            
        elif not((str(self.entry_l.get())+str(self.entry_p.get())) in self.login_password.keys()):

            self.login_password[(str(self.entry_l.get())+str(self.entry_p.get()))]=(str(self.entry_m.get())+'.db')
            with open('password.json','w') as lvl: 
                json.dump(self.login_password,lvl)
            
            if self.r_vkl==1:
                self.label_r.destroy()
        
            self.label_r = tk.Label(text='Вы успешно зарегистрировались.', bg = 'White', font=['arial','18'],)
            self.label_r.place(x=320,y=480)

            self.to_menu = str(self.entry_m.get())

            self.btn_aut.destroy()

            self.menu_btn = tk.Button(text='Открыть меню',bg ='White',font=['arial','10'],width=24,
                            bd = 3,command=self.start_menu_reg)
            self.menu_btn.place(x=390, y=520)


            

#####################################        
        
    def start_menu_aut(self):

        self.menu_red()
        self.menu_cat=0

        if self.menu_cat_==1:
            self.toolbar_c.destroy()
            self.btn_add.destroy()
            self.btn_refr.destroy()
            self.btn_del.destroy()
            self.btn_upd.destroy()
            self.btn_search.destroy()
            self.btn_next.destroy()
            self.back_btn.destroy()
            self.scroll.destroy()
            self.tree.destroy()
        try:
            self.label_na.destroy()
        except:
            pass

        root.title('Категории меню')
        root.geometry('1000x700')

        # Создание панели инструментов
        self.toolbar = tk.Frame(self,bg = 'White', bd = 2)
        self.toolbar.pack(side = tk.TOP, fill = tk.X)

        # Создание кнопки добавления записи в таблицу
        self.add_img = tk.PhotoImage(file = 'img/Add.png' )
        self.btn_add = tk.Button(self.toolbar, text = 'Добавить', bg ='White',
                            bd = 0, image = self.add_img,command=self.open_child)
        self.btn_add.pack(side = tk.LEFT)
        Hovertip(self.btn_add, "Добавить категорию", hover_delay=100)
    
        # Создание кнопки редактирования записи в таблице
        self.refr_img = tk.PhotoImage(file = 'img/Refresh.png')
        self.btn_refr = tk.Button(self.toolbar, text = 'Редактировать', bg ='White',
                            bd = 0, image = self.refr_img,command=self.open_update_child)
        self.btn_refr.pack(side = tk.LEFT)
        Hovertip(self.btn_refr, "Изменить категорию", hover_delay=100)

        # Создание кнопки удаления записи в таблицы
        self.del_img = tk.PhotoImage(file = 'img/Delete.png')
        self.btn_del = tk.Button(self.toolbar, text = 'Удалить', bg ='White',
                            bd = 0, image = self.del_img,
                            command = self.delete_records)        
        self.btn_del.pack(side = tk.LEFT)
        Hovertip(self.btn_del, "Удалить категорию", hover_delay=100)

        # Создание кнопки обновления всех записей таблицы
        self.upd_img = tk.PhotoImage(file = 'img/Upd.png' )
        self.btn_upd = tk.Button(self.toolbar, text = 'Обновить', bg ='White',
                            bd = 0, image = self.upd_img, command=self.refresh_records)        
        self.btn_upd.pack(side = tk.LEFT)
        Hovertip(self.btn_upd, "Обновить таблицу", hover_delay=100)

        # Создание кнопки поиска 
        self.search_img = tk.PhotoImage(file = 'img/Search.png' )
        self.btn_search = tk.Button(self.toolbar, text = 'Поиск', bg ='White',
                            bd = 0, image = self.search_img,
                            command = self.open_search_child)        
        self.btn_search.pack(side = tk.LEFT)
        Hovertip(self.btn_search, "Найти категорию", hover_delay=100)

        self.next_img = tk.PhotoImage(file = 'img/Next.png' )
        self.btn_next = tk.Button(self.toolbar, text = 'Следующее', bg ='White',
                            bd = 0, image = self.next_img, command = self.redact_categ)        
        self.btn_next.pack(side = tk.LEFT)
        Hovertip(self.btn_next, "Перейти к следующему шагу редактирования меню", hover_delay=100)

        # Добавлление таблиц
        self.tree = ttk.Treeview(self, columns = ('ID', 'name', 'numdish'),
                                 height = 45, show = 'headings')

        
        # Добавление параметров колонкам
        self.tree.column('ID', width = 50, anchor = tk.CENTER)
        self.tree.column('name', width = 700, anchor = tk.CENTER)
        self.tree.column('numdish', width = 235, anchor = tk.CENTER)

        # Добавление записей колонкам
        self.tree.heading('ID', text = '№')
        self.tree.heading('name', text = 'Название категории')
        self.tree.heading('numdish', text = 'Количество блюд')

        self.tree.pack(side=tk.LEFT)       

        # Создание ползунка для пролистывания таблицы
        self.scroll = tk.Scrollbar(self, command = self.tree.yview)
        self.scroll.pack(side = tk.LEFT, fill = tk.Y)
        self.tree.configure(yscrollcommand = self.scroll.set)
        
        self.view_records()

#####################################        
        
    def start_menu_reg(self):

        self.menu_red()

        root.title('Редактирование меню')

        

        self.label_l.destroy()
        self.entry_l.destroy()
        self.label_p.destroy()
        self.entry_p.destroy()
        if self.na_vkl==1:
            self.label_na.destroy()
        if self.r_vkl==1:
            self.label_r.destroy()
        if self.rg_to_menu_vkl==1:
            self.btn_aut.destroy()
            self.label_help.destroy()
            self.btn_reg.destroy()
            self.label_lh.destroy()
            self.label_lp.destroy()
            self.label.destroy()
            self.label_m.destroy()
            self.label_mh.destroy()
            self.entry_m.destroy()
            self.btn_back.destroy()
            self.label_r.destroy()
            self.menu_btn.destroy()
        else:
            self.btn_aut.destroy()
            self.label_help.destroy()
            self.btn_reg.destroy()
            self.label_lh.destroy()
            self.label_lp.destroy()
            self.label.destroy()

        self.menu_cat = 0
        
        # Создание панели инструментов
        self.toolbar_r = tk.Frame(bg = 'White', bd = 2)
        self.toolbar_r.pack(side = tk.TOP, fill = tk.X)

        # Создание кнопки добавления записи в таблицу
        self.add_img = tk.PhotoImage(file = 'img/Add.png' )
        self.btn_add = tk.Button(self.toolbar, text = 'Добавить', bg ='White',
                            bd = 0, image = self.add_img,command=self.open_child)
        self.btn_add.pack(side = tk.LEFT)
        Hovertip(self.btn_add, "Добавить категорию", hover_delay=100)
    
        # Создание кнопки редактирования записи в таблице
        self.refr_img = tk.PhotoImage(file = 'img/Refresh.png')
        self.btn_refr = tk.Button(self.toolbar, text = 'Редактировать', bg ='White',
                            bd = 0, image = self.refr_img,command=self.open_update_child)
        self.btn_refr.pack(side = tk.LEFT)
        Hovertip(self.btn_refr, "Изменить категорию", hover_delay=100)

        # Создание кнопки удаления записи в таблицы
        self.del_img = tk.PhotoImage(file = 'img/Delete.png')
        self.btn_del = tk.Button(self.toolbar, text = 'Удалить', bg ='White',
                            bd = 0, image = self.del_img,
                            command = self.delete_records)        
        self.btn_del.pack(side = tk.LEFT)
        Hovertip(self.btn_del, "Удалить категорию", hover_delay=100)

        # Создание кнопки обновления всех записей таблицы
        self.upd_img = tk.PhotoImage(file = 'img/Upd.png' )
        self.btn_upd = tk.Button(self.toolbar, text = 'Обновить', bg ='White',
                            bd = 0, image = self.upd_img, command=self.refresh_records)        
        self.btn_upd.pack(side = tk.LEFT)
        Hovertip(self.btn_upd, "Обновить таблицу", hover_delay=100)

        # Создание кнопки поиска 
        self.search_img = tk.PhotoImage(file = 'img/Search.png' )
        self.btn_search = tk.Button(self.toolbar, text = 'Поиск', bg ='White',
                            bd = 0, image = self.search_img,
                            command = self.open_search_child)        
        self.btn_search.pack(side = tk.LEFT)
        Hovertip(self.btn_search, "Найти категорию", hover_delay=100)

        self.next_img = tk.PhotoImage(file = 'img/Next.png' )
        self.btn_next = tk.Button(self.toolbar, text = 'Следующее', bg ='White',
                            bd = 0, image = self.next_img, command = self.redact_categ)        
        self.btn_next.pack(side = tk.LEFT)
        Hovertip(self.btn_next, "Перейти к следующему шагу редактирования меню", hover_delay=100)

        # Добавлление таблиц
        self.tree = ttk.Treeview(self, columns = ('ID', 'name', 'numdish'),
                                 height = 45, show = 'headings')

        
        # Добавление параметров колонкам
        self.tree.column('ID', width = 50, anchor = tk.CENTER)
        self.tree.column('name', width = 700, anchor = tk.CENTER)
        self.tree.column('numdish', width = 235, anchor = tk.CENTER)

        # Добавление записей колонкам
        self.tree.heading('ID', text = '№')
        self.tree.heading('name', text = 'Название категории')
        self.tree.heading('numdish', text = 'Количество блюд')

        self.tree.pack(side = tk.LEFT)        

        # Создание ползунка для пролистывания таблицы
        self.scroll = tk.Scrollbar(self, command = self.tree.yview)
        self.scroll.pack(side = tk.LEFT, fill = tk.Y)
        self.tree.configure(yscrollcommand = self.scroll.set)

        self.view_records()

#####################################        
            
    def records(self,name,numdish):
        
        self.insert_data(name,numdish)
        self.view_records()
    
    def insert_data_dish(self,id_cat,name,struct,serv_weight,edin_izm,name_cat,price):
        self.cur.execute(f'''INSERT INTO {name_cat} (id_cat,name,structure,serv_weight,edin_izm,price) 
                         VALUES(?,?,?,?,?,?)''',(id_cat,name,struct,serv_weight,edin_izm,price,))
        self.conn.commit()

    
    def records_dish(self, id,name,struct,serv_weight,edin_izm,price):
        

        self.cur.execute('''SELECT name FROM Categories WHERE id LIKE ?''',(id,))
        name_cat=self.cur.fetchall()[0][0]
        name_cat=name_cat.replace(' ','_')

        self.insert_data_dish(id,name,struct,serv_weight,edin_izm,name_cat,price)
        self.view_records_cat(name_cat)


    def view_records(self):

            # Выбор информации из БД
        self.cur.execute('''SELECT * FROM Categories''')

            # Удаление всего из виджета таблицы
        [self.tree.delete(i) for i in self.tree.get_children()]

            # Добавление в  таблицу всех данных из таблицы
        [self.tree.insert('','end',values = row) for row in self.cur.fetchall()]

    def view_records_cat(self,cat_name:str):

        cat_name= cat_name.replace(' ','_')

            # Выбор информации из БД
        self.cur.execute(f'''SELECT * FROM {cat_name}''')

            # Удаление всего из виджета таблицы
        [self.tree.delete(i) for i in self.tree.get_children()]

            # Добавление в  таблицу всех данных из таблицы
        [self.tree.insert('','end',values = row) for row in self.cur.fetchall()]

#####################################        
        
    def refresh_records(self):
        self.view_records()

    def refresh_records_cat(self, name_cat):
        self.view_records_cat(name_cat)

##################################### 
        
    def open_child(self):

        Add(self.to_menu)

#####################################

    def open_update_child(self):

        Update(self.to_menu)

##################################### 

    def open_search_child(self):

        Search()

##################################### 
        
    def open_child_dish(self,i):

        Add_dish(i,self.to_menu)

    def open_update_child_dish(self,i):

        Update_dish(i,self.to_menu)

##################################### 

    def open_search_child_dish(self,i):

        Search_dish(i)

#####################################

    
    
    # Метод поиска данных по ФИО
    def search_records(self, name):

        name = ('%' + name + '%')

        # Выбор информации из БД
        self.cur.execute('''SELECT * FROM Categories WHERE name LIKE ?''',(name,))

        # Удаление всего из виджета таблицы
        [self.tree.delete(i) for i in self.tree.get_children()]

        # Добавление в  таблицу всех данных из таблицы
        [self.tree.insert('','end',values = row)
         for row in self.cur.fetchall()]
        
    # Метод поиска данных по ФИО
    def search_records_dish(self, name_cat, name):

        name = ('%' + name + '%')

        # Выбор информации из БД
        self.cur.execute(f'''SELECT * FROM {name_cat} WHERE name LIKE ?''',(name,))

        # Удаление всего из виджета таблицы
        [self.tree.delete(i) for i in self.tree.get_children()]

        # Добавление в  таблицу всех данных из таблицы
        [self.tree.insert('','end',values = row)
         for row in self.cur.fetchall()]
        
    # Метод изменения данных
    def update_record(self,name,numdish):

        select_record_id = self.tree.set(self.tree.selection()[0],'#1')
        self.cur.execute('''UPDATE Categories SET name = ?, numdish = ? WHERE ID = ?''',
                            (name,numdish,select_record_id))
        
        self.conn.commit()
        self.view_records()

################################

    def update_record_dish(self,id,name,struct,serv_weight,edin_izm,price):

        self.cur.execute('''SELECT name FROM Categories WHERE id LIKE ?''',(id,))
        name_cat=self.cur.fetchall()[0][0]
        name_cat=name_cat.replace(' ','_')

        select_record_id = self.tree.set(self.tree.selection()[0],'#1')
        self.cur.execute(f'''UPDATE {name_cat} SET id_cat = ?, name = ?, structure = ?,
                         serv_weight = ?, edin_izm = ?, price = ? WHERE id_dish = ?''',
                        (id,name,struct,serv_weight,edin_izm,price,select_record_id))
        
        self.conn.commit()
        self.view_records_cat(name_cat)

    # Метод удаления данных
    def delete_records(self):

        for row in self.tree.selection():

            self.cur.execute('''DELETE FROM Categories WHERE ID = ?''',
                                (self.tree.set(row,'#1'), ))
        
            self.cur.execute(f'''DROP TABLE IF EXISTS {(self.tree.set(row,'#2'))}''')


            with open('menuname.json','r', encoding='utf-8') as lvl: 
                self.menu_names_slov = json.load(lvl)

            menu_names = self.menu_names_slov['1']
            menu_names = menu_names.split('_')[:-1]
            
            menu_names.remove((self.tree.set(row,'#2')))
            menu_name=''
            for i in menu_names:
                menu_name=menu_name+i+'_'

            self.menu_names_slov['1'] = menu_name

            with open('menuname.json','w', encoding='utf-8') as lvl: 
                    json.dump(self.menu_names_slov,lvl)

        self.conn.commit()
        self.view_records()

    def delete_records_dish(self, name_cat):

        for row in self.tree.selection():

            self.cur.execute(f'''DELETE FROM {name_cat} WHERE id_dish = ?''',
                                (self.tree.set(row,'#1'), ))
        self.view_records_cat(name_cat)
#####################################        
        
    def menu_red(self):
        
        
        self.conn = sqlite3.connect(f'{self.to_menu}')

        self.cur = self.conn.cursor()

        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS Categories(
                            id INTEGER PRIMARY KEY,
                            name VARCHAR(45),
                            numdish INTEGER)
                            ''')

#####################################        
            
    def insert_data(self,name,numdish):

        self.cur.execute('''INSERT INTO Categories(name,numdish)
                         VALUES(?,?)''',(name,numdish))
        
        with open('menuname.json','r', encoding='utf-8') as lvl: 
            self.menu_names_slov = json.load(lvl)

        menu_names = self.menu_names_slov['1']
        menu_names=menu_names + name + '_'

        self.menu_names_slov['1'] = menu_names

        with open('menuname.json','w', encoding='utf-8') as lvl: 
                json.dump(self.menu_names_slov,lvl)

        self.conn.commit()  

    def red_categ(self):
        self.conn = sqlite3.connect(f'{self.to_menu}')
        

        with open('menuname.json','r', encoding='utf-8') as lvl: 
            self.menu_names_slov = json.load(lvl)
        
        menu_name = self.menu_names_slov['1'].split('_')[:-1]
        query=''
        for i in menu_name:      
            i = i.replace(' ','_')
            query = query + f'''
                            CREATE TABLE IF NOT EXISTS {i} (
                            id_dish INTEGER PRIMARY KEY,
                            id_cat INTEGER,
                            name VARCHAR(45),
                            structure TEXT,
                            serv_weight INT,
                            edin_izm VARCHAR(10),
                            price INT,
                            FOREIGN KEY (id_cat)
                            REFERENCES Categories(id) ON DELETE CASCADE);
                             '''
        self.cur.executescript(query)

#####################################
    
    def redact_categ(self,num_cat=0):
        
        self.red_categ()

        
        root.update()
        
        self.conn = sqlite3.connect(f'{self.to_menu}')
        root.geometry('1020x495')

        with open('menuname.json','r', encoding='utf-8') as lvl: 
            self.menu_names_slov = json.load(lvl)
        
        menu_name = self.menu_names_slov['1'].split('_')[:-1]

        if num_cat>(len(menu_name)-1):
            self.edit_complete()
            num_cat-=1
        if num_cat<0:
            self.start_menu_aut()
            if self.menu_cat==0:
                self.toolbar.destroy()
                self.btn_add.destroy()
                self.btn_refr.destroy()
                self.btn_del.destroy()
                self.btn_upd.destroy()
                self.btn_search.destroy()
                self.btn_next.destroy()
                self.scroll.destroy()
                self.tree.destroy()
            if self.menu_cat_==1:
                self.toolbar_c.destroy()
                self.btn_add.destroy()
                self.btn_refr.destroy()
                self.btn_del.destroy()
                self.btn_upd.destroy()
                self.btn_search.destroy()
                self.btn_next.destroy()
                self.back_btn.destroy()
                self.scroll.destroy()
                self.tree.destroy()
            try:
                self.label_na.destroy()
            except:
                pass
        
        if self.menu_cat==0:
            self.toolbar.destroy()
            self.btn_add.destroy()
            self.btn_refr.destroy()
            self.btn_del.destroy()
            self.btn_upd.destroy()
            self.btn_search.destroy()
            self.btn_next.destroy()
            self.scroll.destroy()
            self.tree.destroy()
        if self.menu_cat_==1:
            self.toolbar_c.destroy()
            self.btn_add.destroy()
            self.btn_refr.destroy()
            self.btn_del.destroy()
            self.btn_upd.destroy()
            self.btn_search.destroy()
            self.btn_next.destroy()
            self.back_btn.destroy()
            self.scroll.destroy()
            self.tree.destroy()
        try:
            self.label_na.destroy()
        except:
            pass
        
        i = menu_name[num_cat]
        self.menu_cat_=1
        i = i.replace(' ','_')

        root.title(f'Блюда категории "{i}"')

       

        # Создание панели инструментов
        self.toolbar_c = tk.Frame(bg = 'White', bd = 2)
        self.toolbar_c.pack(side = tk.TOP, fill=tk.X)

        # Создание кнопки добавления записи в таблицу
        self.add_img = tk.PhotoImage(file = 'img/Add.png' )
        self.btn_add = tk.Button(self.toolbar_c, text = 'Добавить', bg ='White',
                            bd = 0, image = self.add_img,command=lambda: self.open_child_dish(i))
        self.btn_add.pack(side = tk.LEFT)
        Hovertip(self.btn_add, "Добавить блюдо", hover_delay=100)

        # Создание кнопки редактирования записи в таблице
        self.refr_img = tk.PhotoImage(file = 'img/Refresh.png')
        self.btn_refr = tk.Button(self.toolbar_c, text = 'Редактировать', bg ='White',
                            bd = 0, image = self.refr_img,command= lambda: self.open_update_child_dish(i))
        self.btn_refr.pack(side = tk.LEFT)
        Hovertip(self.btn_refr, "Редактировать блюдо", hover_delay=100)

            # Создание кнопки удаления записи в таблицы
        self.del_img = tk.PhotoImage(file = 'img/Delete.png')
        self.btn_del = tk.Button(self.toolbar_c, text = 'Удалить', bg ='White',
                        bd = 0, image = self.del_img,
                        command = lambda: self.delete_records_dish(i))        
        self.btn_del.pack(side = tk.LEFT)
        Hovertip(self.btn_del, "Удалить блюдо", hover_delay=100)

        # Создание кнопки обновления всех записей таблицы
        self.upd_img = tk.PhotoImage(file = 'img/Upd.png' )
        self.btn_upd = tk.Button(self.toolbar_c, text = 'Обновить', bg ='White',
                        bd = 0, image = self.upd_img, command=lambda: self.refresh_records_cat(i))        
        self.btn_upd.pack(side = tk.LEFT)
        Hovertip(self.btn_upd, "Обновить таблицу", hover_delay=100)

        # Создание кнопки поиска 
        self.search_img = tk.PhotoImage(file = 'img/Search.png' )
        self.btn_search = tk.Button(self.toolbar_c, text = 'Поиск', bg ='White',
                        bd = 0, image = self.search_img,
                        command = lambda: self.open_search_child_dish(i))
        self.btn_search.pack(side = tk.LEFT)
        Hovertip(self.btn_search, "Найти блюдо", hover_delay=100)

        self.back_img = tk.PhotoImage(file = 'img/back.png' )
        self.back_btn = tk.Button(self.toolbar_c, text = 'Предыдущее',bg ='White',
                        bd = 0, image = self.back_img, command = lambda: self.redact_categ(num_cat = num_cat-1) if num_cat>0 else self.start_menu_aut())
        self.back_btn.pack(side = tk.LEFT)
        Hovertip(self.back_btn, "Предыдущая страница", hover_delay=100)

        self.next_img = tk.PhotoImage(file = 'img/Next.png' )
        self.btn_next = tk.Button(self.toolbar_c, text = 'Следующее', bg ='White',
                        bd = 0, image = self.next_img, command = lambda: self.redact_categ(num_cat = num_cat+1))        
        self.btn_next.pack(side = tk.LEFT)
        Hovertip(self.btn_next, "Следующая страница", hover_delay=100)

        i = i.replace('_',' ')

        self.label_id_cat = tk.Label(self.toolbar_c, text=f'''Категория: {i}
        ID категории: {num_cat+1}''', font='Arial 20',bg='White')
        self.label_id_cat.pack(side=tk.RIGHT)
        
        
        i = i.replace(' ','_')

         # Добавлление таблиц
        self.tree = ttk.Treeview(self, columns = ('id_dish', 'id_cat','name','structure',
                                                  'serv_weight','edin_izm','price'),
                                                    height = 20, show = 'headings')
        
        
        # Добавление параметров колонкам
        self.tree.column('id_dish', width = 75, anchor = tk.CENTER)
        self.tree.column('id_cat', width = 80, anchor = tk.CENTER)
        self.tree.column('name', width = 245, anchor = tk.CENTER)
        self.tree.column('structure', width = 350, anchor = tk.CENTER)
        self.tree.column('serv_weight', width = 75, anchor = tk.CENTER)
        self.tree.column('edin_izm', width = 100, anchor = tk.CENTER)
        self.tree.column('price',width = 75,anchor=tk.CENTER)


        # Добавление записей колонкам
        self.tree.heading('id_dish', text = '№ блюда')
        self.tree.heading('id_cat', text = 'ID категории')
        self.tree.heading('name', text = 'Название блюда')
        self.tree.heading('structure', text = 'Состав')
        self.tree.heading('serv_weight', text = 'Вес блюда')
        self.tree.heading('edin_izm', text = 'Един. изм. веса')
        self.tree.heading('price', text='Цена, руб')
        self.tree.pack(side = tk.LEFT)    

        # Создание ползунка для пролистывания таблицы
        self.scroll = tk.Scrollbar(self, command = self.tree.yview)
        self.scroll.pack(side = tk.LEFT, fill = tk.Y)
        self.tree.configure(yscrollcommand = self.scroll.set)

            
        self.view_records_cat(cat_name=i)    
            
            
    

#####################################        
                
    def back(self):

        self.label_lh.destroy()
        self.label_lp.destroy()
        self.label.destroy()
        self.label_m.destroy()
        self.label_mh.destroy()
        self.entry_m.destroy()
        self.btn_aut.destroy()
        self.btn_back.destroy()
        self.init_main()
        if self.r_vkl==1:
            self.label_r.destroy()
    
    def edit_complete(self):
        
        EDITCOMP(self.to_menu)

    def menu(self):
        pass



    

#####################################################################################################

class Add(tk.Toplevel):

    # Создание инициализатора
    def __init__(self,to_menu):

        self.to_menu = to_menu

        super().__init__(root)
        self.init_child()
        self.view = app
        

        self.conn = sqlite3.connect(f'{self.to_menu}')

        self.cur = self.conn.cursor()

        
        self.init_child()
        self.default_data()

    # Метод создания и хранения виджетов дочернего окна
    def init_child(self):

        self.title('Добавить категорию')
        self.geometry('400x200')
        self.resizable(False,False)

        # Перехват всех событий происходящих в приложении
        self.grab_set()

        # Захват фокуса
        self.focus_set()

        # Создание строк

        label_name = tk.Label(self, text = 'Название: ')
        label_name.place(x = 50,y = 15) 

        label_numdish = tk.Label(self, text = 'Количесвто блюд: ')
        label_numdish.place(x = 50,y = 55)         

        # Создание полей ввода

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x = 200,y = 15)

        self.entry_namecat = ttk.Entry(self)
        self.entry_namecat.place(x = 200,y = 55)

        # Кнопка закрытия дочернего окна
        self.btn_cancel = ttk.Button(self, text = 'Закрыть', command = self.destroy)
        self.btn_cancel.place(x = 300,y = 170)

        # Кнопка добавления записи
        self.btn_add1 = ttk.Button(self, text = 'Добавить')
        self.btn_add1.place(x = 220,y = 170)
        self.btn_add1.bind('<Button-1>', lambda event: 
                             self.view.records(self.entry_name.get(),
                                               self.entry_namecat.get()))
    ##################################### 

   

    # Метод по выборке всех данных из таблицы с определённым id для выведения этих данных в строке ввода
    def default_data(self):

        select_record_id = self.view.tree.set(self.view.tree.selection()[0],'#1')
        self.cur.execute('''SELECT * FROM Categories WHERE id = ?''',(select_record_id,))

        # Получение доступа к первой записи выборки
        row = self.cur.fetchone()
        self.entry_name.insert(0, row[1])
        self.entry_namecat.insert(0, row[2])
    
    
    



#####################################################################################################    



# Класс поиска записей

class Search(tk.Toplevel):

    # Создание инициализатора
    def __init__(self):

        super().__init__(root)
        self.init_search()
        self.view = app

    # Метод поиска данных 
    def init_search(self):

        self.title('Поиск категории')
        self.geometry('300x130')
        self.resizable(False,False)

        # Перехват всех событий происходящих в приложении
        self.grab_set()

        # Захват фокуса
        self.focus_set()     
        
        # Создание строки
        label_name = tk.Label(self, text = 'Название: ')
        label_name.place(x = 50,y = 50)

        # Создание поля ввода
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x = 135,y = 50)

        # Кнопка закрытия дочернего окна
        self.btn_cancel = ttk.Button(self, text = 'Закрыть', command = self.destroy)
        self.btn_cancel.place(x = 200,y = 80)

        # Кнопка поиска записи
        self.btn_search = ttk.Button(self, text = 'Найти')
        self.btn_search.place(x = 120,y = 80)
        self.btn_search.bind('<Button-1>', lambda event: 
                             self.view.search_records(self.entry_name.get()))   
        
#####################################################################################################

# Класс кнопки редактирования

class Update(tk.Toplevel):

    # Создание инициализатора
    def __init__(self,to_menu):

        self.to_menu = to_menu
        self.conn = sqlite3.connect(f'{self.to_menu}')

        self.cur = self.conn.cursor()

        super().__init__(root)
        self.view = app
        self.init_update()
        self.default_data()

        

    # Метод редактирования данных
    def init_update(self):

        self.title('Редактировать позицию')
        self.geometry('400x200')
        self.resizable(False,False)

        # Перехват всех событий происходящих в приложении
        self.grab_set()

        # Захват фокуса
        self.focus_set()

        # Создание строк

        label_name = tk.Label(self, text = 'Название: ')
        label_name.place(x = 50,y = 15) 

        label_numdish = tk.Label(self, text = 'Количесвто блюд: ')
        label_numdish.place(x = 50,y = 55)         

        # Создание полей ввода

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x = 200,y = 15)

        self.entry_namecat = ttk.Entry(self)
        self.entry_namecat.place(x = 200,y = 55)

        
        self.btn_update = ttk.Button(self, text = 'Редактировать')
        self.btn_update.place(x = 200,y=170)

        # Кнопка закрытия дочернего окна
        self.btn_cancel = ttk.Button(self, text = 'Закрыть', command = self.destroy)
        self.btn_cancel.place(x = 300,y = 170)

        self.btn_update.bind('<Button-1>', lambda event: 
                             self.view.update_record(self.entry_name.get(),
                                                    self.entry_namecat.get()))
        
        self.btn_update.bind('<Button-1>', lambda event: self.destroy(), add = '+')
        self.btn_update.place(x = 200,y = 170)

    # Метод по выборке всех данных из таблицы с определённым id для выведения этих данных в строке ввода
    def default_data(self):

        select_record_id = self.view.tree.set(self.view.tree.selection()[0],'#1')
        self.cur.execute('''SELECT * FROM Categories WHERE id = ?''',(select_record_id))

        # Получение доступа к первой записи выборки
        row = self.cur.fetchone()
        self.entry_name.insert(0, row[1])
        self.entry_namecat.insert(0, row[2])


        
class Add_dish(tk.Toplevel):

    # Создание инициализатора
    def __init__(self,i, to_menu):

        self.to_menu = to_menu
        self.i=i

        super().__init__(root)
        self.init_child()
        self.view = app
        

        self.conn = sqlite3.connect(f'{self.to_menu}')

        self.cur = self.conn.cursor()

        
        self.init_child()
        self.default_data()

    # Метод создания и хранения виджетов дочернего окна
    def init_child(self):

        self.title('Добавить блюдо')
        self.geometry('500x280')
        self.resizable(False,False)

        # Перехват всех событий происходящих в приложении
        self.grab_set()

        # Захват фокуса
        self.focus_set()

        # Создание строк

        label_name = tk.Label(self, text = 'Название: ')
        label_name.place(x = 50,y = 15) 

        label_nameid = tk.Label(self, text = 'ID категории: ')
        label_nameid.place(x = 50,y = 45)  

        label_structure = tk.Label(self, text = 'Состав: ')        
        label_structure.place(x = 50,y = 75)  

        label_serv_weight = tk.Label(self, text = 'Вес блюда: ')
        label_serv_weight.place(x=50,y=105)

        label_edin_izm = tk.Label(self, text = 'Единица измерения веса: ')
        label_edin_izm.place(x=50,y=135)

        label_price = tk.Label(self, text = 'Цена, руб:')
        label_price.place(x=50, y=165)
        # Создание полей ввода

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x = 200,y = 15)

        self.entry_nameid = ttk.Entry(self)
        self.entry_nameid.place(x = 200,y = 45)

        self.entry_structure = ttk.Entry(self)
        self.entry_structure.place(x=200,y=75)

        self.entry_serv_weight = ttk.Entry(self)
        self.entry_serv_weight.place(x=200,y=105)

        self.entry_edin_izm = ttk.Entry(self)
        self.entry_edin_izm.place(x=200,y = 135)

        self.entry_price = ttk.Entry(self)
        self.entry_price.place(x=200,y=165)


        # Кнопка закрытия дочернего окна
        self.btn_cancel = ttk.Button(self, text = 'Закрыть', command = self.destroy)
        self.btn_cancel.place(x = 300,y = 200)

        # Кнопка добавления записи
        self.btn_add1 = ttk.Button(self, text = 'Добавить')
        self.btn_add1.place(x = 220,y = 200)
        self.btn_add1.bind('<Button-1>', lambda event: 
                             self.view.records_dish(self.entry_nameid.get(),
                                               self.entry_name.get(),                                               
                                               self.entry_structure.get(),
                                               self.entry_serv_weight.get(),
                                               self.entry_edin_izm.get(),
                                               self.entry_price.get()),)
        
    ##################################### 

   

    # Метод по выборке всех данных из таблицы с определённым id для выведения этих данных в строке ввода
    def default_data(self):

        select_record_id = self.view.tree.set(self.view.tree.selection()[0],'#1')
        self.cur.execute(f'''SELECT * FROM {self.i} WHERE id_dish = ?''',(select_record_id))

        # Получение доступа к первой записи выборки
        row = self.cur.fetchone()
        self.entry_nameid.insert(0,row[1])
        self.entry_name.insert(0, row[2])
        self.entry_structure.insert(0,row[3])
        self.entry_serv_weight.insert(0,row[4])
        self.entry_edin_izm.insert(0,row[5])
        self.entry_price.insert(0,row[6])
    
    
 
        
#####################################################################################################
class Search_dish(tk.Toplevel):

    # Создание инициализатора
    def __init__(self,i):

        super().__init__(root)
        self.init_search()
        self.view = app
        self.i=i

    # Метод поиска данных 
    def init_search(self):

        self.title('Поиск блюда')
        self.geometry('300x130')
        self.resizable(False,False)

        # Перехват всех событий происходящих в приложении
        self.grab_set()

        # Захват фокуса
        self.focus_set()     
        
        # Создание строки
        label_name = tk.Label(self, text = 'Название блюда: ')
        label_name.place(x = 30,y = 50)

        # Создание поля ввода
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x = 135,y = 50)

        # Кнопка закрытия дочернего окна
        self.btn_cancel = ttk.Button(self, text = 'Закрыть', command = self.destroy)
        self.btn_cancel.place(x = 200,y = 80)


        # Кнопка поиска записи
        self.btn_search = ttk.Button(self, text = 'Найти')
        self.btn_search.place(x = 120,y = 80)
        self.btn_search.bind('<Button-1>', lambda event: 
                             self.view.search_records_dish(self.i, self.entry_name.get()))
        
#####################################################################################################       
# Класс кнопки редактирования


class Update_dish(tk.Toplevel):

    # Создание инициализатора
    def __init__(self,i,to_menu):

        self.to_menu = to_menu
        self.conn = sqlite3.connect(f'{self.to_menu}')

        self.cur = self.conn.cursor()

        super().__init__(root)
        self.view = app
        self.i=i
        self.init_update()
        self.default_data()

        

    # Метод редактирования данных
    def init_update(self):

        self.title('Редактировать позицию')
        self.geometry('500x280')
        self.resizable(False,False)

        # Перехват всех событий происходящих в приложении
        self.grab_set()

        # Захват фокуса
        self.focus_set()

        # Создание строк

        label_name = tk.Label(self, text = 'Название: ')
        label_name.place(x = 50,y = 15) 

        label_nameid = tk.Label(self, text = 'ID категории: ')
        label_nameid.place(x = 50,y = 45)  

        label_structure = tk.Label(self, text = 'Состав: ')        
        label_structure.place(x = 50,y = 75)  

        label_serv_weight = tk.Label(self, text = 'Вес блюда: ')
        label_serv_weight.place(x=50,y=105)

        label_edin_izm = tk.Label(self, text = 'Единица измерения веса: ')
        label_edin_izm.place(x=50,y=135)

        label_price = tk.Label(self, text = 'Цена, руб:')
        label_price.place(x=50, y=165)
        # Создание полей ввода

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x = 200,y = 15)

        self.entry_nameid = ttk.Entry(self)
        self.entry_nameid.place(x = 200,y = 45)

        self.entry_structure = ttk.Entry(self)
        self.entry_structure.place(x=200,y=75)

        self.entry_serv_weight = ttk.Entry(self)
        self.entry_serv_weight.place(x=200,y=105)

        self.entry_edin_izm = ttk.Entry(self)
        self.entry_edin_izm.place(x=200,y = 135)

        self.entry_price = ttk.Entry(self)
        self.entry_price.place(x=200,y=165)


        # Кнопка закрытия дочернего окна
        self.btn_cancel = ttk.Button(self, text = 'Закрыть', command = self.destroy)
        self.btn_cancel.place(x = 300,y = 200)
        
        self.btn_update = ttk.Button(self, text = 'Редактировать')
        self.btn_update.place(x = 200,y=200)


        self.btn_update.bind('<Button-1>', lambda event: 
                             self.view.update_record_dish(self.entry_nameid.get(),
                                                        self.entry_name.get(),                                               
                                                        self.entry_structure.get(),
                                                        self.entry_serv_weight.get(),
                                                        self.entry_edin_izm.get(),
                                                        self.entry_price.get()))
        
        self.btn_update.bind('<Button-1>', lambda event: self.destroy(), add = '+')
        self.btn_update.place(x = 200,y = 200)

    # Метод по выборке всех данных из таблицы с определённым id для выведения этих данных в строке ввода
    def default_data(self):

        select_record_id = self.view.tree.set(self.view.tree.selection()[0],'#1')
        self.cur.execute(f'''SELECT * FROM {self.i} WHERE id_dish = ?''',(select_record_id))

        # Получение доступа к первой записи выборки
        row = self.cur.fetchone()
        self.entry_nameid.insert(0,row[1])
        self.entry_name.insert(0, row[2])
        self.entry_structure.insert(0,row[3])
        self.entry_serv_weight.insert(0,row[4])
        self.entry_edin_izm.insert(0,row[5])
        self.entry_price.insert(0,row[6])

#####################################################################################################
    
class EDITCOMP(tk.Toplevel):

     # Создание инициализатора
    def __init__(self,to_menu):
        self.to_menu=to_menu
        super().__init__(root)
        self.init_edcom()
        self.view = app

    # Метод поиска данных 
    def init_edcom(self):

        self.title('Переход к меню')
        self.geometry('600x200')
        self.resizable(False,False)

        # Перехват всех событий происходящих в приложении
        self.grab_set()

        # Захват фокуса
        self.focus_set()     

        self.label_q=tk.Label(self,text='Вы уверены, что закончили редактирование меню?',font=['Times new roman','17'])
        self.label_q.place(x=50,y=30)

        self.btn_da=tk.Button(self,text = 'Да', bg ='White',font=['arial','10'],width=25,
                            bd = 3, command=self.da)
        self.btn_da.place(x=340, y=100)

        self.btn_net=tk.Button(self,text = 'Нет', bg ='White',font=['arial','10'],width=25,
                            bd = 3, command=self.destroy)
        self.btn_net.place(x=50, y=100)          
        
        self.label_opov = tk.Label(self,text="При переходе в вариант меню для посетителя, возможность вернуться \nк редактору меню будет только с помощью повторной авторизации.",
                                   foreground="#696969", font=['arial','10'])
        self.label_opov.place(x=70,y=140)

    def da(self):
        self.destroy()
        Menu(root_m=root,to_menu=self.to_menu)

#####################################################################################################
class Menu(tk.Frame):

    def __init__(self,root_m,to_menu:str):

        self.conn = sqlite3.connect(f'{to_menu}')

        self.cur = self.conn.cursor()
        
        self.to_menu=to_menu.replace('.db','')
        super().__init__(root)
        self.init_menu()
        self.root_m=root_m
    
    def init_menu(self):
        
        root.title(f'Меню {self.to_menu}')
        root.geometry('800x700')   
        root.configure(bg='#140E9B')
        root.resizable(False,False)

        for widget in root.winfo_children():
            widget.destroy()
    
        with open('menuname.json', 'r', encoding='utf-8') as lvl:
            menu_names_slov = json.load(lvl)

        self.menu_name= menu_names_slov['1'].split('_')

        if self.menu_name and self.menu_name[-1] == '':
            self.menu_name.pop()

        num_buttons = len(self.menu_name)

        self.exit_img=tk.PhotoImage(file='img\Settings.png')

        for i in range(num_buttons):
            btn = tk.Button(root, text=self.menu_name[i], bg='#34FAB6', bd=6, font=['Arial','15','bold'],
                            width=13,height=7, relief='groove',
                            command= lambda i=i: self.menu(self.menu_name[i].replace(' ','_')))
            if num_buttons>4:

                if i<=3:
                    btn.place(x=(420/num_buttons)+i*180,y=40)
                if i>3:
                    btn.place(x=(420/num_buttons)+(i-4)*180,y=310)

            if num_buttons<=4:
                
                btn.place(x=(420/num_buttons)+i*180,y=210)

        
        self.exit_btn=tk.Button(root,text = 'Настройки', bg ='#34FAB6', relief='groove',bd = 4,
                                 image = self.exit_img, command=self.restarting)
        self.exit_btn.place(x=727,y=0)

    def restarting(self):
        
        for widget in root.winfo_children():
            widget.destroy()

        
        subprocess.Popen(["pythonw.exe", 'Web.py'])
    def menu(self,menu_name_):

        for widget in root.winfo_children():
            widget.destroy()
        menu_name_=menu_name_.replace('_',' ')
        root.title(f'Категория {menu_name_}')
        menu_name_=menu_name_.replace(' ','_')
        root.geometry('600x700')
        root.configure(bg = '#140E9B')
        root.resizable(False,False) 
        
        if '.db' in self.to_menu:
            pass
        else:
            self.to_menu=self.to_menu+'.db'

        self.conn = sqlite3.connect(f'{self.to_menu}')

        self.cur = self.conn.cursor()

        self.cur.execute(f'''SELECT name FROM {menu_name_}''',)

        self.listic = list(self.cur.fetchall())
        for i in range(len(self.listic)):
            self.listic[i]=str(self.listic[i][0])

        self.toolbar = tk.Frame( bd = 2, background='#140E9B')
        self.toolbar.pack(side = tk.TOP, fill=tk.X)

        self.btn_btn = tk.Button(self.toolbar,text='Назад',bg='#34FAB6',command=self.back)
        self.btn_btn.pack(side = tk.LEFT)

        for i in range(len(self.listic)):
            self.cur.execute(f'''SELECT serv_weight FROM {menu_name_} WHERE name LIKE ?''',(self.listic[i],))
            self.serv_weight = str(self.cur.fetchall()[0][0])

            self.cur.execute(f'''SELECT edin_izm FROM {menu_name_} WHERE name LIKE ?''',(self.listic[i],))
            self.serv_weight = self.serv_weight + self.cur.fetchall()[0][0]

            self.cur.execute(f'''SELECT price FROM {menu_name_} WHERE name LIKE ?''',(self.listic[i],))
            self.price = str(self.cur.fetchall()[0][0])+'руб'
            if len(self.listic[i])>5:
                self.listic[i]=' '*(26-math.ceil((len(self.listic[i])-5)/2))+self.listic[i]+' '*(33-math.ceil((len(self.listic[i])-3)/2))+self.serv_weight+' '*9+self.price

            if len(self.listic[i])==5:
                self.listic[i]=' '*26+self.listic[i]+' '*(33)+self.serv_weight+' '*9+self.price
        
            if len(self.listic[i])<5:
                self.listic[i]=' '*(26+(math.ceil((len(self.listic[i])-5)/2)*(-1)))+self.listic[i]+' '*(33+(math.ceil((len(self.listic[i])-5)/2)*(-1))+5)+self.serv_weight+' '*9+self.price


        self.dish_list=tk.Variable(value=['                          Блюдо                                 Вес             Цена']+self.listic)
        
        self.dish_listbox = tk.Listbox(listvariable=self.dish_list,font=['arial','15'],width=53,height=29,bg='#140E9B',fg='#34FAB6',selectbackground='#34FAB6',selectmode='SINGLE')
 
        self.dish_listbox.pack(side=tk.LEFT)
        self.dish_listbox.bind("<<ListboxSelect>>",self.select_struct)

        self.cat_name=menu_name_


        self.scroll = ttk.Scrollbar(orient="vertical", command = self.dish_listbox.yview)
        self.scroll.pack(side = tk.RIGHT, fill = tk.Y)
        self.dish_listbox.yview_scroll(number=1, what="units")

    def back(self):
        for widget in root.winfo_children():
            widget.destroy()      
        self.init_menu()

    def select_struct(self,event):

        self.selected_indices = self.dish_listbox.curselection()

        self.name = (self.dish_listbox.get(self.selected_indices[0])).replace(' ','')[:-10]
        if self.name=='Бл':
            return
        SOSTAV(self.root_m,self.to_menu,self.name,self.cat_name)

class SOSTAV(tk.Toplevel):

    def __init__(self,root_s,to_menu,name,cat_name):
        
        super().__init__(root_s)
        self.to_menu=to_menu
        self.cat_name=cat_name
        self.view=app
        self.name=name
        self.init_sostav()
        
        
    def init_sostav(self):
        
        self.title('Состав')
        self.geometry('300x200')
        self.resizable(False,False)

        # Перехват всех событий происходящих в приложении
        self.grab_set()

        # Захват фокуса
        self.focus_set()   

        self.conn = sqlite3.connect(f'{self.to_menu}')

        self.cur = self.conn.cursor() 

        self.cur.execute(f'''SELECT structure FROM {self.cat_name} WHERE name LIKE ?''',(self.name,))

        self.struct = self.cur.fetchall()[0][0]
        if '.' in self.struct:
            pass
        else: self.struct=self.struct+'.'
        self.label = tk.Label(self, text=f'Состав блюда "{self.name}":', font=['Arial','16'])
        self.label.place(x=20,y=30)

        self.label_sostav = tk.Label(self,text=self.struct,font=['Arial','13', "italic"], wraplength=260,justify="left")
        self.label_sostav.place(x=30, y=60)

        self.btn_destroy = tk.Button(self,text = 'Закрыть', bg ='White',font=['arial','10'],width=15,
                            bd = 3, command=self.destroy)
        self.btn_destroy.place(x=150,y=160)
    
          



if __name__ == '__main__':

    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Создание меню')
    root.geometry('1000x700')
    root.configure(bg = 'White')
    root.resizable(False,False)

    root.mainloop()

