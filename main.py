# This is a sample Python script.

# maybe I could use redis in this to store the last few run results, export them or something.

def is_worth_it(surv_wage, real_wage, months_offset_with_surv, months_offset_without_working):
    is_full_time = input('Would you be working full-time? Type `y` if so.') == 'y'
    if is_full_time:
        monthly_surv_wage = surv_wage * 8 * 22
    else:
        monthly_surv_wage = surv_wage * 8 * 11

    monthly_real_wage = real_wage * 8 * 22

    total_wages_with_surv = monthly_surv_wage * months_offset_with_surv
    total_wages_without_surv = monthly_real_wage * (months_offset_with_surv - months_offset_without_working)
    result = total_wages_with_surv > total_wages_without_surv

    return [result, total_wages_with_surv, total_wages_without_surv]


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
            input('How long do you think it will take you to find a real job if you had a survival job?'))
        expected_time_to_find_real_job_unemployed = int(
            input('Now, how long do you expect it would take to you find a real job if you weren\'t working?'))

        res, wages_with, wages_without = is_worth_it(expected_survival_wage,
                                                     expected_real_wage,
                                                     expected_time_to_find_real_job_while_working,
                                                     expected_time_to_find_real_job_unemployed)
        if res:
            print('''it is worth it for you to get a survival job!''')
            comp = 'more'
        else:
            print('It is not worth it for you to get a survival job.')
            comp = 'less'

        print('''You would earn {res} money over {months_with} months with a survival job
        than you would by waiting and focusing on finding a real job.
        Over {months_with} months, the survival job would earn you ${wages_with}.
        Over {months_with} months, the real job would earn you ${wages_without},
        assuming it took you {months_without} to find a real job.
        '''.format(
            res=comp,
            months_with=expected_time_to_find_real_job_while_working,
            months_without=expected_time_to_find_real_job_unemployed,
            wages_with=wages_with,
            wages_without=wages_without
        ))
        print('Remember that this calculation does not count benefits!')
        keep_going = input('Keep going? Type `y` to continue.')
        if not (keep_going == "y"):
            running = False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
