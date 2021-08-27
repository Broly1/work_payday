#!/usr/local/bin/python
miles_rate = 0.51
stors_rate = 10.00
deadstack_cases_rate = 00.10
casecount_carted_rate = 0.05
pre_postrip_rate = 6.00
intertripe_inspection_rate = 4.50
repositions_drop_hooks_rate = 4.50
hourlly_delay_rate = 13.15
meeting_dalay_rate = 21.00

def stors():
    pre_postrip = input("pre/postrip inpections? ")
    miles = input("Miles driven? ")
    stors = input("How many stors? ")
    casecount_carted = input("How many carted cases? ")
    intertripe_inspection = input("Intertrip inpections? ")
    repositions_drop_hooks = input("Drop and hook or trailer repositions? ")
    hourlly_delay = input("Hours of delay? ")
    meeting_delay = input("Meeting delay? ")
    pay = \
        float(pre_postrip)*float(pre_postrip_rate)+float(miles)*float(miles_rate) + \
        float(intertripe_inspection)*float(intertripe_inspection_rate) + \
        float(casecount_carted)*float(casecount_carted_rate) + \
        float(hourlly_delay)*float(hourlly_delay_rate) + \
        float(meeting_delay)*float(meeting_dalay_rate) + \
        float(repositions_drop_hooks)*float(repositions_drop_hooks_rate) + \
        float(stors)*float(stors_rate)
    print("Pay:", pay)
    return

def pec():
    miles = input("Miles driven? ")
    deadstack_cases = input("Deadstack cases? ")
    intertripe_inspection = input("Intertrip inpections? ")
    pre_postrip = input("Prepostrip inpections? ")
    hourlly_delay = input("Delay time? ")
    repositions_drop_hooks = input("Drop or trailer repositions? ")
    meeting_delay = input("Meeting delay? ")
    pay = \
        float(miles)*float(miles_rate) + \
        float(deadstack_cases)*float(deadstack_cases_rate) + \
        float(pre_postrip)*float(pre_postrip_rate) + \
        float(intertripe_inspection)*float(intertripe_inspection_rate) + \
        float(repositions_drop_hooks)*float(repositions_drop_hooks_rate) + \
        float(hourlly_delay)*float(hourlly_delay_rate) + \
        float(meeting_delay)*float(meeting_dalay_rate)
    print("Pay:", pay)
    return

def show_menu():
    print("-----------------")
    print("1) pec")
    print("2) stors")
    print("Q) Exit\n")
def menu():
    while True:
        show_menu()
        choice = input('What type of run did you do?: ').lower()
        if choice == '1':
            pec()
            break
        elif choice == '2':
            stors()
            break
        elif choice == 'q':
            return
        else:
            print(f'Not a correct choice: <{choice}>,try again')

if __name__ == '__main__':
    menu()
