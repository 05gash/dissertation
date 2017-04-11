function [newx, newy] = browns(x, y)
    newx = x/(1+0.3*sqrt(x^2+y^2));
    newy = y/(1+0.3*sqrt(x^2+y^2));
end

clear;

sets = {linspace(-1,1,1344), linspace(-1,1,1512)};
[x,y]= ndgrid(sets{:});
cartProd = [x(:), y(:)];

[u,v] = arrayfun(@browns, cartProd(:,1), cartProd(:,2)); 

ui = linspace(-1,1,480);
vi = linspace(-1,1,540);

ur = interp1(ui,1:numel(ui), u, 'nearest');
yr = interp1(vi,1:numel(vi), v, 'nearest');


z = accumarray([ur, yr], 0.25, [480, 540]);

figure(2);

surf(z, 'marker', 'none', 'linestyle', 'none');
view(2);
colorbar;