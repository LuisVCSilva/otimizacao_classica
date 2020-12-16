clear all
close all
clc

x=linspace(0,pi/4, 45);
y=1250-1250*cos(x)-250*sin(x);


plot(x,y);

%--------------------------------------------------------------------------
%xlabel('teta');
%ylabel('PE');
% title('PE vs teta');
%legend('Energia potencial');
%--------------------------------------------------------------------------

 hold on;
 x=0.1974;%minimo
 f=y;
 plot(x,-24.7549,'*r');
 xlabel('theta');
 ylabel('PE');
  title('PE vs theta');
 legend('Energia potencial','Energia potencial minima');
pause;
