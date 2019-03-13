from unittest import TestCase

from browser.Browser_Lamdba_Helper import Browser_Lamdba_Helper
from utils.Dev import Dev
from utils.aws.Lambdas import Lambdas
from view_helpers.VivaGraph_Js_Views import VivaGraph_Js_Views


class Test_VivaGraph_Js_Views(TestCase):

    def setUp(self):
        self.graph_name = 'graph_XKW'
        self.png_data   = None

    def tearDown(self):
        if self.png_data:
            Browser_Lamdba_Helper(headless=False).save_png_data(self.png_data)

    def test_default(self):
        graph_name = 'graph_XKW'    # (7 nodes)
        #graph_name = 'graph_MKF'    # ( 20 nodes,  27 edges)
        #graph_name = 'graph_YT4'   # (199 nodes, 236 edges)
        #graph_name = 'graph_VZ5'   # (367 nodes, 653 edges)
        #graph_name = 'graph_EE3'    # fails in lamnda
        self.png_data = VivaGraph_Js_Views.default(params=[graph_name])

        browser_helper = Browser_Lamdba_Helper(headless=False).setup()
        pngData = browser_helper.get_screenshot_png(close_browser=False)
        browser_helper.save_png_data(pngData)

        #return







    def test_update_lambda(self):
        Lambdas('browser.lambda_browser').update_with_src()


