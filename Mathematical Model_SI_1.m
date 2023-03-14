function dydt=SI_1(t,y)
a=0.8;b=0.2;
dydt=[-a*y(1)*y(2)+b*y(2);a*y(1)*y(2)-b*y(2)];
end