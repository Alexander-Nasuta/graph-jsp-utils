import os
import pytest
import pathlib as pl
from graph_jsp_utils.jsp_instance_downloader import download_instances


@pytest.fixture(autouse=True)
def with_clean_resources_folder():
    # clear the test_resources directory before tests
    resources_path = pl.Path(os.path.abspath(__file__)).parent.joinpath("test_resources")

    from graph_jsp_utils.disjunctive_graph_logger import log

    def rm_tree(pth):
        """
        deletes a folder and every subfolder and files inside that folder.

        :param pth: a path (to a folder)
        :return: None
        """
        pth = pl.Path(pth)
        if not pth.exists():
            return

        for child in pth.glob('*'):
            if child.is_file():
                child.unlink()
            else:
                rm_tree(child)

        if not pth.is_dir():
            pth.rmdir()

    for child in resources_path.glob('*'):
        log.info(f"deleting '{child}'")
        rm_tree(child)

    yield None
    # Code that will run after the tests

@pytest.fixture(scope="function")
def resources_path():
    resources_path = pl.Path(os.path.abspath(__file__)).parent.joinpath("test_resources")
    yield resources_path


@pytest.fixture(scope="function")
def download_ft06(resources_path):
    download_instances(target_directory=resources_path, start_id=6, end_id=6)
    yield None
