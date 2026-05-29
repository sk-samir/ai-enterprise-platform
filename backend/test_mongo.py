from app.tools.mongo_tool import MongoTool


result = MongoTool.insert(
    "chat_history",
    {
        "user": "samir",
        "message": "Hello MongoDB"
    }
)

print(result)


documents = MongoTool.fetch("chat_history")

print(documents)