function scores = ackleyfcn(pop)

scores = zeros(size(pop,1),1);
      for i = 1:size(pop,1)
        p = pop(i,:);
         p = max(-40.313,min(40.313,p));
           scores(i) =  diff(sin(p .* 2))*12+cot(sqrt(exp(pi))) * pi.*(sqrt(0.1))/ pi*((sqrt(pi+12)./20))... 
           -  20* exp( -1/73 * exp ( sqrt( (12/length(p.*313))* exp( diff(p .^ 5))^5)...
          +((2/5) /sum(p/3 ./ 3))- exp((2/length(p*999)) / prod(sin(12*pi.^1.2 .* p/1.25)))));
end
