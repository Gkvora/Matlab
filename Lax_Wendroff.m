clear;clc;
h=input('enter value of h');
k=input('enter value of k');
c=input('enter value of c');
w=(c*k)/h;
x=0:h:300;
t=0:k:1;
m=length(x);
n=length(t);
u=zeros(m,n);
for i=1:m
    if (x(i)>=0&&x(i)<=50)
    IC(i)=0;
elseif (x(i)>=50&&x(i)<=110)
    IC(i)=100*sin(pi*(x(i)-50)/60);
else
    IC(i)=0;
    end
end
u(:,1)=IC';
u([1,end],:)=0;
for j=1:n-1
    for i=2:m-1
        u(i,j+1)=(1-w^2)*u(i,j)+(w/2)*(w-1)*u(i+1,j)+(w/2)*(w+1)*u(i-1,j);
    end
end
u
surf(u);
xlabel('x');
ylabel('t');
zlabel('u');
title('Wave Equation');