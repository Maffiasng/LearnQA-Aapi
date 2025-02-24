import pytest
import requests


class TestAgent:
    from test.some import useragents

    @pytest.mark.parametrize("agents", useragents)
    def test_user_agent(self, agents):
        headers = {"User-Agent": agents}

        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        response = requests.get(url, headers=headers)
        b = response.json()

        assert (
            b.get("platform") != "Unknown"
            and b.get("browser") != "Unknown"
            and b.get("device") != "Unknown"
        ), (
            f"Upss  значения 'Unknown'"
            f" {b.get("platform")} {b.get("browser")} {b.get("device")} "
        )
