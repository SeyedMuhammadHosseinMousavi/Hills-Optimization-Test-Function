function scores = ackleyfcn(pop)
%ACKLEYFCN Compute the Ackley function.

%   Copyright 2003-2007 The MathWorks, Inc.

scores = zeros(size(pop,1),1);
for i = 1:size(pop,1)
    p = pop(i,:);
    % on the interval [-32.768 32.768]
    p = max(-32.768,min(32.768,p));
    
    scores(i) = 20 + exp(1) - 20 * exp( -0.2 * exp ( sqrt( (1/length(p)) * sum(p .^ 2)) - exp((1/length(p)) * sum(cos(2*pi .* p)))));
end