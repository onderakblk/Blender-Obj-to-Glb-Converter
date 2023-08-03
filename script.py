import os
import bpy

# İşlem yapılacak klasörü belirle
folder_path = "C:/Users/PC/Desktop/denemeblender"
glbl_path = "C:/Users/PC/Desktop/glb"

# Klasördeki her bir dosya için işlem yap
for filename in os.listdir(folder_path):
    if filename.endswith(".obj"):
        # OBJ dosyasını içe aktar
        obj_path = os.path.join(folder_path, filename)
        bpy.ops.import_scene.obj(filepath=obj_path)

        # OBJ dosyasından elde edilen nesneyi bul ve ismini sakla
        obj = bpy.context.selected_objects[0]
        obj_name = obj.name

        # Yönleri düzelt
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        # Nesnenin dönüşünü ayarla
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

        # Nesneyi +90 derece döndür
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.transform.rotate(value=1.5708, orient_axis='Y')

        # Koordinat sistemini değiştir
        bpy.context.scene.transform_orientation_slots[0].type = 'GLOBAL'

        # Nesneyi global olarak kaydet
        glb_path = os.path.join(glbl_path, filename[:-4] + ".glb")
        bpy.ops.export_scene.gltf(filepath=glb_path, export_format='GLB', export_draco_mesh_compression_enable=True)

        # Sahnedeki nesneyi sil
        bpy.data.objects[obj_name].select_set(True)
        bpy.ops.object.delete(use_global=False)