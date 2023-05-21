# import h5py

# with h5py.File("D:\Project-project\Pemilah Sampah\Datasheet created\datasheet1405_next.h5", 'r') as f:
#     for key in f.keys():
#         print(key)

import h5py

# membuka file h5
f = h5py.File('D:/Project-project/Pemilah Sampah/Datasheet created/datasheet1405_next.h5', 'r')

# membaca bobot model
model_weights = f['model_weights']
# print model_weights.keys() untuk melihat daftar layer dalam model

# membaca bobot pengoptimal
optimizer_weights = f['optimizer_weights']
# print optimizer_weights.keys() untuk melihat daftar optimizers

# menutup file h5
# f.close()