h=getSimulinkBlockHandle('test/Sine',true);
%i=get_param(h,'ObjectParameters')获取对象所有参数名/信息
i=get_param(h,'DialogParameters');
load_system("test.slx")
set_param('test','StopTime','20')
set_param('test/Sine','Amplitude','10')
sim("test.slx")

plot(tout,sin.Data)
