 select count(*) from bmp_data;
 select max(temp), min(temp), avg(temp), max(pressure), min(pressure), avg(pressure) from bmp_data where date_time between '2015-02-11 09:15:00' and '2015-02-11 13:45:00';
 select temp, pressure from bmp_data where date_time = '2015-02-11 13:30:00';
 select date_time, temp, pressure from bmp_data where date_time between '2015-02-11 13:12:00' and '2015-02-11 13:24:59';
.exit
