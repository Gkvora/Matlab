function dydt=SEIRv_1(t,y)
A=0.6;
B=0.4;
C=0.05;
D=0.06;
X=0.03;
V=1;
dydt=[-A*y(1)*y(2)+D*y(4)-V*y(1);A*y(1)*y(2)-B*y(2)*y(3)+X*y(4);B*y(2)*y(3)-C*y(3);C*y(3)+V*y(1)-X*y(4)-D*y(4)];
end