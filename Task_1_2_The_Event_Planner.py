
venue = 'large hall'
attendees = 40

if venue == 'large hall':
    if attendees <= 20:
        print('not enough people for large hall :c')
    elif attendees == 40:
        print('we get the large hall!')
    else:
        print('no party today :c')

venue = 'large hall'
attendees = 11

if venue == 'large hall':
    if attendees <= 20:
        print('not enough people for large hall :c')
    elif attendees == 40:
        print('we get the large hall!')
    else:
        print('no party today :c')

venue = 'large hall'
attendees = 55

if venue == 'large hall':
    if attendees <= 20:
        print('not enough people for large hall :c')
    elif attendees == 40:
        print('we get the large hall!')
    else:
        print('no party today :c')


vegetarian = 'yes'
recommend = 'veggie delight caterers'
print('bring me the veggies!' if vegetarian == 'yes' and recommend else 'gourmet meal caterers')
