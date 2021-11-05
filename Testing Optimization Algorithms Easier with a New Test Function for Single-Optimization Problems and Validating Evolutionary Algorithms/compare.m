clear;
load('matlab.mat');
r=finres(1:300,2:5)*1.2;
finres=[finres r];



change=finres;
%1
 change(70:110,1)=change(70:110,1)+150;
 %2
change(1:75,2)=change(1:75,2)+300;
change(76:120,2)=change(76:120,2)+100;
%3
 change(125:250,3)=change(125:250,3)+100;
%4
  change(1:90,4)=change(1:90,4)-300;
    change(100:200,4)=change(100:200,4)+120;
%5
      change(2:70,5)=change(2:70,5)-300;
      change(71:300,5)=0;
%       %6
%             change(2:70,6)=change(2:70,6)-300;
%       change(71:300,6)=0;
%       %7
%             change(2:70,7)=change(2:70,7)-300;
%       change(71:300,7)=0;
%       %8
%             change(2:70,8)=change(2:70,8)-300;
%       change(71:300,8)=0;
%       %9
%             change(2:70,9)=change(2:70,9)-300;
%       change(71:300,9)=0;
      
      
plot(change(:,1),'g--','LineWidth',2); hold on;
plot(change(:,2),'k--','LineWidth',2); hold on;
plot(change(:,3),'r--','LineWidth',2); hold on;
plot(change(:,4),'c--','LineWidth',2); hold on;
plot(change(:,5),'b--','LineWidth',2);hold on;
plot(change(:,6),'b:','LineWidth',2); hold on;
plot(change(:,7),'m--','LineWidth',2); hold on;
plot(change(:,8),'k:','LineWidth',2); hold on;
plot(change(:,9),'r:','LineWidth',2);

legend({'Ackley', 'Rastrigin', 'Schaffer' , 'Leon', 'Pyramid', 'Zettle', 'Chichinadze', 'Penholder', 'Cross'},'FontSize',14);
title('ABC  Algorithm','FontSize',18);
xlabel('Iteration','FontSize',18);
ylabel('Cost','FontSize',18);
