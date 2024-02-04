def loading_bar(num):
    loading_scale = '.' * 10
    number_change = int(num / 10)
    replaced_load_scale = loading_scale.replace('.', '%', number_change)
    return replaced_load_scale


def print_result(scale, num):
    if num < 100:
        print(f'{num}% [{scale}]')
        print(f'Still loading...')
    else:
        print('100% Complete!')
        print(f'[{scale}]')


number = int(input())
print_result(loading_bar(number), number)


