import datetime
import pyautogui
import time


def main():
    # Example code
    print("Sleeping for 5s")
    time.sleep(5)

    clicks = 50
    seconds = 15

    auto_click_num(clicks)
    print()
    auto_click_time(seconds)


def chop_microseconds(delta):
    return delta - datetime.timedelta(microseconds=delta.microseconds)


def auto_click_time(number_of_seconds: int):
    print("Clicking for " + str(chop_microseconds(datetime.timedelta(seconds=number_of_seconds))) + ".")
    start_time = time.time()
    clicks = 0
    last_print_time = start_time
    if number_of_seconds < 120:
        time_for_print_statement = number_of_seconds / 10
    else:
        time_for_print_statement = 10
    while time.time() - start_time < number_of_seconds:
        pyautogui.click()
        clicks = clicks + 1
        # if round(time.time() - start_time, 0) % 10 == 0:
        if round(time.time() - last_print_time, 1) >= time_for_print_statement:
            last_print_time = time.time()
            print(str(chop_microseconds(datetime.timedelta(seconds=time.time() - start_time))) + "s completed. " +
                  str(chop_microseconds(datetime.timedelta(seconds=number_of_seconds - (time.time() - start_time)))) +
                  " remaining. CPS: " + str(round(clicks / (time.time() - start_time), 2)) +
                  " Estimated number of clicks remaining: " +
                  str(round((clicks / (time.time() - start_time)) * (number_of_seconds -
                                                                     (time.time() - start_time)), 0)))

    print("Process Completed. " + str(clicks) + " clicks completed in " +
          str(chop_microseconds(datetime.timedelta(seconds=number_of_seconds))) + ".")


def auto_click_num(number_of_clicks: int):
    print("Clicking " + str(number_of_clicks) + " times.")
    start_time = time.time()
    for i in range(1, number_of_clicks):
        pyautogui.click()
        if i % 25 == 0:
            clicks_per_sec = i / (time.time() - start_time)
            remaining_clicks = number_of_clicks - i
            est_time = remaining_clicks / clicks_per_sec
            print("Completed " + str(i) + "th click out of " + str(number_of_clicks) + ". CPS: " +
                  str(round(clicks_per_sec, 2)) + " Estimated remaining time: " +
                  str(chop_microseconds(datetime.timedelta(seconds=est_time))))

    print("Process took " + str(chop_microseconds(datetime.timedelta(seconds=time.time() - start_time))))


if __name__ == '__main__':
    main()
