from pink_morsel_visualizer import dash_app


def test_header(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#header", timeout=10)


def test_visualization(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#visualization", timeout=10)


def test_region_picker(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#region_picker", timeout=10)