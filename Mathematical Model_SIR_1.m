function dydt=SIR_1(t,y)
A=0.8;B=0.2;C=0.05;
dydt=[-A*y(1)*y(2)+C*y(3);A*y(1)*y(2)-B*y(2);B*y(2)-C*y(3)];
end