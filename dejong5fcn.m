function scores = dejong5fcn(xin)
%DEJONG5FCN Compute DeJongs fifth function.

%   Copyright 2003-2007 The MathWorks, Inc.

a =[-32, -16,   0,  16,  32, -32, -16,   0,  16,  32, -32, -16,  0, 16, 32 -32, -16,  0, 16, 32, -32, -16, 0, 16, 32;
    -32, -32, -32, -32, -32, -16, -16, -16, -16, -16,   0,   0,  0,  0,  0, 16,  16, 16, 16, 16, 32,  32, 32, 32, 32  ];

if(nargin == 0)
    plotobjective(@dejong5fcn,65.536 * [-1 1; -1 1]);
    return
end

scores = zeros(size(xin,1),1);
for i = 1:size(xin,1)
    p = xin(i,:);
    p = max(-65.536,min(65.536,p));
    k = 0.002;
    for j = 1:25
        k = k + 1 /(j + (p(1) - a(1,j))^6 + (p(2) - a(2,j)) ^ 6);
    end
    scores(i) = 1/k;
end

