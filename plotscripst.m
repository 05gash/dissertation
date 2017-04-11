[X,Y] = meshgrid(linspace(-1,1,20), linspace(-1,1, 20));
u = [X(:)];
v = [Y(:)];

[newu, newv] = arrayfun(browns, u, v);

plotmatrix(newu, newv);