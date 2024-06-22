import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='自制学习软件')
        panel = wx.Panel(self)
        wx.StaticText(panel, label='Hello world!', pos=(50, 50))
        btn = wx.Button(panel, label='hello')
        self.Bind(wx.EVT_BUTTON, lambda e: print('Hello'), btn)

app = wx.App()

frame = MyFrame()
frame.Show()

app.MainLoop()
