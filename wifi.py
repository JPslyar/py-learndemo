#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import wx
import ConfigParser
myconfig=ConfigParser.ConfigParser()
myconfig.read('config.ini')
new_ssid=str(myconfig.get('ssid', 'myssid'))
new_passwd=str(myconfig.get('passwd','mypasswd'))
new_security=str(myconfig.get('security_type','mysecurity'))
new_showpwd=str(myconfig.get('showpwd','showpwd'))
new_security_dict={'WPA2':0,'无身份验证(开放式)':1}




class frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Wi-Fi共享帮手",size=(390,240),style=wx.CAPTION|wx.MINIMIZE_BOX|wx.CLOSE_BOX)
        self.panel=wx.Panel(self,-1)
        ssid=wx.StaticText(self.panel,-1,"网络SSID:",pos=(15,20))
        self.ssid_input=wx.TextCtrl(self.panel,-1,value=new_ssid,size=(225,20),pos=(80,20))
        self.ssid_input.Refresh()
        self.ssid_input.SetMaxLength(31)
        self.ssid_input.Bind(wx.EVT_TEXT,self.ssid_evt)
        lenssid=wx.StaticText(self.panel,-1,"(1-31个字符)",pos=(310,20))
        security=wx.StaticText(self.panel,-1,"网络安全类型:",pos=(15,50))
        self.security=wx.ComboBox(self.panel,-1,choices=['WPA2','无身份验证(开放式)'],pos=(100,50))
        self.security.Select(new_security_dict[new_security])
        self.security.Bind(wx.EVT_COMBOBOX, self.security_evt)
        self.passwd_st=wx.StaticText(self.panel,-1,"网络密钥:",pos=(15,80))
        self.passwd=wx.TextCtrl(self.panel,-1,value=new_passwd,style=wx.TE_PASSWORD,size=(225,25),pos=(75,80))
        self.passwd_no=wx.TextCtrl(self.panel,-1,value=new_passwd,size=(225,25),pos=(75,80))
        self.passwd_no.Bind(wx.EVT_TEXT, self.passwd_no_evt)
        self.passwd.Bind(wx.EVT_TEXT, self.passwd_evt)
        self.passwd.SetMaxLength(63)
        self.lenpwd=wx.StaticText(self.panel,-1,"(8-63个字符)",pos=(310,80))
        self.showpwd=wx.CheckBox(self.panel,-1,"显示密钥字符",pos=(15,110))
        self.showpwd.Bind(wx.EVT_CHECKBOX,self.showpwd_evt)
        self.value=wx.CheckBox(self.panel,-1,"保存这个网络设置",pos=(115,110))
        self.value.Bind(wx.EVT_CHECKBOX,self.value_evt)
        self.auto=wx.CheckBox(self.panel,-1,"开机自动启动Wi-Fi共享",pos=(235,110))
        self.auto.Bind(wx.EVT_CHECKBOX, self.auto_evt)
        self.start_wifi=wx.Button(self.panel,-1,"开启Wi-Fi",pos=(15,150))
        self.start_wifi.Bind(wx.EVT_BUTTON,self.start_wifi_evt)
        self.stop_wifi=wx.Button(self.panel,-1,"关闭Wi-Fi",pos=(120,150))
        self.stop_wifi.Bind(wx.EVT_BUTTON,self.stop_wifi_evt)
        if  myconfig.get('windows','start_on_windows')=='true':
            self.auto.SetValue(True)
        else:
            self.auto.SetValue(False)
        if myconfig.get('save_config','save_config')=='true':
            self.value.SetValue(True)
        else:
            self.value.SetValue(False)
        if str(self.security.GetValue())=="无身份验证(开放式)":
            self.passwd.Hide()
            self.passwd_st.Hide()
            self.lenpwd.Hide()
            self.passwd_no.Hide()
            self.showpwd.Disable()
        if new_showpwd=="true":
            self.passwd.Hide()
            self.showpwd.SetValue(True)
        else:
            self.passwd_no.Hide()
            self.showpwd.SetValue(False)
    def showpwd_evt(self,evt):
        if self.showpwd.GetValue() is True:
            self.passwd.Hide()
            self.passwd_no.Show()
            myconfig.set('showpwd','showpwd','true')
            myconfig.write(open('config.ini','w'))
        else:
            self.passwd_no.Hide()
            self.passwd.Show()
            myconfig.set('showpwd','showpwd','false')
            myconfig.write(open('config.ini','w'))
    def auto_evt(self,evt):
        if myconfig.get('windows','start_on_windows')=='true':
            myconfig.set('windows', 'start_on_windows', 'false')
            myconfig.write(open('config.ini','w'))
        else:
            myconfig.set('windows', 'start_on_windows', 'true')
            myconfig.write(open('config.ini','w'))
    def value_evt(self,evt):
        if myconfig.get('save_config','save_config')=='true':
            myconfig.set('save_config','save_config','false')
            myconfig.set('ssid','myssid','')
            myconfig.set('passwd','mypasswd','')
            myconfig.set('security_type','mysecurity','WPA2')
            myconfig.write(open('config.ini','w'))
        else:
            myconfig.set('save_config','save_config','true')
            myconfig.set('ssid','myssid',str(self.ssid_input.GetValue()))
            myconfig.set('passwd','mypasswd',str(self.passwd.GetValue()))
            myconfig.set('security_type','mysecurity',str(self.security.GetValue()))
            myconfig.write(open('config.ini','w'))
    def ssid_evt(self,evt):
        myconfig.set('ssid','myssid',str(self.ssid_input.GetValue()))
        myconfig.write(open('config.ini','w'))
    def passwd_evt(self,evt):
        myconfig.set('passwd','mypasswd',str(self.passwd.GetValue()))
        myconfig.write(open('config.ini','w'))
        self.passwd_no.SetValue(self.passwd.GetValue())
    def passwd_no_evt(self,evt):
        myconfig.set('passwd','mypasswd',str(self.passwd_no.GetValue()))
        myconfig.write(open('config.ini','w'))
        self.passwd.SetValue(self.passwd_no.GetValue())
    def security_evt(self,evt):
        myconfig.set('security_type','mysecurity',str(self.security.GetValue()))
        myconfig.write(open('config.ini','w'))
        if str(self.security.GetValue())=="无身份验证(开放式)":
            self.passwd.Hide()
            self.passwd_st.Hide()
            self.lenpwd.Hide()
            self.passwd_no.Hide()
            self.showpwd.Disable()
        else:
            self.showpwd.Enable()
            self.passwd_st.Show()
            self.lenpwd.Show()
            if self.showpwd.GetValue() is True:
                self.passwd_no.Show()
            else:
                self.passwd.Show()
            
    def start_wifi_evt(self,evt):
        os.system("net start wlansvc")
        os.system("netsh wlan set hostednetwork mode=allow")
        if str(self.security.GetValue())=="无身份验证(开放式)":
            self.passwd.SetValue("")
        os.system("netsh wlan set hostednetwork ssid=%s key=%s"%(self.ssid_input.GetValue(),self.passwd.GetValue()))
        os.system("netsh wlan start hostednetwork")
        self.start_wifi.Disable()
    def stop_wifi_evt(self,evt):
        os.system("netsh wlan stop hostednetwork")
        self.start_wifi.Enable()


    
            




class app(wx.App):
    def OnInit(self):
        myframe=frame()
        myframe.Show()
        return True
if __name__=="__main__":
    myapp=app()
    myapp.MainLoop()
    