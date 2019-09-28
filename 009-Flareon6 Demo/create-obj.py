import struct

# out_file_name = "mesh1.obj"
# vertices_file_name = "vertices1.bin"
# faces_file_name = "faces1.bin"
# num_vertices = 0x1e
# num_faces = 0x38

out_file_name = "mesh2.obj"
vertices_file_name = "vertices2.bin"
faces_file_name = "faces2.bin"
num_vertices = 0x128
num_faces = 0x10a

with open(out_file_name, "w") as mesh:
    print("mtllib Cube.mtl", file=mesh)
    print("o Cube", file=mesh)

    with open(vertices_file_name, "rb") as vertices:
        vertex_data = vertices.read()

        for vertex_index in range(num_vertices):

            x = struct.unpack_from("f", vertex_data, vertex_index * 0x18)[0]
            y = struct.unpack_from("f", vertex_data, vertex_index * 0x18 + 4)[0]
            z = struct.unpack_from("f", vertex_data, vertex_index * 0x18 + 8)[0]

            print("v {:.6f} {:.6f} {:.6f}".format(x, y, z), file=mesh)

        print("g Cube_Cube_Material", file=mesh)
        print("usemtl Material", file=mesh)
        print("s off", file=mesh)

    with open(faces_file_name, "rb") as faces:
        faces_data = faces.read()
        faces_data_index = 0

        for face_index in range(num_faces):

            face_item1 = struct.unpack_from(
                "i", faces_data, face_index * 4 * 3)[0] + 1
            face_item2 = struct.unpack_from(
                "i", faces_data, face_index * 4 * 3 + 4)[0] + 1
            face_item3 = struct.unpack_from(
                "i", faces_data, face_index * 4 * 3 + 8)[0] + 1

            print("f {0} {1} {2}".format(
                face_item1, face_item2, face_item3), file=mesh)
