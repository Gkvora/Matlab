clear;clc;
R=input('enter right boundary value');
L=input('enter left boundary value');
T=input('enter top boundary value');
B=input('enter bottom boundary value');
if (length(R)~=length(L)&&length(T)~=length(B)&&R(end)~=T(end)&&R(1)~=B(end)&&L(1)~=B(1)&&L(end)~=T(1))
    disp('Boundary Is Not Matched')
else
    m=length(L);n=length(B);
    u=zeros(m,n);
    u(:,1)=L;
    u(:,end)=R;
    u(1,:)=B;
    u(end,:)=T;
    h=1/(m-1);
    k=1/(n-1);
    for W=1:4
        for j=2:n-1
            for i=2:m-1
                u(i,j)=1/4*(u(i+1,j)+u(i-1,j)+u(i,j+1)+u(i,j-1)-h^2*(i^2+j^2));
            end
        end
        u
    end
end
surf(u);
xlabel('x');
ylabel('t');
zlabel('u');
title('Laplace Equation');