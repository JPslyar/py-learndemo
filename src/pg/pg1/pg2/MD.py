x = 'pg2_MD'
print(__name__)

#下面可应用于模板的单元测试，即只有当前模板为顶层运行
#模板时才运行，当该模板被作为工具导入时不会运行
if __name__ == '__main__':
    print('单元测试代码')

