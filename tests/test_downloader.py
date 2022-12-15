from graph_jsp_utils.jsp_instance_downloader import download_instances


def test_benchmark_instance_downloader_single(resources_path):
    # abz5
    download_instances(target_directory=resources_path, start_id=1, end_id=1, format="standard")
    assert resources_path.joinpath("standard").joinpath("abz5.txt").exists()
    download_instances(target_directory=resources_path, start_id=1, end_id=1, format="taillard")
    assert resources_path.joinpath("taillard").joinpath("abz5.txt").exists()
    # check if running the code twice causes errors
    download_instances(target_directory=resources_path, start_id=1, end_id=1)
