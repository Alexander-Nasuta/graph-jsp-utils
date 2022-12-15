from graph_jsp_utils.jsp_instance_details import download_benchmark_instances_details, get_jps_instance_details


def test_instance_details_ft06(resources_path):
    download_benchmark_instances_details(
        target_dir=resources_path
    )

    ft06_details_vals = {
        'lower_bound': 55,
        'upper_bound': 55,
        'jobs': 6,
        'machines': 6,
        'n_solutions': 53,
        'lb_optimal': True
    }

    benchmark_details_file_path = resources_path.joinpath("jps_instance_details").joinpath("benchmark_details.json")
    details_ft06 = get_jps_instance_details(
        instance_details_file_path=benchmark_details_file_path,
        instance="ft06"
    )
    assert details_ft06 == ft06_details_vals

