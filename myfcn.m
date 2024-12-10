clc;clear;
% ss=@ackleyfcn;
% plotobjective(ss,[-5 5; -5 5]);


% plotobjective(@rastriginsfcn,[-3 3; -3 3]);
% plotobjective(@dejong2fcn,[-5 5; -5 5]);
% plotobjective(@dejong5fcn,[-5 5; -5 5]);
% plotobjective(@eggholder,[-5 5; -5 5]);
% plotobjective(@multirosenbrock,[-5 5; -5 5]);
% plotobjective(@Hills,[-15 15; -15 15]);
%  FitnessFunction = @Hills;
 FitnessFunction = @ackleyfcn;
% FitnessFunction = @rastriginsfcn;
%  FitnessFunction = @dejong2fcn;
%  FitnessFunction = @eggholder;

% FitnessFunction = @rastriginsfcn;
% FitnessFunction = @dejong2fcn; %it will called rosenbrock or dejong
% FitnessFunction = @eggholder;
% FitnessFunction = @multirosenbrock;
% FitnessFunction = @dejong5fcn;
% FitnessFunction = @simple_fitness;%%its beale
% FitnessFunction = @(x1)x1(2)*exp(-norm(x1)^2);

numberOfVariables = 6;
[x,Fval,exitFlag,Output] = ga(FitnessFunction,numberOfVariables);
fprintf('The number of generations was : %d\n', Output.generations);
fprintf('The number of function evaluations was : %d\n', Output.funccount);
fprintf('The best function value found was : %g\n', Fval);

opts.PopulationSize = 50;
opts.InitialPopulationRange = [20 0; 20 0];
opts = optimoptions(@ga,'PlotFcn',{@gaplotbestf,@gaplotstopping,@gaplotbestindiv},'MaxGenerations',50,'MaxStallGenerations', 50);
[x,Fval,exitFlag,Output] = ga(FitnessFunction,numberOfVariables,[],[],[],[],[],[],[],opts);
