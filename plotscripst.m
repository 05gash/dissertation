clear;

sets = {linspace(-1,1,960), linspace(-1,1,1080)};
[x,y]= ndgrid(sets{:});
cartProd = [x(:), y(:)];

[u,v] = arrayfun(@browns, cartProd(:,1), cartProd(:,2)); 

ui = linspace(-1,1,960);
vi = linspace(-1,1,1080);

ur = interp1(ui,1:numel(ui), u, 'nearest');
yr = interp1(vi,1:numel(vi), v, 'nearest');


z = accumarray([ur, yr], 1, [960, 1080]);

figure(2);

surf(z, 'marker', 'none', 'linestyle', 'none');
view(2);
colorbar;
