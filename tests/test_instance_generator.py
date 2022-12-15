from graph_jsp_utils.jsp_custom_instance_generator import generate_jsp_instances


def test_instance_generator(resources_path):
    target_path = resources_path.joinpath("custom")

    generate_jsp_instances(
        target_dir=target_path,
        n_instances=100,
        n_jobs=5,
        n_machines=5
    )

    assert target_path.joinpath("5x5").exists()
