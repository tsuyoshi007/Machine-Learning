function J = computeCost(X, y, theta)
  
clc;

data = load('C:/Users/Tsuyoshi/Desktop/machine-learning-ex1/ex1/ex1data1.txt');
x = data(:,1);
y = data(:,2);


m = length(y);

x = [ones(m,1),data(:,1)];

theta = zeros(2,1);

hynosis = theta' .* x;  

error=hynosis-y;

J=1/(2*m)*sum(pow2(error));

end