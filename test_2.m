clear;clc
t=0:0.1:10;
S=0.7;I=0.2;R=0.1;
[t,sol]=ode45(@SIR_1,t,[S I R]);
plot(t,sol(:,1),'r')
hold on
plot(t,sol(:,2),'k')
hold on
plot(t,sol(:,3),'g')
grid on;
xlabel('t');
ylabel('p');
legend('S','I','R');
title('SIR-Model');