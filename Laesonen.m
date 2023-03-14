clear;clc;
h=input('enter value of h');
k=input('enter value of k');
c=input('enter value of c');
w=(c^2*k)/h^2;
x=0:h:1;
t=0:k:1;
m=length(x);
n=length(t);
u=zeros(m,n);
IC=sin(pi*x);
u(:,1)=IC';
u([end,1],:)=0;
PD=ones(m-2,1);
SD=ones(m-3,1);
A=diag((1+2*w)*PD)+diag(-w*SD,1)+diag(-w*SD,-1);
for j=2:n-1
    C_1=u((2:end-1),j-1);
    C_2=[u(1,j);zeros(m-4,1);u(end,j)];
    B=C_1+C_2;
    u((2:end-1),j)=inv(A)*B;
end
u
surf(u);
xlabel('x');
ylabel('t');
zlabel('u');
title('HEAT EQUATION');
% 
% 
% 
% clear;clc;
% h=input('enter value of h');
% k=input('enter value of k');
% c=input('enter value of c');
% w=(c^2*k)/h^2;
% x=-1:h:1;
% t=0:k:1;
% m=length(x);
% n=length(t);
% u=zeros(m,n);
% IC=cos((pi*x)/2);
% u(:,1)=IC';
% u([end,1],:)=0;
% PD=ones(m-2,1);
% SD=ones(m-3,1);
% A=diag((1+2*w)*PD)+diag(-w*SD,1)+diag(-w*SD,-1);
% for j=2:n-1
%     C_1=u((2:end-1),j-1);
%     C_2=[u(1,j);zeros(m-4,1);u(end,j)];
%     B=C_1+C_2;
%     u((2:end-1),j)=inv(A)*B;
% end
% u
% surf(u);
% xlabel('x');
% ylabel('t');
% zlabel('u');
% title('HEAT EQUATION');
% 
% 
% clear;clc;
% h=input('enter value of h');
% k=input('enter value of k');
% c=input('enter value of c');
% w=(c^2*k)/h^2;
% x=0:h:1;
% t=0:k:1;
% m=length(x);
% n=length(t);
% u=zeros(m,n);
% if (0<=x<=1/2)
%     IC=x;
% else
%     IC=(1-x);
% end
% u(:,1)=IC';
% u([end,1],:)=0;
% PD=ones(m-2,1);
% SD=ones(m-3,1);
% A=diag((1+2*w)*PD)+diag(-w*SD,1)+diag(-w*SD,-1);
% for j=2:n-1
%     C_1=u((2:end-1),j-1);
%     C_2=[u(1,j);zeros(m-4,1);u(end,j)];
%     B=C_1+C_2;
%     u((2:end-1),j)=inv(A)*B;
% end
% u
% surf(u);
% xlabel('x');
% ylabel('t');
% zlabel('u');
% title('HEAT EQUATION');