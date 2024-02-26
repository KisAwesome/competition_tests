def retrieve_test():
    def load_func(func):
        globals()["test"] = func

    import os

    if os.path.exists(os.path.join(os.path.dirname(__file__), "test_cases_cache.py")):
        from test_cases_cache import test

        load_func(test)

    else:
        import urllib.request
        import ssl

        url = "https://raw.githubusercontent.com/KisAwesome/competition_tests/main/test.py"

        with urllib.request.urlopen(
            url, context=ssl._create_unverified_context()
        ) as response:
            if response.status == 200:

                content = response.read().decode("utf-8")

                with open(
                    os.path.join(os.path.dirname(__file__), "test_cases_cache.py"),
                    "w",
                    encoding="utf-8",
                ) as file:
                    file.write(content)
            else:
                print("Error please ask for help")
                return

        from test_cases_cache import test

        load_func(test)


retrieve_test()

