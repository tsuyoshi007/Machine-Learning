function plotData(x,y)


figure;
data = load('C:/Users/Tsuyoshi/Desktop/machine-learning-ex1/ex1/ex1data1.txt');
x = data(:,1);
y = data(:,2);
plot(x,y,'rx','MarkerSize',4)


end
