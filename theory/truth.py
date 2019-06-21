for A in [True, False]:
    for B in [True, False]:
        for C in [True, False]:
                print(f'{int(A)} -- {int(B)} -- {int(C)} == {int(not(A or B) or ((A or C) and not(B or not C)))}')