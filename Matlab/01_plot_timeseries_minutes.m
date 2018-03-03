numberOfXTicks = 20
data_length = length(newdata)
ticks = minutes(0:1:a-1);
handles = plot(ticks, newdata)
xticks(ticks)
xData = get(handles,'XData');
set(gca,'Xtick',linspace(xData(1),xData(end),numberOfXTicks))
