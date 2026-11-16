# Drill 1: Fix the dynamic route generator trap
def generate_endpoints():
    routes = []
    for path in ["/home", "/api", "/health"]:
        # TODO: Fix this lambda so each route returns its own specific path string
        # Right now, all of them will return "/health"
        local_path = path
        routes.append(lambda p=path: f"Handling {p}")
    return routes


# Drill 2: Stateful Rate Limiter using Closures and nonlocal
# Do NOT use a class.
def create_limiter(limit: int):
    cnt = 0

    def check_limit(req_id: str) -> bool:
        nonlocal cnt
        cnt += 1
        if cnt <= limit:
            return True
        else:
            return False

    return check_limit


if __name__ == "__main__":
    # Test 1
    funcs = generate_endpoints()
    assert funcs[0]() == "Handling /home", f"Failed: {funcs[0]()}"
    assert funcs[1]() == "Handling /api"
    assert funcs[2]() == "Handling /health"

    # Test 2
    limiter = create_limiter(2)
    assert limiter("req1") == True
    assert limiter("req2") == True
    assert limiter("req3") == False
    assert limiter("req4") == False

    print("LEGB & Closures Mastered.")
