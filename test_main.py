from fastapi.testclient import TestClient
from main import app  # 把你之前写的 FastAPI 餐厅实例引进来

# 实例化一个“神秘顾客”
client = TestClient(app)

def test_read_root():
    # 模拟浏览器访问首页
    response = client.get("/")
    # 断言 1：网页状态码必须是 200（代表成功访问）
    assert response.status_code == 200
    # 断言 2：返回的 JSON 数据必须和我们预设的一模一样
    assert response.json() == {"message": "Hello World! 我的第一个 AI 后端接口运行成功啦！"}

def test_ask_question():
    # 模拟用户提问法律问题
    test_query = "租房押金不退怎么办"
    response = client.get(f"/ask?query={test_query}")
    
    assert response.status_code == 200
    # 拿到服务器返回的数据
    data = response.json()
    
    # 断言：返回的数据里必须包含用户的原问题
    assert data["question"] == test_query
    # 断言：AI 的回答里必须包含“正在努力检索”这几个字
    assert "正在努力检索" in data["answer"]
