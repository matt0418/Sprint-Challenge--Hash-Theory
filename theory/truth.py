for A in [True, False]:
    for B in [True, False]:
        print(f'{int(A)} -- {int(B)} -- {int(A or not B)}')