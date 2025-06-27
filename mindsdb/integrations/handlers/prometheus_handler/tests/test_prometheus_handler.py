import unittest
from mindsdb.integrations.handlers.prometheus_handler.prometheus_handler import PrometheusHandler
from mindsdb.api.executor.data_types.response_type import RESPONSE_TYPE


class PrometheusHandlerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kwargs = {
            "host": "http://4.240.90.150/prometheus",
        }
        cls.handler = PrometheusHandler('test_prometheus_handler', cls.kwargs)

    def test_0_check_connection(self):
        result = self.handler.check_connection()
        print("\n\n--- DEBUG (check_connection) ---\n" + str(result))
        assert result

    def test_1_get_tables(self):
        tables = self.handler.get_tables()
        print("\n\n--- DEBUG (get_tables) ---\n" + str(tables))
        assert tables.type is not RESPONSE_TYPE.ERROR

    def test_2_get_columns(self):
        columns = self.handler.get_columns('baseballStats')
        print("\n\n--- DEBUG (get_columns) ---\n" + str(columns))
        assert columns.type is not RESPONSE_TYPE.ERROR

    def test_3_native_query_select(self):
        query = "topk(1, sum(rate(container_cpu_usage_seconds_total[30d])) by (cluster))"
        result = self.handler.native_query(query)
        print("\n\n--- DEBUG (native_query_select) ---\n" + str(result))
        assert result.type is RESPONSE_TYPE.TABLE

    def test_4_native_query_select(self):
        query = "http_requests_total_fake"
        result = self.handler.native_query(query)
        print("\n\n--- DEBUG (native_query_select_fake) ---\n" + str(result))
        assert result.type is RESPONSE_TYPE.TABLE

if __name__ == '__main__':
    unittest.main()
    