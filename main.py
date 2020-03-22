from Scripts.picture import wenzishengcheng
from Scripts.mc_to_hao import zhuanyigepu
import os, sys, shutil
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
    mc_list = [fn for fn in os.listdir(input_folder) if fn.endswith('mc')]
    if not mc_list:
        print('Plz put mc files into the input folder!')
        sys.exit()
    if len(mc_list) > 3:
        print('You put more than 3 difficulties in input.')
        sys.exit()
    for item in mc_list:
        try:
            difficulty = linecache.getline(item, 5).strip()
            if difficulty.find('ADVANCE') != -1:
                zhuanyigepu(item, output_folder + '/adv.eve')
                print('you put ADV file in folder. Transformed!')
            elif difficulty.find('BASIC') != -1:
                zhuanyigepu(item, output_folder + '/bsc.eve')
                print('you put BSC file in folder. Transformed!')
            else:
                zhuanyigepu(item, output_folder + '/ext.eve')
                print('you put EXT file in folder. Transformed!')
        except:
            print('illegal mc_file! Plz check out if mc file is empty.')
            sys.exit()
    if 'ext.eve' not in os.listdir(output_folder):
        print('Failed! There is no extreme chart in this music')
        sys.exit()
    if 'adv.eve' not in os.listdir(output_folder):
        shutil.copy(os.getcwd() + '/output/ext.eve', os.getcwd() + '/output/adv.eve')
        print('No advance chart found! Copy ext to adv...')
    if 'bsc.eve' not in os.listdir(output_folder):
        shutil.copy(os.getcwd() + '/output/ext.eve', os.getcwd() + '/output/bsc.eve')
        print('No basic chart found! Copy ext to bsc...')

    # mc file information
    mc_file = input_folder + '/' + mc_list[0]
    mc_info = json.load(open(mc_file, encoding='UTF-8-sig'))
    print(mc_info)
    title = mc_info['meta']['song']['title']
    artist = mc_info['meta']['song']['artist']

    # make chart title pictures
    wenzishengcheng(title, artist, '1')