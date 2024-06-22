import wx

# 创建 app 对象
app = wx.App()

# 创建窗口
frame = wx.Frame(None, title='学习软件', size=(1000, 800), pos=(500, 100))
# 显示窗口
frame.Show()

# 创建面板
panel = wx.Panel(frame, size=(1000, 800))
panel.Show()

# 创建文本
text = wx.StaticText(panel, label='Hello world!', pos=(100, 100))
text.Show()

# 创建按钮
btn = wx.Button(panel, label='Click Me!')
btn.Show()

def on_click(e):
    print('点击按钮')

# 添加点击事件
frame.Bind(wx.EVT_BUTTON, on_click, btn)

# 进入主循环，让窗口一直显示
app.MainLoop()
