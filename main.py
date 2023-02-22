# This is a sample Python script.

# maybe I could use redis in this to store the last few run results, export them or something.


def get_intersect(surv_wage, real_wage, months_offset):
    # mx + b for now_line: now_linex
    # mx + b for offset_line: offset_linex - (offset_line * months_offset)
    # now_lineX - offset_lineX = - (offset_line * months_offset)
    # offset_lineX - now_lineX = offset_line * months_offset
    # X = (offset_line * months_offset) / (offset_line - now_line)
    # Y = now_line * X
    # print ('waiting one month to start working a real job, the two salaries would match after Y months.)
    x_intercept = (real_wage * months_offset) / (real_wage - surv_wage)
    y_intercept = surv_wage * x_intercept
    return [x_intercept, y_intercept]


def get_intersects(surv_wage, real_wage, months_offset):
    # for each month offset, calculate intersect of two lines
    # if surv is 11/hr, and the graph is dollars over months of time
    # convert 11 into monthly wage
    monthly_survival_pt = surv_wage * 8 * 11
    monthly_survival_ft = surv_wage * 8 * 22
    monthly_real_ft = real_wage * 8 * 22

    line_intersects = get_intersect(monthly_survival_ft, monthly_real_ft, months_offset)
    return line_intersects


def main():
    running = True

    # Use a breakpoint in the code line below to debug your script.
    while running:
        print('''Welcome to the survival job decision helper.
        I'll ask you for some salary inputs, and then tell you whether you should get a survival job.''')
        expected_survival_wage = int(input('For the "survival job," how much would you expect to be paid PER HOUR?\n'))
        expected_real_wage = int(
            input('Now, not counting benefits, how much would you expect to be paid for the "real" job?\n'))

        expected_time_to_find_real_job_while_working = int(
            input('How long do you think it will take you to find a real job?'))
        expected_time_to_find_real_job_unemployed = int(
            input('Now, how long do you expect it would take to you find a real job if you weren\'t working?'))

        intersects = get_intersects(expected_survival_wage, expected_real_wage,
                                    expected_time_to_find_real_job_while_working)
        print('''If it takes you + {expected_time} to find a "real" job, 
        then your real job wages will pass the survival job wages {intersect_months_from_start} months after starting your real job, 
        or {intersect_months_from_now} months from now.'''
              .format(expected_time=expected_time_to_find_real_job_while_working,
                      intersect_months_from_start=intersects[0] - expected_time_to_find_real_job_while_working,
                      intersect_months_from_now=intersects[0]))
        print('Remember that this calculation does not count benefits! It assumes 40 hrs / week.')
        keep_going = input('Keep going? Type `y` to continue.')
        if not (keep_going == "y"):
            running = False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
