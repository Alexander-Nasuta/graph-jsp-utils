import os
import pathlib as pl

from graph_jsp_utils.jsp_instance_downloader import download_instances

if __name__ == '__main__':

    target_path = pl.Path(os.path.abspath(__file__)).parent\
        .joinpath("resources")\
        .joinpath("jsp_instances")
    download_instances(
        target_directory=target_path,
        start_id=1,
        end_id=2
    )
