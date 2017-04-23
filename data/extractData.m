fsMSAA = csvread('fullscreenMSAA.csv', 1, 1);
fsSSAA = csvread('fullscreenSSAA.csv', 1, 1);
noantialiasing = csvread('noantialiasing.csv', 1, 1);
ssMSAA = csvread('subscreenMSAAProfile.csv', 1, 1);
ssSSAA = csvread('subscreenSSAA.csv', 1, 1);

data = vertcat(noantialiasing, fsMSAA, ssMSAA, fsSSAA, ssSSAA);

drawCalls = data(:,1);
frameTime = data(:,2);
vsTime = data(:,6);
gsTime = data(:,12);
psTime = data(:,14);
gsVerticesOut = data(:,31);
psPixelsOut = data(:,36);

csvwrite('drawCalls.csv', drawCalls);
csvwrite('frameTime.csv', frameTime);
csvwrite('vsTime.csv', vsTime);
csvwrite('gsTime.csv', gsTime);
csvwrite('psTime.csv', psTime);
csvwrite('gsVertsOut.csv', gsVerticesOut);
csvwrite('psPixelsOut.csv', psPixelsOut);