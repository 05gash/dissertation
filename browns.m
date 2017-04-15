function [newx, newy] = browns(x, y)
    newx = x/(1+0.25*sqrt(x^2+y^2));
    newy = y/(1+0.25*sqrt(x^2+y^2));
end