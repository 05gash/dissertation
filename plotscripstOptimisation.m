clear;

sets = {linspace(-1,1,672), linspace(-1,1,756)};
innersets = {linspac(-0.5, 0.5, 672), linspace(-0.5, 0.5, 756)};

[xi, yi] = ndgrid(innersets{:});
[x,y]= ndgrid(sets{:});
cartProd = [x(:), y(:)];
cartProdi = [xi(:), yi(:)];

[u,v] = arrayfun(@browns, cartProd(:,1), cartProd(:,2)); 
[uin, vin] = arrayfun(@browns, cartProdi(:,1), cartProdi(:,2));

ui = linspace(-1,1,960);
vi = linspace(-1,1,1080);

ur = interp1(ui,1:numel(ui), u, 'nearest');
yr = interp1(vi,1:numel(vi), v, 'nearest');

uri = interp1(ui,1:numel(ui), uin, 'nearest');
yri = interp1(vi,1:numel(vi), vin, 'nearest');


z = accumarray([vertcat(ur, uri), vertcat(yr,  yri)], 1, [960, 1080]);

figure(2);

surf(z, 'marker', 'none', 'linestyle', 'none');
view(2);
colorbar;