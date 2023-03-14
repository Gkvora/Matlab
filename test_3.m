clear;clc
t=0:0.1:10;
S=0.6;E=0.2;I=0.1;R=0.1;
[t,sol]=ode45(@SEIR_1,t,[S E I R]);
plot(t,sol(:,1),'r')
hold on
plot(t,sol(:,2),'k')
hold on
plot(t,sol(:,3),'g')
hold on
plot(t,sol(:,4),'m')
grid on;
xlabel('t');
ylabel('p');
legend('S','E','I','R');
title('SEIR-Model');