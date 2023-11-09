x = [31,
     
     3, 5,6, 8,9, 11,12, 14,
     
     16,
     
     18, 20,21, 23,24, 26,27, 29]

print(x)

x = [(x_-1)*2 for x_ in x]

print(x)

print()
for i in range(1,19):
    print('images/{:02d}.png'.format(i))

# # now given a image path dir with 01 - 60.png files need to copy to a above index image to a new dir
# # Path: h2.py
# import os
# import shutil

# src_dir_old = '.\\new_exp_normal\images\\old'
# src_dir_new = '.\\new_exp_normal\images\\new'

# # now copy to new dir
# dst_dir = '.\\new_exp_normal\images\\new2'

# for i in range(1, 61):
#     if i in x:
#         src_file = os.path.join(src_dir_old, '{:02d}.png'.format(i))
#         dst_file = os.path.join(dst_dir, '{:02d}.png'.format(i))
#         shutil.copyfile(src_file, dst_file)
        
# # 

# count = 1
# for i in x:
#     src_file = os.path.join(src_dir_new, '{:02d}.png'.format(i))
#     dst_file = os.path.join(dst_dir, '{:02d}.png'.format(count))
    
#     shutil.copyfile(src_file, dst_file)
    
#     count += 1
        
# print('done')
    