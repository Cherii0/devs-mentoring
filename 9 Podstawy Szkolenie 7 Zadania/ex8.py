def func(**kwargs):

    hour_angle = 30
    hour_minute_angle = 0.5
    minute_angle = 6

    hour_final_angle = (kwargs["hour"] * hour_angle )+ (kwargs["minute"] * hour_minute_angle)
    minute_final_angle = (kwargs["minute"] * minute_angle)

    print(hour_final_angle - minute_final_angle)





func(hour = 10, minute = 30)
