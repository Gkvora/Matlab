clear;clc
t=0:0.1:10;
S=0.7;I=0.3;
[t,sol]=ode45(@SI_1,t,[S I]);
plot(t,sol(:,1),'r')
hold on
plot(t,sol(:,2),'k')
grid on;
xlabel('t');
ylabel('p');
legend('S','I');
title('SI-Model');