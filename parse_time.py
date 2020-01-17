import datetime

# date_time_str = '2018-06-29 08:15:27.243860'
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
#
# print('Date:', date_time_obj.date())
# print('Time:', date_time_obj.time())
# print('Date-time:', date_time_obj)


# date_time_str = 'Jun 28 2018  7:40AM'
# date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')
#
# print('Date:', date_time_obj.date())
# print('Time:', date_time_obj.time())
# print('Date-time:', date_time_obj)

# "Jun 28 2018 at 7:40AM" -> "%b %d %Y at %I:%M%p"
# "September 18, 2017, 22:19:55" -> "%B %d, %Y, %H:%M:%S"
# "Sun,05/12/99,12:30PM" -> "%a,%d/%m/%y,%I:%M%p"
# "Mon, 21 March, 2015" -> "%a, %d %B, %Y"
# "2018-03-12T10:12:45Z" -> "%Y-%m-%dT%H:%M:%SZ"

date_time_str = 'Nov 2019 04:02:31,437'
date_time_obj = datetime.datetime.strptime(date_time_str, '%b %Y %H:%M:%S,%f')
print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)