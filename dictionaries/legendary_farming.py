def legendary_farming():
    dict_materials = {}
    legendary_item = ''
    legendary_item_obtained = False
    key_materials = ['shards', 'fragments', 'motes']
    is_break = False

    while True:
        if is_break:
            break

        initial_list = input().split()

        for i in range(0, len(initial_list), 2):
            quantity = int(initial_list[i])
            material = initial_list[i + 1].lower()

            if material not in dict_materials.keys():
                dict_materials[material] = 0

            dict_materials[material] += quantity

            if material in key_materials and legendary_item_obtained is False and dict_materials[material] >= 250:
                if material == 'shards':
                    legendary_item = 'Shadowmourne'
                elif material == 'fragments':
                    legendary_item = 'Valanyr'
                elif material == 'motes':
                    legendary_item = 'Dragonwrath'

                legendary_item_obtained = True
                dict_materials[material] -= 250
                is_break = True
                break

    print(f'{legendary_item} obtained!')
    if 'shards' in dict_materials.keys():
        print(f"shards: {dict_materials['shards']}")
    else:
        print(f"shards: 0")
    if 'fragments' in dict_materials.keys():
        print(f"fragments: {dict_materials['fragments']}")
    else:
        print(f"fragments: 0")
    if 'motes' in dict_materials.keys():
        print(f"motes: {dict_materials['motes']}")
    else:
        print(f"motes: 0")

    for material, quantity in dict_materials.items():
        if material not in key_materials:
            print(f'{material}: {quantity}')


legendary_farming()




