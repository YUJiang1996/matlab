import matlab.engine

import matplotlib.pyplot as plt
eng = matlab.engine.start_matlab()
eng.cd(r'E:\example')
eng.load_system('test')
eng.set_param('test','StopTime','10',nargout=0)
eng.set_param('test/Sine','Amplitude','2',nargout=0)
eng.sim('test',nargout=0)
x=eng.workspace['tout']
print(x)

y=eng.workspace['sin']
print(y)
plt.plot(x,y)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sine Wave')
plt.show()
eng.quit()