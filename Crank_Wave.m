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
PD=ones(m-2,1);
SD=ones(m-3,1);
A=diag(1*PD)+diag((w/4)*SD,1)+diag((-w/4)*SD,-1);
for j=2:n-1
    C_1=(w/4)*u(1,j-1)+u(2,j-1)+(-w/4)*u(3,j-1);
    for i=3:m-1
        S=(w/4)*u(i-1,j-1)+u(i,j-1)+(-w/4)*u(i+1,j-1);
        C_1=[C_1;S];
    end
    C_2=[u(1,j);zeros(m-4,1);u(end,j)];
    B=C_1+C_2;
    u([2:end-1],j)=inv(A)*B;
     end
u
surf(u);
xlabel('x');
ylabel('t');
zlabel('u');
title('WAVE EQAUTION')