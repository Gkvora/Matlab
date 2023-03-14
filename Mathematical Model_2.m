function dxdt = model_2(t,y)
g=9.8;
k=1;
dxdt=[y(2);g-k*y(2)];