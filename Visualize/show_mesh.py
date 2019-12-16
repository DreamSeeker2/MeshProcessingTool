import trimesh

def show_mesh(mesh_path):
    mesh = trimesh.load_mesh(mesh_path, process=False)
    mesh.visual.vertex_colors = [204, 224, 255, 255]
    mesh.show()

if __name__ == '__main__':
    show_mesh('example.obj')
