clear;clc;
t=0:0.1:10;
[t,sol]=ode45(@model_1,t,[0,0]);
plot(t,sol(:,2),'r');
grid on
title('Free Falling')