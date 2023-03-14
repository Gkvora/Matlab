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
j=1;
for i=2:m-1
    u(i,j+1)=w*u(i+1,j)+(1-2*w)*u(i,j)+w*u(i-1,j);
end
for j=2:n-1
    for i=2:m-1
        u(i,j+1)=u(i,j-1)+2*w*u(i+1,j)-4*w*u(i,j)+2*w*u(i-1,j);
    end
end
u
surf(u);
xlabel('x');
ylabel('t');
zlabel('u');
title('Heat Equation');
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
% j=1;
% for i=2:m-1
%     u(i,j+1)=w*u(i+1,j)+(1-2*w)*u(i,j)+w*u(i-1,j);
% end
% for j=2:n-1
%     for i=2:m-1
%         u(i,j+1)=u(i,j-1)+2*w*u(i+1,j)-4*w*u(i,j)+2*w*u(i-1,j);
%     end
% end
% u
% surf(u);
% xlabel('x');
% ylabel('t');
% zlabel('u');
% title('Heat Equation');
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
% j=1;
% for i=2:m-1
%     u(i,j+1)=w*u(i+1,j)+(1-2*w)*u(i,j)+w*u(i-1,j);
% end
% for j=2:n-1
%     for i=2:m-1
%         u(i,j+1)=u(i,j-1)+2*w*u(i+1,j)-4*w*u(i,j)+2*w*u(i-1,j);
%     end
% end
% u
% surf(u);
% xlabel('x');
% ylabel('t');
% zlabel('u');
% title('Heat Equation');