%for running this you have to be in globaloptimtooldemos folder
clc;clear;
% FitnessFunction = @ackleyfcn;
% FitnessFunction = @Hills;
% FitnessFunction = @rastriginsfcn;
%  FitnessFunction = @dejong2fcn; %it will called rosenbrock or dejong
 FitnessFunction = @eggholder;
% FitnessFunction = @multirosenbrock;
% FitnessFunction = @dejong5fcn;

numberOfVariables =4;% A 4-D problem
lb =-10*ones(numberOfVariables,1);
ub =-lb;
%options = optimoptions('particleswarm','SwarmSize',50);
options = optimoptions(@particleswarm,'SwarmSize',20,'OutputFcn',@pswplotranges);
[x,Fval,exitFlag,Output] = particleswarm(FitnessFunction,numberOfVariables,lb,ub,options)
fprintf('The number of iterations was : %d\n', Output.iterations);
fprintf('The number of function evaluations was : %d\n', Output.funccount);
fprintf('The best function value found was : %g\n', Fval);