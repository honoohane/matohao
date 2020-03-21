from Scripts.picture import wenzishengcheng
from Scripts.mc_to_hao import zhuanyigepu
import os
import linecache
import json

if __name__ == '__main__':

    # make an input/output folder
    input_folder = os.getcwd() + '/input'
    output_folder = os.getcwd() + '/output'
    is_path_exists_i = os.path.exists(input_folder)
    if not is_path_exists_i:
        os.makedirs(input_folder)
    is_path_exists_o = os.path.exists(output_folder)
    if not is_path_exists_o:
        os.makedirs(output_folder)

    # transform mc files to hdd files
    mc_list = [fn for fn in os.listdir(input_folder)
               if fn.endswith('mc')]
    if not mc_list:
        print('Plz put mc files into the input folder!')
    else:
        for item in mc_list:
            if len(mc_list) == 1:
                mc_file = input_folder + '/' + mc_list[0]
                zhuanyigepu(mc_file, output_folder + '/ext.eve')
                zhuanyigepu(mc_file, output_folder + '/adv.eve')
                zhuanyigepu(mc_file, output_folder + '/bsc.eve')
                print('you put 1 mc file in folder. Transformed!')
            else:
                for item in mc_list:
                    mc_file = input_folder + '/' + item
                    try:
                        difficulty = linecache.getline(mc_file, 5).strip()
                        if difficulty.find('EXTREME') != -1:
                            zhuanyigepu(mc_file, output_folder + '/ext.eve')
                            print('you put EXT file in folder. Transformed!')
                        elif difficulty.find('ADVANCE'):
                            zhuanyigepu(mc_file, output_folder + '/adv.eve')
                            print('you put ADV file in folder. Transformed!')
                        elif difficulty.find('BASIC'):
                            zhuanyigepu(mc_file, output_folder + '/bsc.eve')
                            print('you put BSC file in folder. Transformed!')
                        else:
                            print('illegal mc_file! Plz check out if "version" is basic, advance or extreme.')
                    except:
                        print('illegal mc_file! Plz check out if mc file is empty.')

    # mc file information
    mc_file = input_folder + '/' + mc_list[0]
    mc_info = json.load(open(mc_file, encoding='UTF-8-sig'))
    print(mc_info)
    title = mc_info['meta']['song']['title']
    artist = mc_info['meta']['song']['artist']

    # make chart title pictures
    wenzishengcheng(title, artist, '1')