import pandas as pd
data= pd.read_csv("WeatherData.csv")
print (data);
print(data.head());
print(data.shape);
print(data.index);
print(data.columns);
print(data.dtypes);
print(data['Rel Hum_%'].unique());
print(data.nunique());
print(data.count());
print(data['Rel Hum_%'].value_counts());
print(data.info());

##TO FIND ALL THE WIND SPEED VALUES FROM THE DATA
print(data['Wind Speed_km/h'].unique());

## number of times weather is excatly clear
#1.value counts
print(data.head());
print(data.Weather.value_counts());
#2.filtring
print(data[data.Weather == 'Clear']);
#3.group by
print(data.groupby('Weather').get_group('Clear'));

##find the data with wind speed = 4
print(data[data['Wind Speed_km/h'] == 4]);

##find out all the null values in data
print(data.isnull().sum())
print(data.notnull().sum())

## rename a column
data.rename(columns = {'Weather' :'weather condition'}, inplace= True);

##mean value of visibility column
print(data.Visibility_km.mean());

##standard deviation of pressuse in the area
print(data.Press_kPa.std());

##  variance of relative humidity
print(data['Rel Hum_%'].var());

## all instances when snow is recorded
#value count
print(data['weather condition'].value_counts());
#filtring
print(data[data['weather condition']  == 'Snow']);
#str.containd
print(data[data['weather condition'].str.contains('Snow')].tail(5));

## all instances when wind speen is 24 and visibility is 25
print(data[(data['Wind Speed_km/h']==24) & (data['Visibility_km']==25)]);

## mean value of each column against each weather condition
print(data.groupby['weather condition'].mean());

## min and max condition of each column against weathe condition

print(data.groupby['Rel Hum_%'].min());

## show all the records where weather condition is  fog
print(data[data['Weather'] == 'Fog']);

##find all the instance when weather is clear and visibility is above 40
print(data[(data['Weather']=='Clear') & (data['Visibility_km']>40)]);

## find the instances where weather is clear , relative humidity is greater than 40 or visibility is above 40
print(data[((data['Weather']=='clear') & (data['Rel Hum_%'] >50)) | (data['Visibility_km']>40)])


