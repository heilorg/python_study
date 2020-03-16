from tkinter import *
import requests
from bs4 import BeautifulSoup as bs

class GUILunch() :
    def __init__(self):
        self.app = Tk()
        self.app.geometry('300x200')
        self.app.title('수정과 급식알리미')

        self.lblTitle = Label(self.app, text="수정과 급식 파싱")
        self.lblTitle.pack()

        self.frmButtonSet = Frame(self.app)
        self.frmButtonSet.pack()

        self.txtDate = Text(self.frmButtonSet, width=20, height=1, bd=1)
        self.txtDate.bind('<Return>', self.getEnterKey)
        self.txtDate.grid(row=0, column=0)
        self.txtDate.focus()

        self.btnLoad = Button(self.frmButtonSet, text="급식 가져오기", width=20, command=self.getLunchData)
        self.btnLoad.grid(row=0, column=1)

        self.lblMenuList = Label(self.app, text="메뉴 나오는 곳", height=5, width=40)
        self.lblMenuList.pack()

    def getEnterKey(self, event) :
        self.getLunchData()
        self.txtDate.delete('1.0', END)

    def run(self):
        self.app.mainloop()

    def getLunchData(self) :
        req = requests.get('http://swjb.hs.kr/lunch.view?date=' + self.txtDate.get("1.0", END))
        html = req.text
        soup = bs(html, 'html.parser')
        meals = soup.select('#morning span')
        menuStr = "급식이 없습니다."
        if len(meals) > 0 :
            menuStr = meals[0].text
        print(menuStr)
        self.lblMenuList.config(text=menuStr)

mainApp = GUILunch()
mainApp.run()

# pyinstaller --onefile lunch_GUI.py
# pyinstaller --noconsole --onefile lunch_GUI.py
