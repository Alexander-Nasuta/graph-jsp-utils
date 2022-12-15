from graph_jsp_utils.jsp_or_tools_solver import solve_jsp


def test_or_tools_solver_on_ft06(ft06_jsp_instance):
    makespan, status, df, info = solve_jsp(jsp_instance=ft06_jsp_instance, plot_results=False)
    assert makespan == 55
