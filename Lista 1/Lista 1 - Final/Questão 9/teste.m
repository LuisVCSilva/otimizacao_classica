clear all
close all
clc

x1=[-0.4:0.01:1];
x2=[-0.4:0.01:1];

[X,Y]=meshgrid(x1,x2);
f=-pi.*X.*Y;
%Curvas de nível
contour(X,Y,f,30);
%--------------------------------------------------------------------------
%Plota os pontos encontrados
hold on;
plot(0.7371,0.0340,'*r');
hold on;
plot(-0.0852,0.1299,'*b');
%--------------------------------------------------------------------------
%Restrições laterais
X1=[0:0.001:0.6];
X2=[0:0.001:0.12];
hold on;
plot(X1,0,'k','LineWidth',2);
hold on;
plot(X1,0.12,'k', 'LineWidth',2)
hold on;
plot(0,X2,'k', 'LineWidth',2);
hold on;
plot(0.6,X2,'k', 'LineWidth',2);
%--------------------------------------------------------------------------
xlabel('x1');
ylabel('x2');
%title('Questao 9');
legend('f(x)','P1 = (0.7371, 0.0340)', 'P2 = (-0.0852, 0.1299)','Restricoes laterais') % inserir legenda, na ordem
pause;
