import subprocess
import os
import matlab.engine    
#1. 查找MATLAB路径
#在matlab中输入matlab.engine.shareEngine

def find_matlab():
    try:
        # 执行'where matlab'命令
        result = subprocess.run(['where', 'matlab'], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip().split('\n')[0]  # 返回第一个路径
    except:
        pass
# 2. 启动MATLAB
def launch_matlab():
    matlab_path = find_matlab()
    if matlab_path:
        print(f"找到MATLAB: {matlab_path}")
        subprocess.Popen([matlab_path])
        print("MATLAB已启动")
        return True
    else:
        print("未找到MATLAB")
        return False 
if __name__ == "__main__":
    #launch_matlab()
    a=matlab.engine.find_matlab()
    eng=matlab.engine.connect_matlab(a[0])
    eng.cd(r'E:\example')
    #工作空间
    eng.eval('b=1',nargout=0)

    x=2.0
    eng.workspace['y']=x
   
    c=eng.eval('y+b',nargout=1)
    print(c)
    eng.exit()

