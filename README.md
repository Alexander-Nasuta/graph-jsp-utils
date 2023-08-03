![Tests](https://github.com/mCodingLLC/SlapThatLikeButton-TestingStarterProject/actions/workflows/tests.yml/badge.svg)

<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://cybernetics-lab.de/">
    <img src="https://github.com/Alexander-Nasuta/graph-jsp-env/raw/master/resources/readme_images/logo.png" alt="Logo" height="80">
  </a>

  <h1 align="center">
     Graph Job Shop Problem Gym Environment Utils
  </h1>

   <a>
    <img src="https://github.com/Alexander-Nasuta/graph-jsp-env/raw/master/resources/readme_images/graph_jsp_tikz.png" alt="Logo" height="180">
  </a>

</div>




# About The Project
This project contains various utilities for the [Graph Job Shop Environment](https://github.com/Alexander-Nasuta/graph-jsp-env)
This includes:
- `graph_jsp_utils.jsp_instance_downloader.download_instances`: a function for downloading JSP instances different [formats](http://jobshop.jjvh.nl/explanation.php) form http://jobshop.jjvh.nl/
- `graph_jsp_utils.jsp_instance_parser`: a file that contains functions for parsing JSP instances from different formats into the format used by the Graph Job Shop Environment.
- `graph_jsp_utils.jsp_instance_details`: a file that contains functions for scraping additional information about JSP instances form http://jobshop.jjvh.nl/. It's essentially saving all the data given in the [table](http://jobshop.jjvh.nl/index.php) to a json-file.
- `graph_jsp_utils.jsp_custom_instance_details`: generates similar information like `graph_jsp_utils.jsp_instance_details` but for custom instances using [Google OR-Tools](https://developers.google.com/optimization). This is only feasible for instances with a small number of jobs and machines. The results are also saved to a json-file.
- `graph_jsp_utils.jsp_custom_instance_generator`: a file that contains functions for generating JSP instances.
- `graph_jsp_utils.jsp_or_tools_solver`: a file that contains functions for solving JSP instances using the [Google OR-Tools](https://developers.google.com/optimization) library.

Github: https://github.com/Alexander-Nasuta/graph-jsp-utils

PyPi: https://pypi.org/project/graph-jsp-utils/



### Install the Package 
Install the package with pip:
```
   pip install graph-jsp-utils
```

# Project Structure
This project ist structured according to [James Murphy's testing guide](https://www.youtube.com/watch?v=DhUpxWjOhME) and 
this [PyPi-publishing-guide](https://realpython.com/pypi-publish-python-package/).

## Usage and Examples

Ever script/file has a `__main__` function, which demonstrates demonstrates it's functionality.
Additional examples can be found in the [graph-jsp-examples](https://github.com/Alexander-Nasuta/graph-jsp-examples) repo.

# License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- MARKDOWN LINKS & IMAGES todo: add Github, Linked in etc.-->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[screenshot]: resources/readme_images/screenshot.png


